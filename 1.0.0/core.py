import re
import copy
from jinja2 import Template

import module
import wrapper
import verilog_parser
import basic_component
import basic_parameter

class Core():
    def __init__(self):
        self.VP = verilog_parser.ClassVerilogParser()
        self.module_lt = []
        self.wrap_module_lt = None
        # self.proc_inst = None
        self.inst_lt = []
        self.jinja_tmpl = Template(" ")
        self.jinja_tmpl.environment.variable_start_string = "[{["
        self.jinja_tmpl.environment.variable_end_string = "]}]"
        # self.proc_wrapper = None
        self.update = False
        self.genVerilogCodeTxt = ''
        self.CreateEmptyWrapper("new_wrapper")
        self.src_lt = []
        self.dest_lt = []
        self.proc_inst = module.Instance(module.Module("init"),'init')
        pass

    def CreateWrapperFromModule(self,module_idx=0):
        sel_mod = self.module_lt[module_idx]
        self.proc_wrapper = module.Wrapper(sel_mod.name)

        for IO_port in sel_mod.IO_lt:
            cp_IO = copy.deepcopy(IO_port)
            self.proc_wrapper.AddPort(cp_IO)

        for param in sel_mod.param_lt:
            cp_param = copy.deepcopy(param)
            self.proc_wrapper.AddParameter(cp_param)

        if (self.inst_lt!=[]):
            for inst in self.inst_lt:
                self.proc_wrapper.AddInst(inst)

        self.update = True

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
        self.proc_wrapper.AddInst(temp_inst)
        self.update = True


    def Select_procInst(self,idx):
        self.proc_inst = self.inst_lt[idx]
        pass

    def LinkPoint(self,src_obj,dest_obj):
        dest_orig_obj = dest_obj
        src_orig_obj = src_obj
        if (isinstance(src_obj,basic_component.Class_IO_Port)):
            pass
            if (type(src_obj.owner_obj) == module.Instance):
                # src is inst IO
                src_obj = src_obj.mapWrap_obj
                pass
            else:
                # src is wrap IO
                pass
        else:
            # src is wrap wire
            pass

        if (isinstance(dest_obj,basic_component.Class_IO_Port)):
            pass
            if (type(dest_obj.owner_obj) == module.Instance):
                dest_obj = dest_obj.mapWrap_obj
                pass
            else:
                pass
        else:
            pass
        # dest_obj.SetAssign(src_obj)
        dest_obj.assign_obj = src_obj
        self.update = True


    def LinkParam(self,override_obj,inst_param_obj):
        inst_param_obj.override_obj = override_obj
        self.update = True


    def CreateWireToWrapper(self,wireName,wireSeg,bitwidth="[0:0]"):
        temp_wire = basic_component.ClassWire(wireName,bitwidth)
        self.proc_wrapper.AddWire(temp_wire)

    def CreateIO_toWrapper(self,itemName,type_str,bitwidth="[0:0]"):
        dict_class = {
            'input': basic_component.ClassInput(itemName,bitwidth)
            ,'inout':basic_component.ClassInout(itemName,bitwidth)
            ,'output': basic_component.ClassOutput(itemName,bitwidth)
        }
        new_port = dict_class[type_str]
        self.proc_wrapper.AddPort(new_port)

        self.update = True

    def CreateParameterToWrapper(self,paramName,value,bitwidth=""):
        new_param = basic_parameter.ClassParameter(paramName,value,bitwidth)
        self.proc_wrapper.AddParameter(new_param)

    def CreateEmptyWrapper(self,wrapperName):
        self.proc_wrapper = module.Wrapper(wrapperName)
        self.update = True

    # def CfgAllPortOverrider(self):
    #     for inst in self.inst_lt:
    #         self.CfgPortParam(inst)

    def LinkAllParameter(self):
        self.proc_wrapper.LinkAllParameter()
        for inst in self.inst_lt:
            inst.LinkAllParameter()

    def GenerateVerilogCode(self):

        self.LinkAllParameter()

        self.GenVerilogCode_WrapHeader()
        self.GenVerilogCode_Inst()
        self.GenVerilogCode_instWireAssign()
        self.GenVerilogCode_wrapWireAssign()

        self.genVerilogCodeTxt = self.code_wrapperHeader    \
            + self.code_wrapperInst     \
            + self.code_instWireAssign  \
            + self.code_wrapWireAssign  \
            + '\nendmodule '
        # print (self.genVerilogCodeTxt)
        return (self.genVerilogCodeTxt)


    def GenVerilogCode_WrapHeader(self):
        self.jinja_tmpl = Template(basic_verilog_code_wrapHeader())
        self.code_wrapperHeader = self.jinja_tmpl.render(
            proc_wrapper = self.proc_wrapper
        )
        # print (self.code_wrapperHeader)

    def GenVerilogCode_Inst(self):
        self.code_wrapperInst = ''
        self.jinja_tmpl = Template(basic_verilog_code_inst())
        for inst in self.proc_wrapper.inst_lt:

            code_wrapperInst = self.jinja_tmpl.render(
                inst = inst
            )
            # print (code_wrapperInst)
            self.code_wrapperInst += code_wrapperInst

    def GenVerilogCode_instWireAssign(self):
        self.code_instWireAssign = ''
        self.jinja_tmpl = Template(basic_verilog_code_instWireAssign())

        # Instance wire assign
        for inst in self.proc_wrapper.inst_lt:
            any_assign = False
            filter_assign_IO_lt = []
            for IO in inst.IO_lt:
                if (IO.mapWrap_obj.assign_obj!=None):
                    any_assign = True
                    filter_assign_IO_lt.append (IO)

            if (any_assign==True):

                code_instWireAssign = self.jinja_tmpl.render(
                    inst = inst
                    ,IO_lt = filter_assign_IO_lt
                )

                # print (code_instWireAssign)

                self.code_instWireAssign += code_instWireAssign

    def GenVerilogCode_wrapWireAssign(self):
        # Wrapper wire assign
        self.code_wrapWireAssign = ''
        self.jinja_tmpl = Template(basic_verilog_code_wrapWireAssign())

        wire_lt = []
        for wire in self.proc_wrapper.wire_lt:
            if ((wire.assign_obj != None ) & (wire.mapInst_obj == None)):
                wire_lt.append (wire)

        IO_lt = []
        for IO in self.proc_wrapper.IO_lt:
            if (IO.assign_obj != None):
                IO_lt.append (IO)


        code_wrapWireAssign = self.jinja_tmpl.render(
            wrap = self.proc_wrapper
            ,wire_lt = wire_lt
            ,IO_lt = IO_lt
        )
        # print (code_wrapWireAssign)
        self.code_wrapWireAssign += code_wrapWireAssign

    def GetLinkablePointList(self,scan_dest):
        rt_lt = []

        if (scan_dest):
            typeChk_wrap_lt = [
                basic_component.ClassOutput
                ,basic_component.ClassInout
            ]
            typeChk_inst_lt = [
                basic_component.ClassInput
                ,basic_component.ClassInout
            ]
        else:
            typeChk_wrap_lt = [
                basic_component.ClassInput
                ,basic_component.ClassInout
            ]
            typeChk_inst_lt = [
                basic_component.ClassOutput
                ,basic_component.ClassInout
            ]

        for IO in self.proc_wrapper.IO_lt:
            
            for typeChk in typeChk_wrap_lt:
                if (type(IO)==typeChk):
                    rt_lt.append (IO)
        
        for wire in self.proc_wrapper.wire_lt:
            if (wire.mapInst_obj==None):
                rt_lt.append (wire)

        for inst in self.proc_wrapper.inst_lt:
            for IO in inst.IO_lt:
                for typeChk in typeChk_inst_lt:
                    if (type(IO)==typeChk):
                        rt_lt.append (IO)

        if (scan_dest):
            self.dest_lt = rt_lt
            return (self.dest_lt)
        else:
            self.src_lt = rt_lt
            return (self.src_lt)

    def GetUpdateResult(self):
        rt = self.update
        if (self.update):
            self.update = False
        return (rt)



def basic_verilog_code_wrapHeader():
        templateTxt = u"""
`timescale 1ns / 1ps

module [{[proc_wrapper.name]}] #(
{%-for wrapParam in proc_wrapper.param_lt%}
    parameter [{[wrapParam.name]}] = [{[wrapParam.value]}] {%if loop.last == False%},{%endif%}
{%-endfor%}
)
(
{%-for port in proc_wrapper.IO_lt%}
    [{[port.type]}] wire[{[port.bitwidth]}] [{[port.name]}] {%if loop.last == False%},{%endif%}
{%-endfor%}
);

// Wrapper wire
{%-for wire in proc_wrapper.wire_lt%}
{%-if wire.mapInst_obj==None%}
wire [{[wire.bitwidth]}] [{[wire.name]}] ;
{%-endif%}
{%-endfor%}


"""
        return (templateTxt)

def basic_verilog_code_inst():
        templateTxt = u"""

// -----------------------------------------------------
// ### Instance: [[{[inst.inst_name]}]] ###
// ## Parameter override
{%-for param in inst.param_lt%}
localparam[{[param.GetBitwidth()]}] [{[param.GetWrapRuleName()]}] = [{[param.GetWrapMapParamValue()]}] ;
{%-endfor%}

// ## IO wire
{%-for IO in inst.IO_lt%}
wire [{[IO.bitwidth.GetWrapMapWire_bitwidth()]}] [{[IO.mapWrap_obj.name]}] ;
{%-endfor%}

[{[inst.name]}] # (
    {%-for param in inst.param_lt%}
    .[{[param.name]}] ( [{[param.GetWrapRuleName()]}] ) {%if loop.last == False%},{%endif%}
    {%-endfor%}
)
[{[inst.inst_name]}] (
    {%-for IO in inst.IO_lt%}
    .[{[IO.name]}] ( [{[IO.mapWrap_obj.name]}] ) {%if (loop.last == False or last_key==False)%},{%endif%}
    {%-endfor%}
) ;
// ### Instance: [[{[inst.inst_name]}]] ###
// -----------------------------------------------------

"""

        return (templateTxt)


def basic_verilog_code_instWireAssign():
    templateTxt = u"""

// -----------------------------------------------------
// ### Wire assign - instance : [[{[inst.inst_name]}]] ###
{%-for IO in IO_lt%}
assign [{[IO.mapWrap_obj.name]}] = [{[IO.mapWrap_obj.assign_obj.name]}] ;
{%-endfor%}
// -----------------------------------------------------

"""

    return (templateTxt)

def basic_verilog_code_wrapWireAssign():
    templateTxt = u"""

{%-if wire_lt != []%}
// -----------------------------------------------------
// ### Wire assign - wrapper : [[{[wrap.name]}]] ###
{%-for wire in wire_lt%}
assign [{[wire.name]}] = [{[wire.assign_obj.name]}] ;
{%-endfor%}
// -----------------------------------------------------
{%-endif%}

// -----------------------------------------------------
// ### IO assign - wrapper : [[{[wrap.name]}]] ###
{%-for IO in IO_lt%}
assign [{[IO.name]}] = [{[IO.assign_obj.name]}] ;
{%-endfor%}
// -----------------------------------------------------
"""

    return (templateTxt)






def test2():
    core = Core()
    core.ParseVerilogToModule("D:/DevProjects/anaconda/verilog_IO_linker/1.0.0/test.v")
    core.ParseVerilogToModule("D:/DevProjects/anaconda/verilog_IO_linker/1.0.0/test_wrapper.v")
    core.CreateInstFromModule("instA_0",0)
    core.CreateInstFromModule("instA_1",0)
    core.CreateInstFromModule("instB_1",1)
    core.Select_procInst(0)
    core.CreateWrapperFromModule(0)
    core.LinkPoint(core.inst_lt[0].port_dict["output"][0],core.inst_lt[1].port_dict["input"][0])

    # core.CreateWireToWrapper("wire_1","~rstn",assign_obj=core.inst_lt[0].port_dict["output"][0])
    core.CreateWireToWrapper("wire_1","~rstn",assign_obj=core.proc_wrapper.port_dict["input"][1])
    core.LinkWrapWire(core.proc_wrapper.port_dict["wire"][0],core.inst_lt[0].port_dict["input"][1])
    core.LinkParam(core.proc_wrapper.param_lt[0],core.inst_lt[0].param_lt[0])
    # core.CfgPortParam(core.inst_lt[0])
    core.LinkPoint(core.inst_lt[0].port_dict["output"][0],core.proc_wrapper.output_lt[0])
    core.CreateIO_toWrapper("abc_o","output")
    core.GenerateVerilogCode()
    pass


def test3():
    core = Core()
    core.ParseVerilogToModule("D:/DevProjects/anaconda/verilog_IO_linker/1.0.0/test.v")
    core.ParseVerilogToModule("D:/DevProjects/anaconda/verilog_IO_linker/1.0.0/test_wrapper.v")
    core.CreateInstFromModule("instA_0",0)
    core.CreateInstFromModule("instA_1",0)
    core.CreateInstFromModule("instB_1",1)
    core.Select_procInst(0)
    core.CreateEmptyWrapper("Top_wrapper")
    core.CreateParameterToWrapper("asb",10,"[abc-1:0]")
    core.CreateIO_toWrapper("abc_o","output","[asb-1:0]")
    # core.CreateWrapperFromModule(0)
    # core.LinkPoint(core.inst_lt[0].port_dict["output"][0],core.inst_lt[1].port_dict["input"][0])

    # # core.CreateWireToWrapper("wire_1","~rstn",assign_obj=core.inst_lt[0].port_dict["output"][0])
    # core.CreateWireToWrapper("wire_1","~rstn",assign_obj=core.proc_wrapper.port_dict["input"][1])
    # core.LinkWrapWire(core.proc_wrapper.port_dict["wire"][0],core.inst_lt[0].port_dict["input"][1])
    # core.LinkParam(core.proc_wrapper.param_lt[0],core.inst_lt[0].param_lt[0])
    # # core.CfgPortParam(core.inst_lt[0])
    # core.LinkPoint(core.inst_lt[0].port_dict["output"][0],core.proc_wrapper.output_lt[0])
    # core.CreateIO_toWrapper("abc_o","output")
    # core.GenerateVerilogCode()
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


def test4():
    core = Core()
    core.ParseVerilogToModule("D:\\DevProjects\\Vivado\\IP_Design\\CMOS-Python_Sys\\python_data_proc\\python_data_proc.srcs\\sources_1\\python_data_proc.sv")
    core.ParseVerilogToModule("D:\\DevProjects\\Vivado\\IP_Design\\CMOS-Python_Sys\\python_data_proc\\python_data_proc.srcs\\sources_1\\sub\\training\\data_training_v4\\top_data_training.v")



def test5():
    core = Core()
    core.ParseVerilogToModule("D:/DevProjects/anaconda/verilog_IO_linker/1.0.0/test.v")
    core.ParseVerilogToModule("D:/DevProjects/anaconda/verilog_IO_linker/1.0.0/test_wrapper.v")

    # core.CreateEmptyWrapper("Top_wrapper")
    core.CreateWrapperFromModule(2)

    core.CreateInstFromModule("instA_0",0)
    core.CreateInstFromModule("instA_1",0)
    core.CreateInstFromModule("instB_1",1)
    core.Select_procInst(0)


    core.CreateParameterToWrapper("asb",'10',"[abc-1:0]")
    core.CreateIO_toWrapper("abc_o","output","[asb-1:0]")
    core.CreateIO_toWrapper("abc_i","input","")
    core.CreateWireToWrapper('_zz_','~rst')
    core.CreateWireToWrapper('_zz2_','~rstn','[3:0]')

    core.CreateParameterToWrapper('bbb','5')
    core.CreateParameterToWrapper('aa112b','5')
    core.CreateParameterToWrapper('pp','aa112b*bbb-5')

    # core.proc_wrapper.LinkAllParameter()





    # core.proc_wrapper.ShowPorts(basic_component.ClassOutput)
    # print ('--')
    # core.inst_lt[0].ShowPorts(basic_component.ClassOutput)
    # core.proc_wrapper.ShowParams()

    core.LinkPoint(core.inst_lt[0].IO_lt[1],core.inst_lt[1].IO_lt[2])

    core.LinkPoint(core.inst_lt[0].IO_lt[0],core.proc_wrapper.IO_lt[0])
    core.LinkPoint(core.proc_wrapper.IO_lt[1],core.inst_lt[0].IO_lt[1])
    core.LinkPoint(core.proc_wrapper.IO_lt[1],core.proc_wrapper.wire_lt[1])
    core.LinkPoint(core.proc_wrapper.IO_lt[1],core.proc_wrapper.wire_lt[60])

    core.LinkParam(core.proc_wrapper.param_lt[0],core.inst_lt[0].param_lt[0])


    core.LinkAllParameter()
    core.GenerateVerilogCode()
    # core.proc_wrapper.GenerateWrapperInfo()
    print (core.genVerilogCodeTxt)
    src_lt = core.GetLinkablePointList(False)
    dest_lt = core.GetLinkablePointList(True)
    a = 1
    # core.CreateWrapperFromModule(0)
    # core.LinkPoint(core.inst_lt[0].port_dict["output"][0],core.inst_lt[1].port_dict["input"][0])

    # # core.CreateWireToWrapper("wire_1","~rstn",assign_obj=core.inst_lt[0].port_dict["output"][0])
    # core.CreateWireToWrapper("wire_1","~rstn",assign_obj=core.proc_wrapper.port_dict["input"][1])
    # core.LinkWrapWire(core.proc_wrapper.port_dict["wire"][0],core.inst_lt[0].port_dict["input"][1])
    # core.LinkParam(core.proc_wrapper.param_lt[0],core.inst_lt[0].param_lt[0])
    # # core.CfgPortParam(core.inst_lt[0])
    # core.LinkPoint(core.inst_lt[0].port_dict["output"][0],core.proc_wrapper.output_lt[0])
    # core.CreateIO_toWrapper("abc_o","output")
    # core.GenerateVerilogCode()
    pass

# test5()