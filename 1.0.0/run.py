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
        pass
    def UpdateParamList(self):
        self.m_listBox__override_param.Clear()
        # inst_sel = self.core.inst_lt[self.m_listBox__inst.GetSelection()]
        for param in self.core.proc_inst.param_lt:
            str = param.name
            if (param.override_obj != None):
                str += " :: " + param.override_obj.name
            
            self.m_listBox__override_param.Append (str)
        pass
    def UpdateWrapperParam(self):
        self.m_listBox__wrapper_param.Clear()
        for param in self.core.proc_wrapper.param_lt:
            str = param.name
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
        pass
    def loadAsWrapper__onBtnClick( self, event ):
        sel_num = self.m_listBox__parser_module.GetSelection()
        self.core.CreateWrapperFromModule(sel_num)
        self.UpdateWrapperParam()
    def mapping__onBtnClick( self, event ):
        num_instParam = self.m_listBox__override_param.GetSelection()
        num_wrapParam = self.m_listBox__wrapper_param.GetSelection()
        wrap_param_obj = self.core.proc_wrapper.param_lt[num_wrapParam]
        inst_param_obj = self.core.proc_inst.param_lt[num_wrapParam]
        # # self.core.proc_inst.param_lt[num_instParam].override_txt = self.core.proc_wrapper.param_lt[num_wrapParam].name
        self.core.LinkParam(wrap_param_obj,inst_param_obj)
        self.UpdateParamList()

        self.m_listBox__override_param.Select((num_instParam+1)%self.m_listBox__override_param.GetCount())
        self.m_listBox__wrapper_param.Select((num_wrapParam+1)%self.m_listBox__wrapper_param.GetCount())
        pass
    
    def createNewWrapper__onBtnClick( self, event ):
        wrapName = self.m_textCtrl__createNewWrapper.GetValue()
        self.core.CreateEmptyWrapper(wrapName)

    def overrideParamByConst__onBtnClick( self, event ):
        pass
    
    def createNewParam__onBtnClick( self, event ):
        # paramName = self.m_textCtrl__newParam_name.GetValue()
        # paramValue = self.m_textCtrl_newParam_value.GetValue()
        # paramName = paramName.replace(" ","")
        # re_res_lt = re.findall(r"(\[.+\])(.+)",paramName)
        # paramDepth = ''
        # if (len(re_res_lt)>0):
        #     re_res_lt = re_res_lt[0]
        #     paramName = re_res_lt[1]
        #     paramDepth = re_res_lt[0]

        # if ((paramName!='') & (paramValue!='')):
        #     self.core.CreateParameterToWrapper(paramName,paramValue,paramDepth)
        #     self.UpdateWrapperParam()
        pass

class MainFrame ( wx_gui.mainFrame.MainFrame ):	
    def __init__( self, parent ):
        super(MainFrame,self).__init__(parent)
        self.core = core.Core()
        self.update_cnt = 0
        self.moduleManagerFrame = ModuleManagerFrame(None,self.core)
        self.verilogCodeFrame = VerilogCodeFrame(None,self.core)
        self.verilogCodeFrame.Show()

        self.debug()
    
    
    def debug(self):
        self.moduleManagerFrame.Show()
        self.moduleManagerFrame.m_filePicker__loadFile.SetPath('D:\\Share\\python\\verilog_IO_linker\\1.0.0\\test.v')
        self.moduleManagerFrame.filePicker__onFileChanged(None)
    def Update_all_list(self):
        type_str_dict = {
            'input': 'I'
            ,'inout': 'IO'
            ,'output': 'O'
            ,'wire': 'W'
        }

        self.core.GetLinkablePointList(False)
        self.core.GetLinkablePointList(True)

        list_func_lt = [[self.m_listBox__src,self.core.src_lt],[self.m_listBox__dest,self.core.dest_lt]]
        
        for listBox,point_lt in list_func_lt:
            listBox.Clear()
            for point in point_lt:
                try:
                    owner_name = point.owner_obj.inst_name + '/'
                except AttributeError:
                    owner_name = ''
                self.list_item_str = '%s%s(%s)'%(owner_name,point.name,type_str_dict[point.type])

                if (listBox == self.m_listBox__dest):
                    self.Update_all_list_assign_src_str(point)

                listBox.Append (self.list_item_str)
        pass
    def Update_all_list_assign_src_str(self,point):
            assign_check = False
            if (point.assign_obj != None):
                # Inst IO / wrap wire
                if (point.assign_obj.mapInst_obj!=None):
                    redir_obj = point.assign_obj.mapInst_obj
                    assign_name = redir_obj.owner_obj.inst_name + '/' + redir_obj.name
                else:
                    assign_name = point.assign_obj.name
                assign_check = True
            elif (point.mapWrap_obj != None):
                if (point.mapWrap_obj.assign_obj != None):
                    # assign_name = point.owner_obj.inst_name + '/' + point.name
                    assign_name = point.name
                    assign_check = True

            if (assign_check):
                self.list_item_str += '<= %s'%(assign_name)

    # event
    def menu_moduleManager__onMenuSel( self , event ):
        self.moduleManagerFrame.Show()

    def mainFrame__onAct( self , event ):
        if (self.core.GetUpdateResult()):
            self.Update_all_list()
            
    def connect__onBtnClick( self , event ):
        for dest_sel_num in self.m_listBox__dest.GetSelections():
            src_sel_num = self.m_listBox__src.GetSelections()[0]
            sel_dest_obj = self.core.dest_lt[dest_sel_num]
            sel_src_obj = self.core.src_lt[src_sel_num]
            self.core.LinkPoint(sel_src_obj,sel_dest_obj)

            self.Update_all_list()

            self.m_listBox__dest.SetSelection((dest_sel_num+1)%self.m_listBox__dest.GetCount())

            self.m_listBox__src.Deselect(src_sel_num)
            self.m_listBox__src.SetSelection((src_sel_num+1)%self.m_listBox__src.GetCount())

    def src__onListBox( self , event ):
        # get_sel = self.m_listBox__src.GetSelections()
        # if (get_sel!=[]):
        #     src_sel_num = get_sel[0]
        #     sel_src = self.srcList_objID_lt[src_sel_num]
        #     self.m_textCtrl__agnModeSeg.SetLabel(sel_src.wrapper_wire_name)
        pass

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
        pass
        if (self.core.proc_wrapper!=None):
            self.m_richText__showGen.SetValue(self.core.GenerateVerilogCode())


def main():
    app=wx.App()
    mainFrame=MainFrame(None)
    mainFrame.Show()
    # moduleManagerFrame.Show()
    app.MainLoop()


main()