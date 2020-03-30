# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class ModuleManagerFrame
###########################################################################

class ModuleManagerFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 974,760 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer23 = wx.BoxSizer( wx.VERTICAL )

		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_filePicker__loadFile = wx.FilePickerCtrl( self, wx.ID_ANY, u"D:\\dev\\py3\\verilog_IO_linker\\1.0.0\\wx_gui\\noname.h", u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer24.Add( self.m_filePicker__loadFile, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer23.Add( bSizer24, 0, wx.EXPAND, 5 )

		self.m_staticline5 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer23.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer241 = wx.BoxSizer( wx.HORIZONTAL )

		sbSizer10 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Module list" ), wx.VERTICAL )

		m_listBox__parser_moduleChoices = []
		self.m_listBox__parser_module = wx.ListBox( sbSizer10.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox__parser_moduleChoices, 0 )
		sbSizer10.Add( self.m_listBox__parser_module, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer241.Add( sbSizer10, 1, wx.EXPAND, 5 )

		sbSizer13 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Configuration" ), wx.VERTICAL )

		bSizer28 = wx.BoxSizer( wx.VERTICAL )


		bSizer28.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText39 = wx.StaticText( sbSizer13.GetStaticBox(), wx.ID_ANY, u"Instance name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )

		bSizer28.Add( self.m_staticText39, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl__inst_name = wx.TextCtrl( sbSizer13.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.m_textCtrl__inst_name, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_button__inst = wx.Button( sbSizer13.GetStaticBox(), wx.ID_ANY, u"Instance", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.m_button__inst, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticline3 = wx.StaticLine( sbSizer13.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer28.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer28.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button__set_wrapper = wx.Button( sbSizer13.GetStaticBox(), wx.ID_ANY, u"Set wrapper", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.m_button__set_wrapper, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticline81 = wx.StaticLine( sbSizer13.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer28.Add( self.m_staticline81, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button__createNewWrapper = wx.Button( sbSizer13.GetStaticBox(), wx.ID_ANY, u"Create new wrapper", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer26.Add( self.m_button__createNewWrapper, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl__createNewWrapper = wx.TextCtrl( sbSizer13.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer26.Add( self.m_textCtrl__createNewWrapper, 1, wx.ALL, 5 )


		bSizer28.Add( bSizer26, 1, wx.EXPAND, 5 )


		sbSizer13.Add( bSizer28, 1, wx.EXPAND, 5 )


		bSizer241.Add( sbSizer13, 1, wx.EXPAND, 5 )

		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Instance list" ), wx.VERTICAL )

		m_listBox__instChoices = []
		self.m_listBox__inst = wx.ListBox( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox__instChoices, 0 )
		sbSizer11.Add( self.m_listBox__inst, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer241.Add( sbSizer11, 1, wx.EXPAND, 5 )


		bSizer23.Add( bSizer241, 1, wx.EXPAND, 5 )

		self.m_staticline51 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer23.Add( self.m_staticline51, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )

		sbSizer12 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Instance parameters" ), wx.VERTICAL )

		m_listBox__override_paramChoices = []
		self.m_listBox__override_param = wx.ListBox( sbSizer12.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox__override_paramChoices, 0 )
		sbSizer12.Add( self.m_listBox__override_param, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button12 = wx.Button( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Clear override", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer12.Add( self.m_button12, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button__overrideParamByConst = wx.Button( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Set constant", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer25.Add( self.m_button__overrideParamByConst, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl__setInstParamByConst = wx.TextCtrl( sbSizer12.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer25.Add( self.m_textCtrl__setInstParamByConst, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		sbSizer12.Add( bSizer25, 0, wx.EXPAND, 5 )


		bSizer30.Add( sbSizer12, 1, wx.EXPAND, 5 )

		bSizer32 = wx.BoxSizer( wx.VERTICAL )


		bSizer32.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button__param_mapping = wx.Button( self, wx.ID_ANY, u"<<-- Override --<", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.m_button__param_mapping, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer32.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer30.Add( bSizer32, 1, wx.EXPAND, 5 )

		sbSizer131 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Wrapper parameters" ), wx.VERTICAL )

		m_listBox__wrapper_paramChoices = []
		self.m_listBox__wrapper_param = wx.ListBox( sbSizer131.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox__wrapper_paramChoices, 0 )
		sbSizer131.Add( self.m_listBox__wrapper_param, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button__createNewParam = wx.Button( sbSizer131.GetStaticBox(), wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer34.Add( self.m_button__createNewParam, 1, wx.ALL, 5 )

		self.m_button__del_wrapper_param = wx.Button( sbSizer131.GetStaticBox(), wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer34.Add( self.m_button__del_wrapper_param, 1, wx.ALL, 5 )


		sbSizer131.Add( bSizer34, 0, wx.EXPAND, 5 )

		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText19 = wx.StaticText( sbSizer131.GetStaticBox(), wx.ID_ANY, u"name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		bSizer21.Add( self.m_staticText19, 0, wx.ALL, 5 )

		self.m_staticText20 = wx.StaticText( sbSizer131.GetStaticBox(), wx.ID_ANY, u"value", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		bSizer21.Add( self.m_staticText20, 0, wx.ALL, 5 )


		bSizer20.Add( bSizer21, 0, wx.EXPAND, 5 )

		bSizer211 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl__newParam_name = wx.TextCtrl( sbSizer131.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer211.Add( self.m_textCtrl__newParam_name, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl_newParam_value = wx.TextCtrl( sbSizer131.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer211.Add( self.m_textCtrl_newParam_value, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer20.Add( bSizer211, 1, wx.EXPAND, 5 )


		sbSizer131.Add( bSizer20, 0, wx.EXPAND, 5 )


		bSizer30.Add( sbSizer131, 1, wx.EXPAND, 5 )


		bSizer23.Add( bSizer30, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer23 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_filePicker__loadFile.Bind( wx.EVT_FILEPICKER_CHANGED, self.filePicker__onFileChanged )
		self.m_listBox__parser_module.Bind( wx.EVT_LISTBOX, self.parser_module__onListBox )
		self.m_button__inst.Bind( wx.EVT_BUTTON, self.inst__onButtonClick )
		self.m_button__set_wrapper.Bind( wx.EVT_BUTTON, self.loadAsWrapper__onBtnClick )
		self.m_button__createNewWrapper.Bind( wx.EVT_BUTTON, self.createNewWrapper__onBtnClick )
		self.m_listBox__inst.Bind( wx.EVT_LISTBOX, self.inst__onListBox )
		self.m_button12.Bind( wx.EVT_BUTTON, self.clearInstParamOverride__onBtnClick )
		self.m_button__overrideParamByConst.Bind( wx.EVT_BUTTON, self.overrideParamByConst__onBtnClick )
		self.m_button__param_mapping.Bind( wx.EVT_BUTTON, self.mapping__onBtnClick )
		self.m_button__createNewParam.Bind( wx.EVT_BUTTON, self.createNewParam__onBtnClick )
		self.m_button__del_wrapper_param.Bind( wx.EVT_BUTTON, self.delWrapParam__onBtnClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def filePicker__onFileChanged( self, event ):
		event.Skip()

	def parser_module__onListBox( self, event ):
		event.Skip()

	def inst__onButtonClick( self, event ):
		event.Skip()

	def loadAsWrapper__onBtnClick( self, event ):
		event.Skip()

	def createNewWrapper__onBtnClick( self, event ):
		event.Skip()

	def inst__onListBox( self, event ):
		event.Skip()

	def clearInstParamOverride__onBtnClick( self, event ):
		event.Skip()

	def overrideParamByConst__onBtnClick( self, event ):
		event.Skip()

	def mapping__onBtnClick( self, event ):
		event.Skip()

	def createNewParam__onBtnClick( self, event ):
		event.Skip()

	def delWrapParam__onBtnClick( self, event ):
		event.Skip()


