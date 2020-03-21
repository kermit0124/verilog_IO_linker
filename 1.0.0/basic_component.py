import re
import bitwidth

class Basic_component():
    def __init__(self,name_str,depth_d1_str='[0:0]'):
        self.name = name_str
        self.bitwidth = bitwidth.Bitwidth(depth_d1_str,self)
        self.owner_obj = None
        self.assign_from_obj = None
    
    def SetOwner(self,owner_obj):
        self.owner_obj = owner_obj
    def SetAssign(self,assign_from_obj):
        self.assign_from_obj = assign_from_obj


class ClassRegister(Basic_component):
    def __init__(self,name_str,depth_d1_str="[0:0]",depth_d2_str=None,depth_d3_str=None):
        super(ClassRegister, self).__init__(name_str,depth_d1_str)

class ClassWire(Basic_component):
    def __init__(self,name_str,depth_d1_str="[0:0]"):
        super(ClassWire, self).__init__(name_str,depth_d1_str)
        self.scanable_src = False
        self.scanable_dest = False
        self.type = "wire"

class ClassInput(ClassWire):
    def __init__(self,name_str,depth_d1_str="[0:0]"):
        super(ClassInput, self).__init__(name_str,depth_d1_str)
        self.asloOut = False
        self.type = "input"
class ClassOutput(ClassWire):
    def __init__(self,name_str,depth_d1_str="[0:0]"):
        super(ClassOutput, self).__init__(name_str,depth_d1_str)
        self.type = "output"
class ClassInout(ClassWire):
    def __init__(self,name_str,depth_d1_str="[0:0]"):
        super(ClassInout, self).__init__(name_str,depth_d1_str)
        self.asloOut = True
        self.type = "inout"

def test():
    # DV = Depth_vector("aa  -1 :0")
    # DV = Depth_vector("[aa  -1 :0]")
    # DV = Depth_vector("[aa  -1 :0") #]


    # a = Basic_component("test_name","","[3:0]","a-4:0")
    # a = Basic_component("test_name","","[3:0]","0:s")
    # a = Basic_component("test_name","","[3:0]","0:0")
    a = ClassInput("test_name","1:0")
    pass


# test()