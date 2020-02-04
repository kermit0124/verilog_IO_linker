import re
import copy
import module
import wrapper
import verilog_parser
import basic_component

class Core():
    def __init__(self):
        self.VP = verilog_parser.ClassVerilogParser()
        self.module_lt = []
        self.wrap_module_lt = None
        self.proc_inst = None
        self.inst_lt = []
        self.inst_update = False
        pass

    def CreateWrapperFromModule(self,module_idx=0):
        self.proc_wrapper = module.Wrapper(self.module_lt[module_idx])
        self.Config_wrapper_linkPoints()
        self.inst_update = True

    def ParseVerilogToModule(self,filePath):
        self.VP.LoadTxt(filePath)
        temp_module_lt = self.VP.GetModuleInfo()
        if (len(temp_module_lt)>0):
            for temp_module in temp_module_lt:
                check = True
                for moduleCheck in self.module_lt:
                    if (temp_module.name == moduleCheck.name):
                        check = False
                
                if (check):
                    self.module_lt.append (temp_module)
                else:
                    print ("Module conflict: ",temp_module.name)

    def CreateInstFromModule(self,inst_name,module_idx):
        temp_module = self.module_lt[module_idx]
        temp_inst = module.Instance(temp_module,inst_name)
        self.inst_lt.append (temp_inst)
        self.inst_update = True
        self.Config_inst_linkPoints(len(self.inst_lt)-1)
            
    def Config_inst_linkPoints(self,lt_idx):
        inst = self.inst_lt[lt_idx]
        key_lt = ["output","inout"]
        for key in key_lt:
            for port in inst.port_dict[key]:
                str = "_" + inst.inst_name + "__" + port.name
                port.wrapper_wire_name = str
                port.scanable_src = True
                
        key_lt = ["input","inout"]
        for key in key_lt:
            for port in inst.port_dict[key]:
                port.scanable_dest = True
        
    def Config_wrapper_linkPoints(self):
        key_lt = ["input","inout","wire"]
        for key in key_lt:
            for port in self.proc_wrapper.port_dict[key]:
                port.wrapper_wire_name = port.name
                port.scanable_src = True
        
        key_lt = ["output","inout","wire"]
        for key in key_lt:
            for port in self.proc_wrapper.port_dict[key]:
                port.scanable_dest = True

    
    def Select_procInst(self,idx):
        self.proc_inst = self.inst_lt[idx]
    
    def LinkInstIO(self,src_obj,dest_obj):
        dest_obj.assign_objID = src_obj
        dest_obj.assign_txt = src_obj.wrapper_wire_name
        dest_obj.jump_link_objID = None
        dest_obj.sample_assign = True

    def LinkWrapWire(self,src_obj,dest_obj):
        dest_obj.assign_objID = src_obj
        dest_obj.assign_txt = src_obj.name
        dest_obj.jump_link_objID = None
        dest_obj.sample_assign = False
        pass

    def CreateWireToWrapper(self,wireName,wireSeg,vec_d1="[0:0]",vec_d2=None,vec_d3=None,assign_objID=None):
        new_wire = basic_component.ClassWire(wireName,vec_d1,vec_d2,vec_d3)
        new_wire.assign_txt = wireSeg
        new_wire.scanable_src = True
        new_wire.sample_assign = False
        new_wire.assign_objID = assign_objID
        new_wire.wrapper_wire_name = wireName
        self.proc_wrapper.AddWire(new_wire)


def test2():
    core = Core()
    core.ParseVerilogToModule("D:/DevProjects/anaconda/verilog_IO_linker/1.0.0/test.v")
    core.ParseVerilogToModule("D:/DevProjects/anaconda/verilog_IO_linker/1.0.0/test_wrapper.v")
    core.CreateInstFromModule("instA_0",0)
    core.CreateInstFromModule("instA_1",0)
    core.CreateInstFromModule("instB_1",1)
    core.Select_procInst(0)
    core.CreateWrapperFromModule(0)
    core.LinkInstIO(core.inst_lt[0].port_dict["output"][0],core.inst_lt[1].port_dict["input"][0])
    
    # core.CreateWireToWrapper("wire_1","~rstn",assign_objID=core.inst_lt[0].port_dict["output"][0])
    core.CreateWireToWrapper("wire_1","~rstn",assign_objID=core.proc_wrapper.port_dict["input"][1])
    core.LinkWrapWire(core.proc_wrapper.port_dict["wire"][0],core.inst_lt[0].port_dict["input"][1])

    pass

def test():
    core = Core()
    core.ParseVerilogToModule("D:/DevProjects/anaconda/verilog_IO_linker/1.0.0/test.v")
    core.ParseVerilogToModule("D:/DevProjects/anaconda/verilog_IO_linker/1.0.0/test_wrapper.v")
    # core.ParseVerilogToModule("D:/DevProjects/anaconda/verilog_IO_linker/1.0.0/test.v")
    core.CreateInstFromModule("inst_0",0)
    core.CreateInstFromModule("inst_1",1)
    core.Select_procInst(0)
    # core.Config_data_bak(core.proc_inst,0)
    core.CreateWrapperFromModule(0)
    # core.Config_data_bak(core.proc_wrapper,1)

    # print (type(core.proc_wrapper))
    # print (type(core.proc_inst))
    # print (type(core.proc_inst) == type(core.inst_lt[1]))
    # dict = {
    #     "inst": core.inst_lt
    #     ,"module": core.module_lt
    #     ,"wrapper": core.proc_wrapper
    # }
    
    # key_lt = ["inst","module","wrapper"]
    # for key in key_lt:
    #     for inst in dict[key]:
    #         print (inst)

    for inst in core.inst_lt:
        dict_keys = ["input","inout","output","wire"]
        for key in dict_keys:
            for port in inst.port_dict[key]:
                print ("ID",port,"src/dest",port.scanable_src,port.scanable_dest)

    pass


# test2()