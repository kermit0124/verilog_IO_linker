
import wx.xrc
import wxGUI_layout
import verilog_IO_linker
	
#import the newly created GUI file 
class MainFrame(wxGUI_layout.Frame1): 
	def __init__(self,parent): 
		wxGUI_layout.Frame1.__init__(self,parent)  
		self.tab_focus_list = []
		self.tab_focus_list.append (self.m_textCtrl__instName)
		self.tab_focus_list.append (self.m_textCtrl__prefix)
		self.tab_focus_list.append (self.m_textCtrl__suffix)
		self.tab_focus_list.append (self.m_choice__left_comma)
		self.tab_focus_list.append (self.m_choice__modSel)

	def OnKeyUp__all_txtCtrl( self, event ):
		if (event.KeyCode==9):
			for idx,obj in enumerate(self.tab_focus_list):
				if (obj==event.EventObject):
					idx += 1
					idx %= len(self.tab_focus_list)
					self.tab_focus_list[idx].SetFocus()
					break

	def rtxt_origSrc__onText( self , event ):
		self.m_textCtrl__prefix
		VIOL.reparse_txt(self.m_richText__origSrc.Value)
		module_select_list_txt = VIOL.get_module_name_list()
		self.m_choice__modSel.Clear()
		for modName in module_select_list_txt:
			self.m_choice__modSel.Append(modName)
		self.m_choice__modSel.Select(0)
	
	def gen_code( self, event ):

		# print (self.m_choice__modSel.GetSelection())
		VIOL.select_modulde(self.m_choice__modSel.GetSelection())
		VIOL.comma_left = self.m_choice__left_comma.GetSelection()
		VIOL.link_prefix = self.m_textCtrl__prefix.Value
		VIOL.link_suffix = self.m_textCtrl__suffix.Value
		VIOL.link_inst_name = self.m_textCtrl__instName.Value


		txt_list = VIOL.gen_code()
		all_txt = ''
		for txt in txt_list:
			all_txt += txt
		self.m_richText__genSrc.Value = all_txt

VIOL = verilog_IO_linker.class__verilog_IO_linker('')
app = wx.App(False) 
frame = MainFrame(None) 
frame.Show(True) 
#start the applications 
app.MainLoop()  