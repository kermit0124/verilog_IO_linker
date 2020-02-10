import re
import basic_component
import basic_parameter
import module

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
                self.parse_succ = True
                
                self.module_lt.append (
                    module.Module(
                        self.module_name
                        ,self.input_lt
                        ,self.output_lt
                        ,self.inout_lt
                        ,self.param_lt
                    )
                )

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
        rStr = r"module (.+) "
        re_res = re.findall(rStr,self.src_module_title)
        self.module_name = re_res[0] if (re_res!=[]) else ""
        
        if ("#") in self.src_module_title:
            # with parameter in title
            self.__ParseModuleTitle_param()
        self.__ParseModuleTitle_IO_scan()
    
    def __ParseModuleTitle_param(self):
        rStr = r"parameter[\n ]+(\[(.+)\]|)([\n ]+|)(.+)=([\n ]+|)(.+?)(\n|,)"
        re_res_lt = re.findall(rStr,self.src_module_title)
        for para_seg in re_res_lt:
            depth = para_seg[1].replace(" ","")
            name = para_seg[3].replace(" ","")
            value = para_seg[5].replace(" ","")
            self.param_lt.append (basic_parameter.ClassParameter(name,value,depth))
        

    def __ParseModuleTitle_IO_scan(self):
        self.parseModuleTitle_IO_type_sel = "input"
        self.__ParseModuleTitle_IO_type()
        self.parseModuleTitle_IO_type_sel = "output"
        self.__ParseModuleTitle_IO_type()
        self.parseModuleTitle_IO_type_sel = "inout"
        self.__ParseModuleTitle_IO_type()

    def __ParseModuleTitle_IO_type(self):
        rStr = self.parseModuleTitle_IO_type_sel
        rStr = rStr + "[\n| ]+(wire|)[\n| ]+(\[(.+)\]|)(.+?)(,|\n)"
        re_res_lt = re.findall(rStr,self.src_module_title)
        # print (self.parseModuleTitle_IO_type_sel)
        for io_seg in re_res_lt:
            IO_name = io_seg[3].replace(" ","")
            IO_depth = io_seg[2].replace(" ","")
            if (self.parseModuleTitle_IO_type_sel == "input"):
                self.input_lt.append (basic_component.ClassInput(IO_name,IO_depth))
            elif (self.parseModuleTitle_IO_type_sel == "output"):
                self.output_lt.append (basic_component.ClassOutput(IO_name,IO_depth))
            else:
                self.inout_lt.append (basic_component.ClassInout(IO_name,IO_depth))
            # print (IO_name , IO_depth)


def test():
    VP = ClassVerilogParser()
    VP.LoadTxt("1.0.0/test.v")
    VP.ParseTxt()
    pass


# test()