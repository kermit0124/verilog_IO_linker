import re
import basic_component
import basic_parameter
import module
import bitwidth

class ClassVerilogParser():
    def __init__(self):
        self.src_txt_all = ""
        self.input_lt = []
        self.output_lt = []
        self.inout_lt = []
        self.param_lt = []
        self.parse_succ = False
        self.module_lt = []
        pass
    def LoadTxt(self,fileName):        
        fp = open (fileName,'r')
        self.src_txt_all = fp.read()
        fp.close()
        self.ParseTxt()
        pass
    def ParseTxt(self):
        self.module_lt = []
        self.src_txt_all_orig = self.src_txt_all
        self.src_txt_all = re.sub(r"/\*[\s\w\S\W]+?\*/","",self.src_txt_all)
        self.src_txt_all = re.sub(r"//.+","",self.src_txt_all)
        self.src_txt_module_lt = re.findall(r"module[\w\s\W\S]+?endmodule",self.src_txt_all)
        self.src_num_module = len(self.src_txt_module_lt)
        print ("Found moudule:" , self.src_num_module)
        for src_moduleAll in self.src_txt_module_lt:
            self.ClearAllModuleInfo()
            re_res2_lt = []
            re_res2_lt = re.findall(r"(module [\s\w\S\W]+?);([\s\w\S\W]+?)endmodule",src_moduleAll)

            if (len(re_res2_lt)>0):
                self.src_module_title = re_res2_lt[0][0]
                self.src_body = re_res2_lt[0][1]
                self.__ParseModuleTitle()
                self.__ParseModuleBody_IO_scan()
                self.parse_succ = True
                
                module_t = module.Module( self.module_name)

                port_type_lt = [
                    self.input_lt
                    ,self.output_lt
                    ,self.inout_lt
                ]
                for port_type in port_type_lt:
                    for port in port_type:
                        module_t.AddPort(port)
                
                for param in self.param_lt:
                    module_t.AddParameter(param)

                self.module_lt.append (module_t)

                # self.module_lt.append (
                #     module.Module(
                #         self.module_name
                #         ,self.input_lt
                #         ,self.output_lt
                #         ,self.inout_lt
                #         ,self.param_lt
                #     )
                # )

                # check = True
                # for moduleInfo in self.module_lt:
                #     if (moduleInfo.name == self.module_name):
                #         check = False

                # if (check):
                #     self.module_lt.append (
                #         module.Module(
                #             self.module_name
                #             ,self.input_lt
                #             ,self.output_lt
                #             ,self.inout_lt
                #             ,self.param_lt
                #         )
                #     )
                # else:
                #     print ("Module conflict: ",self.module_name)
            else:
                print ("Module format error")
            pass
        pass
    def GetModuleInfo(self):
        return (self.module_lt)
    def ClearAllModuleInfo(self):
        self.input_lt = []
        self.output_lt = []
        self.inout_lt = []
        self.param_lt = []
        self.parse_succ = False

    
    def __ParseModuleTitle(self):
        # rStr = r"module (.+?)([\s]+|)(#[\w\s\W\S]+?\)|)(\s+|)(\([\w\s\W\S]+\))"
        rStr = r"module (.+?)([\s]+|)(#(\s+|)([\w\s\W\S]+)\)|)(\s+|)(\(([\w\s\W\S]+)\))"
        
        re_res = re.findall(rStr,self.src_module_title)
        if (len(re_res)>0):
            re_res = re_res[0]
            self.module_name = re_res[0] if (re_res!=[]) else ""
            self.module_name = self.module_name.replace(" ","")
            
            if ("#") in self.src_module_title:
                # with parameter in title
                self.src_param_title = re_res[4]
                self.__ParseModuleTitle_param()
            
            self.src_module_title_IO = re_res[7]
            self.__ParseModuleTitle_IO_scan()
    
    def __ParseModuleTitle_param(self):
        rStr = r"parameter[\n ]+(\[(.+)\]|)([\n ]+|)(.+)=([\n ]+|)(.+?)(\n|,)"
        re_res_lt = re.findall(rStr,self.src_param_title)
        for para_seg in re_res_lt:
            depth = para_seg[1].replace(" ","")
            name = para_seg[3].replace(" ","")
            value = para_seg[5].replace(" ","")

            new_param = basic_parameter.ClassParameter(name,value,depth)

            new_param.LinkParameter(self.param_lt)



            self.param_lt.append (new_param)
    
        

    def __ParseModuleTitle_IO_scan(self):
        self.src_module_title_IO = self.src_module_title_IO.replace("\n","")
        for txt in self.src_module_title_IO.split(","):
            self.__ParseModuleIO_scan(txt)

    def __ParseModuleBody_IO_scan(self):
        type_keys = ["input","inout","output"]
        re_lt = re.findall("([\s\w\S\W]+?);",self.src_body.replace("\n",""))
        for txt in re_lt:
            self.__ParseModuleIO_scan(txt)
    def __ParseModuleIO_scan(self,txt):
        re2_lt = re.findall("(input|output|inout) +(wire|)( +|)(\[.+\]|)( +|)(.+)",txt)
        if (len(re2_lt)>0):
            re2_lt = re2_lt[0]
            temp_type = re2_lt[0].replace(" ","")
            temp_depth = re2_lt[3].replace(" ","")
            temp_name = re2_lt[5].replace(" ","")
            temp_name_lt = temp_name.split(",")
            for name in temp_name_lt:
                # print(name , temp_depth ,temp_type)
                if (temp_type =="input"):
                    self.input_lt.append (basic_component.ClassInput(name,temp_depth))
                elif (temp_type == "output"):
                    self.output_lt.append (basic_component.ClassOutput(name,temp_depth))
                elif (temp_type == "inout"):
                    self.inout_lt.append (basic_component.ClassInout(name,temp_depth))
                else:
                    print ("Type error:",name,temp_type,temp_depth)


def test():
    VP = ClassVerilogParser()
    VP.LoadTxt("1.0.0/test.v")
    VP.ParseTxt()
    pass


# test()