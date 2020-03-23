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
        self.proc_inst = None
        self.inst_lt = []
        self.jinja_tmpl = Template(" ")
        self.jinja_tmpl.environment.variable_start_string = "[{["
        self.jinja_tmpl.environment.variable_end_string = "]}]"
        self.jinja_tmpl = Template(basic_verilog_code_wrapHeader())
        self.proc_wrapper = None
        self.update_cnt = 0
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

        self.update_cnt += 1

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
        self.update_cnt += 1

    
    def Select_procInst(self,idx):
        self.proc_inst = self.inst_lt[idx]
    
    def LinkInstIO(self,src_obj,dest_obj):
        # dest_obj.assign_obj = src_obj
        # dest_obj.assign_txt = src_obj.wrapper_wire_name
        # dest_obj.jump_link_objID = None
        # dest_obj.sample_assign = True
        dest_obj.assign_obj = src_obj
        self.update_cnt += 1


    def LinkWrapWire(self,src_obj,dest_obj):
        # dest_obj.assign_obj = src_obj
        # dest_obj.assign_txt = src_obj.name
        # dest_obj.jump_link_objID = None
        # dest_obj.sample_assign = False
        self.update_cnt += 1

    
    def LinkParam(self,override_obj,inst_param_obj):
        inst_param_obj.override_obj = override_obj
        # dest_obj.override_txt = src_obj.name
        self.update_cnt += 1

    
    # def CfgPortParam(self,inst):
        # for key in ["input","inout","output"]:
        #     for port in inst.port_dict[key]:
        #         temp_str = port.vec_lt[0].verilog_str
        #         if (temp_str!=""):
        #             search_succ = False
        #             for param in inst.param_lt:
        #                 if (param.name) in temp_str:
        #                     port.vec_lt[0].verilog_overrideParam_str  = temp_str.replace(param.name,"("+param.override_txt+")")


    def CreateWireToWrapper(self,wireName,wireSeg,vec_d1="[0:0]",vec_d2=None,vec_d3=None,assign_obj=None):
        temp_wire = basic_component.ClassWire(wireName,vec_d1)
        self.proc_wrapper.AddWire(temp_wire)

    def CreateIO_toWrapper(self,itemName,type_str,vec_d1="[0:0]"):
        dict_class = {
            'input': basic_component.ClassInput(itemName,vec_d1)
            ,'inout':basic_component.ClassInout(itemName,vec_d1)
            ,'output': basic_component.ClassOutput(itemName,vec_d1)
        }
        new_port = dict_class[type_str]
        self.proc_wrapper.AddPort(new_port)

        self.update_cnt += 1

    def CreateParameterToWrapper(self,paramName,value,vec_d1=""):
        new_param = basic_parameter.ClassParameter(paramName,value,vec_d1)
        self.proc_wrapper.AddParameter(new_param)

    def CreateEmptyWrapper(self,wrapperName):
        self.proc_wrapper = module.Wrapper(wrapperName)
        self.update_cnt += 1

    # def CfgAllPortOverrider(self):
    #     for inst in self.inst_lt:
    #         self.CfgPortParam(inst)

    def LinkAllParameter(self):
        self.proc_wrapper.LinkAllParameter()
        for inst in self.inst_lt:
            inst.LinkAllParameter()

    def GenerateVerilogCode(self):
        
        self.GenVerilogCode_WrapHeader()

        self.GenVerilogCode_Inst()

    
    def GenVerilogCode_WrapHeader(self):
        self.jinja_tmpl = Template(basic_verilog_code_wrapHeader1())
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
            self.code_wrapperInst += code_wrapperInst



        # WIP inst func

        # self.gen_source = self.jinja_tmpl.render(
        #     wrapper_name = self.proc_wrapper.name
        #     ,wrapParams = self.proc_wrapper.param_lt
        #     ,wrapPort_lt = wrapPort_lt
        #     ,inst_lt = self.inst_lt
        #     ,proc_wrapper = self.proc_wrapper
        # )
        # print (self.gen_source)
        # return(self.gen_source)
    # def GenerateVerilogCode(self):
    #     # self.CfgAllPortOverrider()

    #     wrapPort_lt = []
    #     keys = ["input","output","inout"]
    #     for key in keys:
    #         for port in self.proc_wrapper.port_dict[key]:
    #             wrapPort_lt.append (port)

    #     self.gen_source = self.jinja_tmpl.render(
    #         wrapper_name = self.proc_wrapper.name
    #         ,wrapParams = self.proc_wrapper.param_lt
    #         ,wrapPort_lt = wrapPort_lt
    #         ,inst_lt = self.inst_lt
    #         ,proc_wrapper = self.proc_wrapper
    #     )
    #     print (self.gen_source)
    #     return(self.gen_source)




def basic_verilog_code_wrapHeader1():
        templateTxt = u"""
`timescale 1ns / 1ps

module [{[proc_wrapper.name]}] #(
{%-for wrapParam in proc_wrapper.param_lt%}
    parameter [{[wrapParam.name]}] = [{[wrapParam.value]}] {%if loop.last == False%},{%endif%}
{%-endfor%}
)
(
{%-for port in proc_wrapper.IO_lt%}
    [{[port.type]}] wire [{[port.bitwidth]}] [{[port.name]}] {%if loop.last == False%},{%endif%}
{%-endfor%}
);

// Wrapper wire 
{%-for wire in proc_wrapper.wire_lt%}
{%-if wire.inst_mapping_obj==None%}
wire [{[wire.bitwidth]}] [{[wire.name]}] ;
{%-endif%}
{%-endfor%}


"""
        return (templateTxt)

def basic_verilog_code_inst():
        templateTxt = u"""
// ## Instance: [{[inst.inst_name]}]
// ## IO wire
{%-for IO in inst.IO_lt%}
wire [{[IO.bitwidth.GetWrapMapWire_bitwidth()]}] [{[IO.wrap_mapping_obj.name]}] ;
{%-endfor%}
"""
# ---------------------



        b ="""
// ## Output port
{%-for IO in inst.IO_lt%}
wire [{[outPort.vec_lt[0].verilog_overrideParam_str]}] [{[outPort.wrapper_wire_name]}] ;
{%-endfor%}

[{[inst.name]}] # (
    {%-for param in inst.param_lt%}
    {%-if param.override_obj != None %}
    .[{[param.name]}] ( [{[param.override_obj.name]}] ) {%if loop.last == False%},{%endif%}
    {%-else%}
    //.[{[param.name]}] ( [{[param.override_obj.name]}] ) {%if loop.last == False%},{%endif%}
    {%-endif%}
    {%-endfor%}
)
[{[inst.inst_name]}] (
    {%-for key in inst_port_keys%}
    {%-set last_key = loop.last%}
    {%-for port in inst.port_dict[key]%}
    .[{[port.name]}] ( [{[port.assign_txt]}] ) {%if (loop.last == False or last_key==False)%},{%endif%}
    {%-endfor%}    
    {%-endfor%}    
);

"""
        return (templateTxt)









def basic_verilog_code_wrapHeader():
        templateTxt = u"""
{%-macro port_link_item(port)%}
{%-if (port.type != "output")%}
{%-if (port.assign_obj != None)%}[{[port.assign_obj.wrapper_wire_name]}]
{%-endif%}
{%-else%}[{[port.wrapper_wire_name]}]
{%-endif%}
{%- endmacro %}
{%-set inst_port_keys = [
"input"
,"output"
,"inout"
]%}
`timescale 1ns / 1ps

module [{[wrapper_name]}] #(
{%-for wrapParam in wrapParams%}
    parameter [{[wrapParam.name]}] = [{[wrapParam.value]}] {%if loop.last == False%},{%endif%}
{%-endfor%}
)
(
{%-for port in wrapPort_lt%}
    [{[port.type]}] wire [{[port.vec_lt[0]]}] [{[port.name]}] {%if loop.last == False%},{%endif%}
{%-endfor%}
);

// Wrapper wire 
{%-for wire in proc_wrapper.wire_lt%}
wire [{[wire.vec_lt[0]]}] [{[wire.name]}] ;
{%endfor%}

// Instance module
{%-for inst in inst_lt%}

// ## Instance: [{[inst.inst_name]}]
// ## Output port
{%-for outPort in inst.output_lt%}
wire [{[outPort.vec_lt[0].verilog_overrideParam_str]}] [{[outPort.wrapper_wire_name]}] ;
{%-endfor%}

[{[inst.name]}] # (
    {%-for param in inst.param_lt%}
    {%-if param.override_obj != None %}
    .[{[param.name]}] ( [{[param.override_obj.name]}] ) {%if loop.last == False%},{%endif%}
    {%-else%}
    //.[{[param.name]}] ( [{[param.override_obj.name]}] ) {%if loop.last == False%},{%endif%}
    {%-endif%}
    {%-endfor%}
)
[{[inst.inst_name]}] (
    {%-for key in inst_port_keys%}
    {%-set last_key = loop.last%}
    {%-for port in inst.port_dict[key]%}
    .[{[port.name]}] ( [{[port.assign_txt]}] ) {%if (loop.last == False or last_key==False)%},{%endif%}
    {%-endfor%}    
    {%-endfor%}    
);
{%-endfor%}

// Assign input/inout


{%-for wire in proc_wrapper.wire_lt%}
assign [{[wire.name]}] = [{[wire.assign_txt]}] ;
{%-endfor%}

// Wrapper IO
{%-for outPort in proc_wrapper.output_lt%}
{%-if (outPort.assign_obj != None)%}
assign [{[outPort.name]}] = [{[outPort.assign_txt]}] ;
{%-else%}
//assign [{[outPort.name]}] = [{[outPort.assign_txt]}] ;
{%-endif%}
{%-endfor%}

endmodule

"""
        return (templateTxt)


def basic_verilog_code_inst_2():
        templateTxt = u"""
axis_async_fifo #(
    .DEPTH(DEPTH),
    .DATA_WIDTH(DATA_WIDTH),
    .KEEP_ENABLE(EXPAND_BUS ? M_KEEP_ENABLE : S_KEEP_ENABLE),
    .KEEP_WIDTH(KEEP_WIDTH),
    .LAST_ENABLE(1),
    .ID_ENABLE(ID_ENABLE),
    .ID_WIDTH(ID_WIDTH),
    .DEST_ENABLE(DEST_ENABLE),
    .DEST_WIDTH(DEST_WIDTH),
    .USER_ENABLE(USER_ENABLE),
    .USER_WIDTH(USER_WIDTH),
    .FRAME_FIFO(FRAME_FIFO),
    .USER_BAD_FRAME_VALUE(USER_BAD_FRAME_VALUE),
    .USER_BAD_FRAME_MASK(USER_BAD_FRAME_MASK),
    .DROP_BAD_FRAME(DROP_BAD_FRAME),
    .DROP_WHEN_FULL(DROP_WHEN_FULL)
)
fifo_inst (
    // Common reset
    .async_rst(s_rst | m_rst),
    // AXI input
    .s_clk(s_clk),
    .s_axis_tdata(pre_fifo_axis_tdata),
    .s_axis_tkeep(pre_fifo_axis_tkeep),
    .s_axis_tvalid(pre_fifo_axis_tvalid),
    .s_axis_tready(pre_fifo_axis_tready),
    .s_axis_tlast(pre_fifo_axis_tlast),
    .s_axis_tid(pre_fifo_axis_tid),
    .s_axis_tdest(pre_fifo_axis_tdest),
    .s_axis_tuser(pre_fifo_axis_tuser),
    // AXI output
    .m_clk(m_clk),
    .m_axis_tdata(post_fifo_axis_tdata),
    .m_axis_tkeep(post_fifo_axis_tkeep),
    .m_axis_tvalid(post_fifo_axis_tvalid),
    .m_axis_tready(post_fifo_axis_tready),
    .m_axis_tlast(post_fifo_axis_tlast),
    .m_axis_tid(post_fifo_axis_tid),
    .m_axis_tdest(post_fifo_axis_tdest),
    .m_axis_tuser(post_fifo_axis_tuser),
    // Status
    .s_status_overflow(s_status_overflow),
    .s_status_bad_frame(s_status_bad_frame),
    .s_status_good_frame(s_status_good_frame),
    .m_status_overflow(m_status_overflow),
    .m_status_bad_frame(m_status_bad_frame),
    .m_status_good_frame(m_status_good_frame)
);
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
    core.LinkInstIO(core.inst_lt[0].port_dict["output"][0],core.inst_lt[1].port_dict["input"][0])
    
    # core.CreateWireToWrapper("wire_1","~rstn",assign_obj=core.inst_lt[0].port_dict["output"][0])
    core.CreateWireToWrapper("wire_1","~rstn",assign_obj=core.proc_wrapper.port_dict["input"][1])
    core.LinkWrapWire(core.proc_wrapper.port_dict["wire"][0],core.inst_lt[0].port_dict["input"][1])
    core.LinkParam(core.proc_wrapper.param_lt[0],core.inst_lt[0].param_lt[0])
    # core.CfgPortParam(core.inst_lt[0])
    core.LinkInstIO(core.inst_lt[0].port_dict["output"][0],core.proc_wrapper.output_lt[0])
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
    # core.LinkInstIO(core.inst_lt[0].port_dict["output"][0],core.inst_lt[1].port_dict["input"][0])
    
    # # core.CreateWireToWrapper("wire_1","~rstn",assign_obj=core.inst_lt[0].port_dict["output"][0])
    # core.CreateWireToWrapper("wire_1","~rstn",assign_obj=core.proc_wrapper.port_dict["input"][1])
    # core.LinkWrapWire(core.proc_wrapper.port_dict["wire"][0],core.inst_lt[0].port_dict["input"][1])
    # core.LinkParam(core.proc_wrapper.param_lt[0],core.inst_lt[0].param_lt[0])
    # # core.CfgPortParam(core.inst_lt[0])
    # core.LinkInstIO(core.inst_lt[0].port_dict["output"][0],core.proc_wrapper.output_lt[0])
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

    core.LinkInstIO(core.inst_lt[0].IO_lt[0],core.proc_wrapper.IO_lt[0])

    core.LinkParam(core.proc_wrapper.param_lt[0],core.inst_lt[0].param_lt[0])

    core.LinkAllParameter()
    core.GenerateVerilogCode()
    # core.proc_wrapper.GenerateWrapperInfo()
    a = 1
    # core.CreateWrapperFromModule(0)
    # core.LinkInstIO(core.inst_lt[0].port_dict["output"][0],core.inst_lt[1].port_dict["input"][0])
    
    # # core.CreateWireToWrapper("wire_1","~rstn",assign_obj=core.inst_lt[0].port_dict["output"][0])
    # core.CreateWireToWrapper("wire_1","~rstn",assign_obj=core.proc_wrapper.port_dict["input"][1])
    # core.LinkWrapWire(core.proc_wrapper.port_dict["wire"][0],core.inst_lt[0].port_dict["input"][1])
    # core.LinkParam(core.proc_wrapper.param_lt[0],core.inst_lt[0].param_lt[0])
    # # core.CfgPortParam(core.inst_lt[0])
    # core.LinkInstIO(core.inst_lt[0].port_dict["output"][0],core.proc_wrapper.output_lt[0])
    # core.CreateIO_toWrapper("abc_o","output")
    # core.GenerateVerilogCode()
    pass

test5()