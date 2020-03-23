import re
import wx
import wx_gui.mainFrame
import wx_gui.moduleManagerFrame
import wx_gui.verilogCodeFrame
import verilog_parser
import linker
import core

class ModuleManagerFrame ( wx_gui.moduleManagerFrame.ModuleManagerFrame):	
    def __init__( self, parent ,core):
        wx_gui.moduleManagerFrame.ModuleManagerFrame.__init__(self,parent)
        # core.Core.__init__(self)
        self.core = core
    
    def SetObject(self):
        pass
    def GenNewVerilogParser(self):
        pass
    
    def UpdateInstList(self):
        self.m_listBox__inst.Clear()
        for inst in self.core.inst_lt:
            self.m_listBox__inst.Append(inst.inst_name)
    def UpdateParamList(self):
        self.m_listBox__override_param.Clear()
        for param in self.core.proc_inst.param_lt:
            str = param.GetVerilogCode()
            info = " :: " + param.override_txt
            if (param.ignore == True):
                info = " :: ignore"
            str += info
            self.m_listBox__override_param.Append(str)
    def UpdateWrapperParam(self):
        self.m_listBox__wrapper_param.Clear()
        for param in self.core.proc_wrapper.param_lt:
            str = param.GetVerilogCode()
            self.m_listBox__wrapper_param.Append(str)
        pass


    # wx gui event
    def filePicker__onFileChanged(self,event):
        fp = self.m_filePicker__loadFile.GetPath()
        try:
            f = open (fp,"r")
            f.close()
            self.core.ParseVerilogToModule(fp)
            self.m_listBox__parser_module.Clear()
            for moduleInfo in self.core.module_lt:
                self.m_listBox__parser_module.Append(moduleInfo.name)
        except FileNotFoundError:
            print("File error")
            pass
    def parser_module__onListBox( self, event ):
        tempStr = self.m_listBox__parser_module.GetStringSelection()
        self.m_textCtrl__inst_name.SetValue(tempStr+"_inst")
    def inst__onButtonClick( self, event ):
        sel_num = self.m_listBox__parser_module.GetSelection()
        module_sel = self.core.module_lt[sel_num]
        inst_name = self.m_textCtrl__inst_name.GetValue()
        self.core.CreateInstFromModule(inst_name,sel_num)
        self.UpdateInstList()
    def inst__onListBox( self, event ):
        self.core.Select_procInst(self.m_listBox__inst.GetSelection())
        self.UpdateParamList()
    def loadAsWrapper__onBtnClick( self, event ):
        sel_num = self.m_listBox__parser_module.GetSelection()
        self.core.CreateWrapperFromModule(sel_num)
        self.UpdateWrapperParam()
    def mapping__onBtnClick( self, event ):
        num_instParam = self.m_listBox__override_param.GetSelection()
        num_wrapParam = self.m_listBox__wrapper_param.GetSelection()
        # self.core.proc_inst.param_lt[num_instParam].override_txt = self.core.proc_wrapper.param_lt[num_wrapParam].name
        self.core.LinkParam(self.core.proc_wrapper.param_lt[num_wrapParam],self.core.proc_inst.param_lt[num_instParam])
        self.UpdateParamList()
        self.m_listBox__override_param.Select((num_instParam+1)%self.m_listBox__override_param.GetCount())
        self.m_listBox__wrapper_param.Select((num_wrapParam+1)%self.m_listBox__wrapper_param.GetCount())
    
    def createNewWrapper__onBtnClick( self, event ):
        wrapName = self.m_textCtrl__createNewWrapper.GetValue()
        self.core.CreateEmptyWrapper(wrapName)

    def overrideParamByConst__onBtnClick( self, event ):
        pass
    
    def createNewParam__onBtnClick( self, event ):
        paramName = self.m_textCtrl__newParam_name.GetValue()
        paramValue = self.m_textCtrl_newParam_value.GetValue()
        paramName = paramName.replace(" ","")
        re_res_lt = re.findall(r"(\[.+\])(.+)",paramName)
        paramDepth = ''
        if (len(re_res_lt)>0):
            re_res_lt = re_res_lt[0]
            paramName = re_res_lt[1]
            paramDepth = re_res_lt[0]

        if ((paramName!='') & (paramValue!='')):
            self.core.CreateParameterToWrapper(paramName,paramValue,paramDepth)
            self.UpdateWrapperParam()
        pass

class MainFrame ( wx_gui.mainFrame.MainFrame ):	
    def __init__( self, parent ):
        super(MainFrame,self).__init__(parent)
        self.core = core.Core()
        self.update_cnt = 0
        self.moduleManagerFrame = ModuleManagerFrame(None,self.core)
        self.verilogCodeFrame = VerilogCodeFrame(None,self.core)
        self.verilogCodeFrame.Show()
    
    def Update_all_list(self):
        self.Update_src_list()
        self.Update_dest_list()


    def Update_dest_list(self):
        self.destList_objID_lt = self.ScanListToShow(True)
        self.UpdateListItem(self.m_listBox__dest,self.destList_objID_lt,True)


    def Update_src_list(self):
        self.srcList_objID_lt = self.ScanListToShow(False)
        self.UpdateListItem(self.m_listBox__src,self.srcList_objID_lt)

        pass

    def UpdateListItem(self,classList,objID_lt,isDestList = False):
        type_str_dict = {
            "input":"I"
            ,"inout":"IO"
            ,"output":"O"
            ,"wire":"W"
        }
        classList.Clear()
        
        for obj in objID_lt:
            type_str = type_str_dict[obj.type]
            if (obj.onwer_objID==self.core.proc_wrapper):
                str_inst = "wrapper"
            else:
                str_inst = obj.onwer_objID.inst_name
            if (len(obj.vec_lt)>0):
                str_depth = obj.vec_lt[0]
            else:
                str_depth = ""
            str_port_name = obj.name
            if (obj.assign_obj!=None):
                str_src_name = obj.assign_obj.wrapper_wire_name
            else:
                str_src_name = ""
            str = "[%s:%s] %s%s: %s"%(str_inst,type_str,str_depth,str_port_name,str_src_name)
            classList.Append(str)

    
    def ScanListToShow(self,isDest=False):
        
        rt = []
        if (isDest):
            keys = ["output","inout"]
        else:
            keys = ["input","inout","wire"]
        
        for key in keys:
            for port in self.core.proc_wrapper.port_dict[key]:
                rt.append (port)


        if (isDest):
            keys = ["input","inout"]
        else:
            keys = ["output","inout"]

        for inst in self.core.inst_lt:
            for key in keys:
                for port in inst.port_dict[key]:
                    rt.append (port)
        return (rt)
        
    def Update_src_list_bak(self):
        self.src_inst_lt = []
        self.src_objID_lt = []
        self.src_mapListIdx_lt = []
        for inst in self.core.inst_lt:
            cnt = 0
            for output in inst.output_lt:
                self.src_inst_lt.append (inst)
                self.src_objID_lt.append (output)
                self.src_mapListIdx_lt.append (cnt)
                cnt += 1
        
        cnt = 0
        for input in self.core.proc_wrapper.input_lt:
            self.src_inst_lt.append (self.core.proc_wrapper)
            self.src_objID_lt.append (input)
            self.src_mapListIdx_lt.append (cnt)

        cnt = 0
        for wire in self.core.proc_wrapper.wire_lt:
            self.src_inst_lt.append (self.core.proc_wrapper)
            self.src_objID_lt.append (wire)
            self.src_mapListIdx_lt.append (cnt)


        self.m_listBox__src.Clear()
        for idx,objID in enumerate(self.src_objID_lt):
            if (self.src_inst_lt[idx]!=self.core.proc_wrapper):
                txt = "[" + self.src_inst_lt[idx].inst_name + ":O] "
                txt += objID.name
            else:
                # print (type(objID))
                txt = "[Wrapper:I]"
                txt += objID.name
            self.m_listBox__src.Append (txt)

    # event
    def menu_moduleManager__onMenuSel( self , event ):
        self.moduleManagerFrame.Show()

    def mainFrame__onAct( self , event ):
        if (self.core.update_cnt!=self.update_cnt):
            self.update_cnt = self.core.update_cnt
            self.Update_all_list()
            
    def connect__onBtnClick( self , event ):
        for dest_sel_num in self.m_listBox__dest.GetSelections():
            src_sel_num = self.m_listBox__src.GetSelections()[0]
            sel_dest = self.destList_objID_lt[dest_sel_num]
            sel_src = self.srcList_objID_lt[src_sel_num]
            self.core.LinkInstIO(sel_src,sel_dest)

            self.Update_dest_list()

            self.m_listBox__dest.SetSelection((dest_sel_num+1)%self.m_listBox__dest.GetCount())

            self.m_listBox__src.Deselect(src_sel_num)
            self.m_listBox__src.SetSelection((src_sel_num+1)%self.m_listBox__src.GetCount())

    def src__onListBox( self , event ):
        get_sel = self.m_listBox__src.GetSelections()
        if (get_sel!=[]):
            src_sel_num = get_sel[0]
            sel_src = self.srcList_objID_lt[src_sel_num]
            self.m_textCtrl__agnModeSeg.SetLabel(sel_src.wrapper_wire_name)

    def create_wireIO__onBtnClick( self, event ):
        name = self.m_textCtrl__createWireName.GetValue()
        segm = self.m_textCtrl__createWireSeg.GetValue()

        re_res_lt = re.findall(r"(input|output|inout|wire|)( |)(\[.+\]|)(.+)",name)
        if (len(re_res_lt)>0):
            re_res_lt = re_res_lt[0]
            # IO_type = re_res_lt[0]
            IO_type = self.m_choice__create_wireIO_type.GetStringSelection()
            if (IO_type=='wire'):
                if (segm.replace(' ','') == ''):
                    segm = '0'
                self.core.CreateWireToWrapper(name,segm)
            else:
                IO_depth = re_res_lt[2]
                IO_name = re_res_lt[3].replace(' ','')
                self.core.CreateIO_toWrapper(IO_name,IO_type,IO_depth)
        
        self.Update_all_list()

class VerilogCodeFrame ( wx_gui.verilogCodeFrame.VerilogCodeFrame ):	
    def __init__( self, parent , core):
        super(VerilogCodeFrame,self).__init__(parent)
        self.core = core
        self.update_cnt = 0
    
    def VerilogCodeFrame__onAct( self, event ):
        if (self.core.proc_wrapper!=None):
            if (self.update_cnt!=self.core.update_cnt):
                self.m_richText__showGen.SetValue(self.core.GenerateVerilogCode())
                self.update_cnt = self.core.update_cnt

def main():
    app=wx.App()
    mainFrame=MainFrame(None)
    mainFrame.Show()
    # moduleManagerFrame.Show()
    app.MainLoop()


main()