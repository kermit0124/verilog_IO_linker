import re
import wx
import wx_gui.mainFrame
import wx_gui.moduleManagerFrame
import wx_gui.verilogCodeFrame
import wx_gui.createPointDialog
import verilog_parser
import linker
import core

class CreatePointDialog ( wx_gui.createPointDialog.CreatePointDialog):	
    def __init__( self, parent ,core):
        wx_gui.createPointDialog.CreatePointDialog.__init__(self,parent)
        self.core = core

    def UpdatePointInfo(self):
        name = self.m_textCtrl__point_name.GetValue()
        bit = self.m_textCtrl__point_bit.GetValue()
        if (bit==''):
            bit = '0:0'
        wire_assign_code = self.m_textCtrl__wire_assign_code.GetValue()
        point_type = self.m_choice__create_point_type.GetStringSelection()
        info_str = '(%s) [%s] %s'%(point_type,bit,name)
        if (point_type=='wire'):
            info_str += ' = %s'%(wire_assign_code)
        self.m_staticText__pointInfo.SetLabel(info_str)

    def point_type__onChoice( self, event ):
        if (self.m_choice__create_point_type.GetStringSelection()=='wire'):
            self.m_textCtrl__wire_assign_code.Enable()
        else:
            self.m_textCtrl__wire_assign_code.Disable()
        self.UpdatePointInfo()

    def point_bit__onText( self, event ):
        self.UpdatePointInfo()

    def wire_assign_code__onText( self, event ):
        self.UpdatePointInfo()

    def point_name__onText( self, event ):
        self.UpdatePointInfo()

    def create_point__onBtnClick( self, event ):
        name = self.m_textCtrl__point_name.GetValue()
        bit = self.m_textCtrl__point_bit.GetValue()
        wire_assign_code = self.m_textCtrl__wire_assign_code.GetValue()
        point_type = self.m_choice__create_point_type.GetStringSelection()
        self.core.CreateIO_toWrapper(name,point_type,bit)

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
    def UpdateInstParam(self):
        self.m_listBox__override_param.Clear()
        for param in self.core.proc_inst.param_lt:
            str = param.name
            if (param.override_obj != None):
                str += " :: " + param.override_obj.name
            
            self.m_listBox__override_param.Append (str)
        pass
    def UpdateWrapperParam(self):
        self.m_listBox__wrapper_param.Clear()
        for param in self.core.proc_wrapper.param_lt:
            str = '%s = %s'%(param.name,param.value)
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
        self.UpdateInstParam()
        pass
    def loadAsWrapper__onBtnClick( self, event ):
        sel_num = self.m_listBox__parser_module.GetSelection()
        self.core.CreateWrapperFromModule(sel_num)
        self.UpdateWrapperParam()
    def mapping__onBtnClick( self, event ):
        num_instParam = self.m_listBox__override_param.GetSelection()
        num_wrapParam = self.m_listBox__wrapper_param.GetSelection()
        wrap_param_obj = self.core.proc_wrapper.param_lt[num_wrapParam]
        inst_param_obj = self.core.proc_inst.param_lt[num_instParam]
        
        self.core.LinkParam(wrap_param_obj,inst_param_obj)
        self.UpdateInstParam()

        self.m_listBox__override_param.Select((num_instParam+1)%self.m_listBox__override_param.GetCount())
        self.m_listBox__wrapper_param.Select((num_wrapParam+1)%self.m_listBox__wrapper_param.GetCount())
        pass
    
    def createNewWrapper__onBtnClick( self, event ):
        wrapName = self.m_textCtrl__createNewWrapper.GetValue()
        self.core.CreateEmptyWrapper(wrapName)

    def overrideParamByConst__onBtnClick( self, event ):
        value = self.m_textCtrl__setInstParamByConst.GetValue()
        if (value.replace(' ','')!=''):
            param_num = self.m_listBox__override_param.GetSelection()
            param_obj = self.core.proc_inst.param_lt[param_num]
            param_obj.value = value
            self.UpdateInstParam()
        pass
    
    def createNewParam__onBtnClick( self, event ):
        paramName = self.m_textCtrl__newParam_name.GetValue()
        paramValue = self.m_textCtrl_newParam_value.GetValue()
        paramName = paramName.replace(" ","")
        re_res_lt = re.findall(r"(\[.+\])(.+)",paramName)
        paramBit = ''
        if (len(re_res_lt)>0):
            re_res_lt = re_res_lt[0]
            paramName = re_res_lt[1]
            paramBit = re_res_lt[0]

        if ((paramName!='') & (paramValue!='')):
            self.core.CreateParameterToWrapper(paramName,paramValue,paramBit)
            self.UpdateWrapperParam()
        pass

    def delWrapParam__onBtnClick( self,event ):
        param_num = self.m_listBox__wrapper_param.GetSelection()
        self.core.proc_wrapper.RemoveParam(param_num)
        self.UpdateWrapperParam()
        self.UpdateInstParam()
    
    def clearInstParamOverride__onBtnClick( self,event ):
        param_num = self.m_listBox__override_param.GetSelection()
        self.core.proc_inst.param_lt[param_num].override_obj = None
        self.UpdateInstParam()


class MainFrame ( wx_gui.mainFrame.MainFrame ):	
    def __init__( self, parent ):
        super(MainFrame,self).__init__(parent)
        self.core = core.Core()
        self.update_cnt = 0
        self.moduleManagerFrame = ModuleManagerFrame(None,self.core)
        self.verilogCodeFrame = VerilogCodeFrame(None,self.core)
        self.verilogCodeFrame.Show()
        self.createPointDialog = CreatePointDialog(None,self.core)
        self.createPointDialog.Hide()
        self.listBoxDest_selection = []

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
                self.list_item_str = '%s(%s)'%(self.core.GetPointFullName(point),type_str_dict[point.type])

                if (listBox == self.m_listBox__dest):
                    self.Update_all_list_assign_src_str(point)

                listBox.Append (self.list_item_str)
        pass
    def Update_all_list_assign_src_str(self,dest_obj):
        assign_name = self.core.GetPointLinkFullName(dest_obj)
        if (assign_name!=''):
            self.list_item_str += '<= %s'%(assign_name)
    def ShowPointMessage(self,call_by_dest=False):
        point_lt = self.core.src_lt
        ctrlList_obj = self.m_listBox__src
        basic_info = self.m_textCtrl__src_info

        if (call_by_dest):
            point_lt = self.core.dest_lt
            ctrlList_obj = self.m_listBox__dest
            basic_info = self.m_textCtrl__dest_info

        sel_num = None
        sel_lt = ctrlList_obj.GetSelections()
        if (sel_lt != []):
            sel_num = sel_lt [0]

        if (sel_num!=None):
            sel_point_obj = point_lt [sel_num]

            if (type(sel_point_obj.owner_obj)==core.module.Instance):
                owner_type = 'Inst'
            else:
                owner_type = 'Wrap'

            bitwidth_str = str(sel_point_obj.bitwidth)
            if (bitwidth_str==''):
                bitwidth_str = '[0:0]'

            basic_info_str = 'Name: %s\nType: %s\nBitwidth: %s\nOwner: [%s]%s \n' %(
                sel_point_obj.name
                ,sel_point_obj.type
                ,bitwidth_str
                ,owner_type
                ,sel_point_obj.owner_obj.name
            )

            if (call_by_dest):
                sel_assign_name = self.core.GetPointLinkFullName(sel_point_obj)
                if (sel_assign_name!=''):
                    basic_info_str += 'Assign: %s'%(sel_assign_name)
            else:
                self.m_listBox__src_linkTo.Clear()
                cnt = 0
                for dest in self.core.dest_lt:
                    if (self.core.GetPointLinkObj(dest)==sel_point_obj):
                        dest_name = self.core.GetPointFullName(dest)
                        cnt += 1
                        linkTo_str = '%d - %s'%(cnt,dest_name)
                        self.m_listBox__src_linkTo.Append (dest_name)
                        if (cnt == 1):
                            basic_info_str += 'Link to:\n'
                        basic_info_str += linkTo_str + '\n'
            
            basic_info.SetValue(basic_info_str)


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

            if (self.m_menuItem__autoNext.IsChecked()):
                self.m_listBox__dest.SetSelection((dest_sel_num+1)%self.m_listBox__dest.GetCount())

                self.m_listBox__src.Deselect(src_sel_num)
                self.m_listBox__src.SetSelection((src_sel_num+1)%self.m_listBox__src.GetCount())
            else:
                self.m_listBox__src.SetSelection(src_sel_num)
                self.m_listBox__dest.SetSelection(dest_sel_num)

    def src__onListBox( self , event ):
        self.ShowPointMessage(False)
        

    def dest__onListBox( self , event ):
        if (self.m_menuItem__multSel.IsChecked()==False):
            if (self.listBoxDest_selection!=[]):
                temp_sel = self.m_listBox__dest.GetSelections()
                new_sel = list(set(temp_sel).difference(set(self.listBoxDest_selection)))
                old_sel = list(set(temp_sel).difference(set(new_sel)))
                for sel in old_sel:
                    self.m_listBox__dest.Deselect(sel)
        self.listBoxDest_selection = self.m_listBox__dest.GetSelections()

        self.ShowPointMessage(True)
        

    def create_wireIO__onBtnClick( self, event ):
        # name = self.m_textCtrl__createWireName.GetValue()
        # segm = self.m_textCtrl__createWireSeg.GetValue()

        # re_res_lt = re.findall(r"(input|output|inout|wire|)( |)(\[.+\]|)(.+)",name)
        # if (len(re_res_lt)>0):
        #     re_res_lt = re_res_lt[0]
        #     # IO_type = re_res_lt[0]
        #     IO_type = self.m_choice__create_wireIO_type.GetStringSelection()
        #     if (IO_type=='wire'):
        #         if (segm.replace(' ','') == ''):
        #             segm = '0'
        #         self.core.CreateWireToWrapper(name,segm)
        #     else:
        #         IO_depth = re_res_lt[2]
        #         IO_name = re_res_lt[3].replace(' ','')
        #         self.core.CreateIO_toWrapper(IO_name,IO_type,IO_depth)
        
        # self.Update_all_list()
        pass

    def destDisconnect__onBtnClick( self, event ):
        sel_num_lt = self.m_listBox__dest.GetSelections()
        for sel_num in sel_num_lt:
            dest_obj = self.core.dest_lt[sel_num]
            self.core.RemoveLinkPoint(dest_obj)
            self.Update_all_list()
    
    
    def menu_addPoint__onMenuSel( self, event ):
        self.createPointDialog.Show()

class VerilogCodeFrame ( wx_gui.verilogCodeFrame.VerilogCodeFrame ):	
    def __init__( self, parent , core):
        super(VerilogCodeFrame,self).__init__(parent)
        self.core = core
        self.update_cnt = 0
    
    def VerilogCodeFrame__onAct( self, event ):
        pass
        if (self.core.proc_wrapper!=None):
            self.m_richText__showGen.SetValue(self.core.GenerateVerilogCode())

    def genFile__onBtnClick( self, event ):
        file_dir = self.m_dirPicker1.GetPath()
        file_name = self.m_textCtrl__fileName.GetValue()

        if ((file_dir != '')&(file_name != '')):
            f_fp = file_dir+'\\'+file_name+'.v'
            fp = open(f_fp,'w+')
            fp.write (self.m_richText__showGen.GetValue())
            fp.close ()

            wx.MessageBox('Generate file success!\nFile: %s'%(f_fp), 'Info', wx.OK | wx.ICON_INFORMATION)

def main():
    app=wx.App()
    mainFrame=MainFrame(None)
    mainFrame.Show()
    # moduleManagerFrame.Show()
    app.MainLoop()


main()