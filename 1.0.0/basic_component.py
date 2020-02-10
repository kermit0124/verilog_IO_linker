import re
class Depth_vector():
    def __init__(self,init_str = "[0:0]"):
        rm_lt = ["[","]"," "]
        for rm_char in rm_lt:
            init_str = init_str.replace(rm_char,"")

        self.vec_top = ""
        self.vec_down = ""
        self.verilog_str = ""
        self.verilog_overrideParam_str = ""
        re_txt = r"(.+):(.+)"
        re_res = re.match(re_txt,init_str)
        if (re_res!=None):
            self.vec_top = re_res.group(1)
            self.vec_down = re_res.group(2)

            vec_show = 1
            try:
                vec_top_int = int (self.vec_top)
                vec_down_int = int (self.vec_down)
                if ((vec_down_int == 0) & (vec_top_int == 0)):
                    vec_show = 0
            except ValueError:
                pass
            
            if (vec_show):
                self.verilog_str = "[ " + self.vec_top + " : " + self.vec_down + " ]"
        else:
            print ("Format error")
        pass
    def __repr__(self):
        return self.verilog_str


class Basic_component():
    def __init__(self,name_str,depth_d1_str="[0:0]",depth_d2_str=None,depth_d3_str=None):
        self.vec_lt = []
        self.dimension = 1 
        if (depth_d1_str==""):
            depth_d1_str = "[0:0]"
        self.vec_lt.append  (Depth_vector(depth_d1_str))
        if ((depth_d3_str == None) & (depth_d2_str != None)):
            self.vec_lt.append  (Depth_vector(depth_d2_str))
            dimension = 2
            pass
        elif (depth_d3_str != None):
            self.vec_lt.append  (Depth_vector(depth_d2_str))
            self.vec_lt.append  (Depth_vector(depth_d3_str))
            dimension = 3
        pass
        
        self.name = name_str


class ClassRegister(Basic_component):
    def __init__(self,name_str,depth_d1_str="[0:0]",depth_d2_str=None,depth_d3_str=None):
        super(ClassRegister, self).__init__(name_str,depth_d1_str,depth_d2_str,depth_d3_str)

class ClassWire(Basic_component):
    def __init__(self,name_str,depth_d1_str="[0:0]",depth_d2_str=None,depth_d3_str=None):
        super(ClassWire, self).__init__(name_str,depth_d1_str,depth_d2_str,depth_d3_str)
        self.assign_txt = ""
        self.assign_objID = None
        self.sample_assign = True
        self.wrapper_wire_name = None
        self.jump_link_objID = None
        self.scanable_src = False
        self.scanable_dest = False
        self.onwer_objID = None
        self.type = "wire"


class ClassInput(ClassWire):
    def __init__(self,name_str,depth_d1_str="[0:0]",depth_d2_str=None,depth_d3_str=None):
        super(ClassInput, self).__init__(name_str,depth_d1_str,depth_d2_str,depth_d3_str)
        self.asloOut = False
        self.type = "input"
class ClassOutput(ClassWire):
    def __init__(self,name_str,depth_d1_str="[0:0]",depth_d2_str=None,depth_d3_str=None):
        super(ClassOutput, self).__init__(name_str,depth_d1_str,depth_d2_str,depth_d3_str)
        self.type = "output"
class ClassInout(ClassWire):
    def __init__(self,name_str,depth_d1_str="[0:0]",depth_d2_str=None,depth_d3_str=None):
        super(ClassInout, self).__init__(name_str,depth_d1_str,depth_d2_str,depth_d3_str)
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