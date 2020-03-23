import copy
import basic_component
class Module():
    def __init__(self
        ,name = ""
    ):
        self.input_lt = []
        self.output_lt = []
        self.inout_lt = []
        self.param_lt = []
        self.wire_lt = []
        self.IO_lt = []
        self.name = name
        pass

    def SetModuleName(self,name):
        self.name = name

    def AddWire(self,wire_obj):
        wire_obj.SetOwner(self)
        self.wire_lt.append (wire_obj)

    def AddPort(self,port_obj):
        port_obj.SetOwner(self)
        self.IO_lt.append (port_obj)
        pass

    def AddParameter(self,param_obj):
        param_obj.SetOwner(self)
        self.param_lt.append (param_obj)

    def SetOwner(self,onwer_objID):
        keys = [
            "input"
            ,"inout"
            ,"output"
            ,"wire"
        ]
        for key in keys:
            for port in self.port_dict[key]:
                port.onwer_objID = onwer_objID
    
    def LinkAllParameter(self):
        for IO_port in self.IO_lt:
            IO_port.bitwidth.LinkParameter(self.param_lt)
        
        for param in self.param_lt:
            param.LinkParameter(self.param_lt)

        for wire in self.wire_lt:
            if (wire.inst_mapping_obj!=None):
                wire.bitwidth.LinkParameter(wire.inst_mapping_obj.owner_obj.param_lt)
    
    
    def ShowPorts(self,type_class = None):
        for port in self.IO_lt:
            if (type_class!=None):
                if (type(port) == type_class):
                    print (port.name)
            else:
                print (port.name)
    
    def ShowParams(self):
        for param in self.param_lt:
            print (param.name)

class Instance(Module):
    def __init__(self,ClassModule,instName):
        cp = copy.deepcopy (ClassModule)
        super(Instance, self).__init__(cp.name)

        for cp_port in cp.IO_lt:
            self.AddPort(cp_port)
        
        for cp_param in cp.param_lt:
            self.AddParameter(cp_param)

        self.inst_name = instName


class Wrapper(Module):
    def __init__(self,wrap_name):
        super(Wrapper, self).__init__(wrap_name)
        self.inst_lt = []

    def AddInst(self,inst_obj):
        for IO in inst_obj.IO_lt:
            wire_name = IO.GetWrapWireName()
            new_wire = basic_component.ClassWire(wire_name,IO.bitwidth.str)
            new_wire.SetInstMapping(IO)
            IO.SetWrapMapping(new_wire)
            self.AddWire(new_wire)
        self.inst_lt.append (inst_obj)

    
    def RemoveInst(self,inst_index):
        del self.inst_lt[inst_index]

    def AddWire(self,wire_obj):
        self.wire_lt.append (wire_obj)
        wire_obj.SetOwner(self)

    def GenerateWrapperInfo(self):
        for inst in self.inst_lt:
            print (inst.IO_lt)
            pass