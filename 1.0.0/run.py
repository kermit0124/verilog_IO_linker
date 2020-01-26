import re
import wx
import wx_gui.mainFrame
import wx_gui.moduleManagerFrame
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
        self.core.proc_inst.param_lt[num_instParam].override_txt = self.core.proc_wrapper.param_lt[num_wrapParam].name
        self.UpdateParamList()
        self.m_listBox__override_param.Select((num_instParam+1)%self.m_listBox__override_param.GetCount())
        self.m_listBox__wrapper_param.Select((num_wrapParam+1)%self.m_listBox__wrapper_param.GetCount())
    

class MainFrame ( wx_gui.mainFrame.MainFrame ):	
    def __init__( self, parent ):
        super(MainFrame,self).__init__(parent)
        self.core = core.Core()
        self.moduleManagerFrame = ModuleManagerFrame(None,self.core)
    
    def Update_all_list(self):
        self.Update_src_list()
        self.Update_dest_list()

    def Update_dest_list(self):
        self.dest_inst_lt = []
        self.dest_objID_lt = []
        self.dest_mapListIdx_lt = []
        
        for inst in self.core.inst_lt:
            cnt = 0
            for input in inst.input_lt:
                self.dest_inst_lt.append (inst)
                self.dest_objID_lt.append (input)
                self.dest_mapListIdx_lt.append (cnt)
                cnt += 1
        
        cnt = 0
        for output in self.core.proc_wrapper.output_lt:
            self.dest_inst_lt.append (self.core.proc_wrapper)
            self.dest_objID_lt.append (output)
            self.dest_mapListIdx_lt.append (cnt)

        self.m_listBox__dest.Clear()
        for idx,objID in enumerate(self.dest_objID_lt):
            if (self.dest_inst_lt[idx]!=self.core.proc_wrapper):
                txt = "[" + self.dest_inst_lt[idx].inst_name + ":I] "
                txt += objID.name
                txt += " :: "
                txt += objID.assign_txt
            else:
                txt = "[Wrapper:O]"
                txt += objID.name
                txt += " :: "
                txt += objID.assign_txt
            self.m_listBox__dest.Append (txt)



        
    def Update_src_list(self):
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
                print (type(objID))
                txt = "[Wrapper:I]"
                txt += objID.name
            self.m_listBox__src.Append (txt)

    # event
    def menu_moduleManager__onMenuSel( self , event ):
        self.moduleManagerFrame.Show()

    def mainFrame__onAct( self , event ):
        if (self.core.inst_update):
            self.core.inst_update = False
            self.Update_all_list()
    def connect__onBtnClick( self , event ):
        for dest_sel_num in self.m_listBox__dest.GetSelections():
            src_sel_num = self.m_listBox__src.GetSelections()[0]
            sel_dest = self.dest_objID_lt[dest_sel_num]
            sel_src = self.src_objID_lt[src_sel_num]
            self.core.LinkInstIO(sel_dest,sel_src)

            self.Update_dest_list()

            self.m_listBox__dest.SetSelection((dest_sel_num+1)%self.m_listBox__dest.GetCount())

            self.m_listBox__src.Deselect(src_sel_num)
            self.m_listBox__src.SetSelection((src_sel_num+1)%self.m_listBox__src.GetCount())

    def src__onListBox( self , event ):
        src_sel_num = self.m_listBox__src.GetSelections()[0]
        sel_src = self.src_objID_lt[src_sel_num]
        self.m_textCtrl__agnModeSeg.SetLabel(sel_src.wrapper_wire_name)

    def createWire__onBtnClick( self, event ):
        wireName = self.m_textCtrl__createWireName.GetValue()
        wireSeg = self.m_textCtrl__createWireSeg.GetValue()
        self.core.CreateWireToWrapper(wireName,wireSeg)
        self.Update_src_list()

def main():
    app=wx.App()
    mainFrame=MainFrame(None)
    mainFrame.Show()
    # moduleManagerFrame.Show()
    app.MainLoop()


main()