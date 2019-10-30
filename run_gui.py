
import wx.xrc
import wxGUI_layout
import verilog_IO_linker
	
#import the newly created GUI file 
class MainFrame(wxGUI_layout.Frame1): 
	t=[]
	def __init__(self,parent): 
		wxGUI_layout.Frame1.__init__(self,parent)  

	# def onText__instName( self, event ):
	# def OnKeyDown__instName( self, event ):		
		# pass
		# if (event.key()=='t'):
		# 	print ("ttt")
	# def OnKeyUp__instName( self, event ):
		# if (event.KeyCode==9):
		# 	self.m_textCtrl__prefix.SetFocus()

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