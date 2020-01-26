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
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 983,624 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Source port" ), wx.VERTICAL )

		sbSizer9 = wx.StaticBoxSizer( wx.StaticBox( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Configuration" ), wx.VERTICAL )

		m_comboBox__src_inst_filterChoices = []
		self.m_comboBox__src_inst_filter = wx.ComboBox( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox__src_inst_filterChoices, 0 )
		sbSizer9.Add( self.m_comboBox__src_inst_filter, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer2.Add( sbSizer9, 0, wx.EXPAND, 5 )

		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Pins" ), wx.VERTICAL )

		m_listBox__srcChoices = []
		self.m_listBox__src = wx.ListBox( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox__srcChoices, wx.LB_HSCROLL|wx.LB_MULTIPLE )
		sbSizer5.Add( self.m_listBox__src, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		sbSizer2.Add( sbSizer5, 1, wx.EXPAND, 5 )

		self.m_button__output_tracer = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Tracer link", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2.Add( self.m_button__output_tracer, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer19.Add( sbSizer2, 1, wx.EXPAND, 5 )

		bSizer22 = wx.BoxSizer( wx.VERTICAL )


		bSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button__connect = wx.Button( self, wx.ID_ANY, u">> Connect >>", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.m_button__connect, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticline5 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer22.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )

		sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Modify assign mode" ), wx.VERTICAL )

		self.m_staticText7 = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Wire name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		sbSizer8.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.m_textCtrl__agnModeName = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer8.Add( self.m_textCtrl__agnModeName, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText6 = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Assign segment", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		sbSizer8.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.m_textCtrl__agnModeSeg = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer8.Add( self.m_textCtrl__agnModeSeg, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_staticText5 = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Verilog:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		sbSizer8.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button__assign = wx.Button( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Assign", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer8.Add( self.m_button__assign, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticline6 = wx.StaticLine( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer8.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_textCtrl__createWireName = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer8.Add( self.m_textCtrl__createWireName, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_textCtrl__createWireSeg = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer8.Add( self.m_textCtrl__createWireSeg, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_button__createWire = wx.Button( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Create wire", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer8.Add( self.m_button__createWire, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer22.Add( sbSizer8, 1, wx.EXPAND, 5 )


		bSizer22.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer19.Add( bSizer22, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Destination port" ), wx.VERTICAL )

		sbSizer10 = wx.StaticBoxSizer( wx.StaticBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Configuration" ), wx.HORIZONTAL )

		m_comboBox__dest_inst_filterChoices = []
		self.m_comboBox__dest_inst_filter = wx.ComboBox( sbSizer10.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox__dest_inst_filterChoices, 0 )
		sbSizer10.Add( self.m_comboBox__dest_inst_filter, 1, wx.ALL, 5 )

		self.m_checkBox7 = wx.CheckBox( sbSizer10.GetStaticBox(), wx.ID_ANY, u"Ignore assigned pin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox7.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_checkBox7.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		sbSizer10.Add( self.m_checkBox7, 0, wx.ALL, 5 )


		sbSizer4.Add( sbSizer10, 0, wx.EXPAND, 5 )

		sbSizer51 = wx.StaticBoxSizer( wx.StaticBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Pins" ), wx.VERTICAL )

		m_listBox__destChoices = []
		self.m_listBox__dest = wx.ListBox( sbSizer51.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox__destChoices, wx.LB_HSCROLL|wx.LB_MULTIPLE )
		sbSizer51.Add( self.m_listBox__dest, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		sbSizer4.Add( sbSizer51, 1, wx.EXPAND, 5 )

		self.m_button__disconnect_input = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Disconnect", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.m_button__disconnect_input, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer19.Add( sbSizer4, 1, wx.EXPAND, 5 )


		bSizer2.Add( bSizer19, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu2 = wx.Menu()
		self.m_menuItem11 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Module manager", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem11 )

		self.m_menubar1.Append( self.m_menu2, u"File" )

		self.m_menu21 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu21, wx.ID_ANY, u"Replace bit width by wrapper parameter", wx.EmptyString, wx.ITEM_CHECK )
		self.m_menu21.Append( self.m_menuItem1 )
		self.m_menuItem1.Enable( False )

		self.m_menubar1.Append( self.m_menu21, u"View" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.mainFrame__onAct )
		self.m_listBox__src.Bind( wx.EVT_LISTBOX, self.src__onListBox )
		self.m_button__connect.Bind( wx.EVT_BUTTON, self.connect__onBtnClick )
		self.m_button__assign.Bind( wx.EVT_BUTTON, self.assign__onBtnClick )
		self.m_button__createWire.Bind( wx.EVT_BUTTON, self.createWire__onBtnClick )
		self.m_listBox__dest.Bind( wx.EVT_LISTBOX, self.dest__onListBox )
		self.Bind( wx.EVT_MENU, self.menu_moduleManager__onMenuSel, id = self.m_menuItem11.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def mainFrame__onAct( self, event ):
		event.Skip()

	def src__onListBox( self, event ):
		event.Skip()

	def connect__onBtnClick( self, event ):
		event.Skip()

	def assign__onBtnClick( self, event ):
		event.Skip()

	def createWire__onBtnClick( self, event ):
		event.Skip()

	def dest__onListBox( self, event ):
		event.Skip()

	def menu_moduleManager__onMenuSel( self, event ):
		event.Skip()


