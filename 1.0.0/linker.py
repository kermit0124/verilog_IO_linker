import re
import module
import wrapper

# class ClassParameter(Basic_component):
#     def __init__(self,name_str,value,depth_d1_str="[0:0]"):
#         self.value = value
#         super(ClassParameter, self).__init__(name_str,depth_d1_str,None,None)

class ClassLinker():
    def __init__(self):
        # super(ClassLinker, self).__init__(name_str,depth_d1_str,None,None)
        self.ClearInst()
        self.wrapper = wrapper.Wrapper("")
        pass
    def ClearInst(self):
        self.inst_lt = []
    
    def AddInst(self,moduleInfo,instName):
        temp = module.Instance(moduleInfo,instName)
        self.inst_lt.append (temp)



def test():
    pass


# test()