import copy
class Module():
    def __init__(self
        ,name = ""
    ):
        self.input_lt = []
        self.output_lt = []
        self.inout_lt = []
        self.param_lt = []
        self.wire_lt = []
        self.IO_port_lt = []
        self.name = name
        pass

    def AddPort(self,port_obj):
        port_obj.SetOwner(self)
        self.IO_port_lt.append (port_obj)
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
        # for param in self.param_lt:
        #     param.LinkParameter(self.param_lt)
        
        for IO_port in self.IO_port_lt:
            IO_port.bitwidth.LinkParameter(self.param_lt)
        pass

class Instance(Module):
    def __init__(self,ClassModule,instName):
        cp = copy.deepcopy (ClassModule)
        # super(Instance, self).__init__(cp.name,cp.input_lt,cp.output_lt,cp.inout_lt,cp.param_lt)
        super(Instance, self).__init__(cp.name)

        for cp_port in cp.IO_port_lt:
            self.AddPort(cp_port)
        
        for cp_param in cp.param_lt:
            self.AddParameter(cp_param)

        # self = cp

        self.inst_name = instName
        # self.SetOwner(self)

class Wrapper(Module):
    # def __init__(self,ClassModule):
    #     cp = copy.deepcopy (ClassModule)
    #     super(Wrapper, self).__init__(cp.name,cp.input_lt,cp.output_lt,cp.inout_lt,cp.param_lt)
    #     self.SetOwner(self)
    def __init__(self,wrap_name):
        super(Wrapper, self).__init__(wrap_name)
        # self.SetOwner(self)

    def AddWire(self,wire_obj):
        self.wire_lt.append (wire_obj)
        wire_obj.SetOwner(self)
    
    # def AddWire(self,ClassWire):
    #     self.wire_lt.append (ClassWire)
    #     self.SetOwner(self)