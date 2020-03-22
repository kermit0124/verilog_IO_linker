import re

import basic_component
import basic_parameter
import bitwidth
import module


class ClassVerilogParser():
    def __init__(self):
        self.src_txt_all = ""
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

                self.proc_module = module.Module('new')
                self.parse_succ = True
                self.src_module_title = re_res2_lt[0][0]
                self.src_body = re_res2_lt[0][1]

                self.__ParseModuleTitle()

                self.proc_module.SetModuleName(self.module_name)

                self.__ParseModuleBody_param()
                self.__ParseModuleBody_IO_scan()

                if (self.parse_succ==True):
                    print ('Module parse success:%s'%(self.proc_module.name))
                    self.module_lt.append (self.proc_module)


            else:
                print ("Module format error")
            pass
        pass
    def GetModuleInfo(self):
        return (self.module_lt)
    def ClearAllModuleInfo(self):
        self.parse_succ = False

    
    def __ParseModuleTitle(self):
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

            self.__ParseModule_paramGenerate(name,depth,value)

    def __ParseModuleBody_param(self):
        rStr = r"parameter(( |)\[(.+)\]| )(.+?)=(.+?);"
        re_res_lt = re.findall(rStr,self.src_body.replace('\n',''))
        for seg in re_res_lt:
            name = seg[3].replace(" ","")
            value = seg[4].replace(" ","")
            depth = seg[2].replace(" ","")
            self.__ParseModule_paramGenerate(name,depth,value)


    def __ParseModule_paramGenerate(self,name,depth,value):
        new_param = basic_parameter.ClassParameter(name,value,depth)
        self.proc_module.AddParameter(new_param)


    def __ParseModuleTitle_IO_scan(self):
        self.src_module_title_IO = self.src_module_title_IO.replace("\n","")
        for txt in self.src_module_title_IO.split(","):
            self.__ParseModule_IOportGenerate(txt)

    def __ParseModuleBody_IO_scan(self):
        re_lt = re.findall("([\s\w\S\W]+?);",self.src_body.replace("\n",""))
        for txt in re_lt:
            self.__ParseModule_IOportGenerate(txt)

    def __ParseModule_IOportGenerate(self,txt):
        re2_lt = re.findall("(input|output|inout) +(wire|)( +|)(\[.+\]|)( +|)(.+)",txt)
        if (len(re2_lt)>0):
            re2_lt = re2_lt[0]
            temp_type = re2_lt[0].replace(" ","")
            temp_depth = re2_lt[3].replace(" ","")
            temp_name = re2_lt[5].replace(" ","")
            temp_name_lt = temp_name.split(",")
            for name in temp_name_lt:
                typeError = False
                dict_class = {
                    'input': basic_component.ClassInput(name,temp_depth)
                    ,'output': basic_component.ClassOutput(name,temp_depth)
                    ,'inout': basic_component.ClassInout(name,temp_depth)
                }
                try:
                    new_port = dict_class[temp_type]
                except KeyError:
                    typeError = True
                
                if (typeError == False):
                    self.proc_module.AddPort(new_port)
                else:
                    self.parse_succ = False



def test():
    VP = ClassVerilogParser()
    VP.LoadTxt("1.0.0/test.v")
    VP.ParseTxt()
    pass


# test()
