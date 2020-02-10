import re

class Basic_parameter():
    def __init__(self,name_str,depth_str=""):
        rm_lt = ["[","]"," "]
        for rm_word in rm_lt:
            depth_str = depth_str.replace(rm_word,"")
        
        if (depth_str!=''):
            depth_str = "[%s]"%depth_str

        self.depth_str = depth_str
        self.name = name_str


class ClassParameter(Basic_parameter):
    def __init__(self,name_str,value,depth_str=""):
        self.value = value
        self.override_txt = value
        self.override_objID = None
        self.ignore = False
        super(ClassParameter, self).__init__(name_str,depth_str)
    def GetVerilogCode(self):
        vec_str = self.depth_str if (self.depth_str!="") else ""
        rt = vec_str + self.name + " = " + self.value
        return (rt)

