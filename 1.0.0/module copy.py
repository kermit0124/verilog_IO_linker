import copy
class Module():
    def __init__(self
        ,name = ""
        ,input_lt = []
        ,output_lt = []
        ,inout_lt = []
        ,param_lt = []
        ,wire_lt = []
    ):
        self.input_lt = input_lt
        self.output_lt = output_lt
        self.inout_lt = inout_lt
        self.param_lt = param_lt
        self.wire_lt = wire_lt
        self.port_dict = {
            "input": self.input_lt
            ,"inout": self.inout_lt
            ,"output": self.output_lt
            ,"wire": self.wire_lt
        }
        self.name = name
        pass

    def AddPort(self,port_obj):
        pass

    def SetOnwer(self,onwer_objID):
        keys = [
            "input"
            ,"inout"
            ,"output"
            ,"wire"
        ]
        for key in keys:
            for port in self.port_dict[key]:
                port.onwer_objID = onwer_objID

class Instance(Module):
    def __init__(self,ClassModule,instName):
        cp = copy.deepcopy (ClassModule)
        super(Instance, self).__init__(cp.name,cp.input_lt,cp.output_lt,cp.inout_lt,cp.param_lt)
        self.inst_name = instName
        self.SetOnwer(self)

class Wrapper(Module):
    def __init__(self,ClassModule):
        cp = copy.deepcopy (ClassModule)
        super(Wrapper, self).__init__(cp.name,cp.input_lt,cp.output_lt,cp.inout_lt,cp.param_lt)
        self.SetOnwer(self)

    
    def AddWire(self,ClassWire):
        self.wire_lt.append (ClassWire)
        self.SetOnwer(self)