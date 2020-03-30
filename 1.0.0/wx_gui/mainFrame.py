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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1096,684 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer68 = wx.BoxSizer( wx.VERTICAL )

		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Source port" ), wx.VERTICAL )

		sbSizer9 = wx.StaticBoxSizer( wx.StaticBox( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Configuration" ), wx.VERTICAL )

		m_comboBox__src_inst_filterChoices = []
		self.m_comboBox__src_inst_filter = wx.ComboBox( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox__src_inst_filterChoices, 0 )
		sbSizer9.Add( self.m_comboBox__src_inst_filter, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer2.Add( sbSizer9, 0, wx.EXPAND, 5 )

		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Pins" ), wx.VERTICAL )

		m_listBox__srcChoices = []
		self.m_listBox__src = wx.ListBox( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox__srcChoices, wx.LB_HSCROLL )
		sbSizer5.Add( self.m_listBox__src, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		sbSizer2.Add( sbSizer5, 1, wx.EXPAND, 5 )

		sbSizer44 = wx.StaticBoxSizer( wx.StaticBox( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Detials" ), wx.VERTICAL )

		self.m_notebook7 = wx.Notebook( sbSizer44.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_BOTTOM )
		self.m_notebook7.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.m_panel3 = wx.Panel( self.m_notebook7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer70 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl__src_info = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_DONTWRAP|wx.TE_MULTILINE )
		self.m_textCtrl__src_info.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer70.Add( self.m_textCtrl__src_info, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel3.SetSizer( bSizer70 )
		self.m_panel3.Layout()
		bSizer70.Fit( self.m_panel3 )
		self.m_notebook7.AddPage( self.m_panel3, u"Information", True )
		self.m_panel4 = wx.Panel( self.m_notebook7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer71 = wx.BoxSizer( wx.VERTICAL )

		m_listBox__src_linkToChoices = []
		self.m_listBox__src_linkTo = wx.ListBox( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox__src_linkToChoices, 0 )
		bSizer71.Add( self.m_listBox__src_linkTo, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel4.SetSizer( bSizer71 )
		self.m_panel4.Layout()
		bSizer71.Fit( self.m_panel4 )
		self.m_notebook7.AddPage( self.m_panel4, u"Link to", False )

		sbSizer44.Add( self.m_notebook7, 1, wx.EXPAND |wx.ALL, 5 )


		sbSizer2.Add( sbSizer44, 1, wx.EXPAND, 5 )

		self.m_button__output_tracer = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Tracer link", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2.Add( self.m_button__output_tracer, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer19.Add( sbSizer2, 1, wx.EXPAND, 5 )

		self.m_button__connect = wx.Button( self, wx.ID_ANY, u"Link\n>--->", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button__connect.SetMaxSize( wx.Size( 60,-1 ) )

		bSizer19.Add( self.m_button__connect, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

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

		sbSizer441 = wx.StaticBoxSizer( wx.StaticBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Detials" ), wx.VERTICAL )

		self.m_notebook71 = wx.Notebook( sbSizer441.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_BOTTOM )
		self.m_notebook71.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.m_panel31 = wx.Panel( self.m_notebook71, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer701 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl__dest_info = wx.TextCtrl( self.m_panel31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_DONTWRAP|wx.TE_MULTILINE )
		bSizer701.Add( self.m_textCtrl__dest_info, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel31.SetSizer( bSizer701 )
		self.m_panel31.Layout()
		bSizer701.Fit( self.m_panel31 )
		self.m_notebook71.AddPage( self.m_panel31, u"Information", False )

		sbSizer441.Add( self.m_notebook71, 1, wx.EXPAND |wx.ALL, 5 )


		sbSizer4.Add( sbSizer441, 1, wx.EXPAND, 5 )

		self.m_button__destDisconnect = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Disconnect", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.m_button__destDisconnect, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer19.Add( sbSizer4, 1, wx.EXPAND, 5 )


		bSizer68.Add( bSizer19, 1, wx.EXPAND, 5 )


		bSizer2.Add( bSizer68, 1, wx.EXPAND, 5 )


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

		self.m_menu5 = wx.Menu()
		self.m_menuItem4 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"point", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.Append( self.m_menuItem4 )

		self.m_menubar1.Append( self.m_menu5, u"Add" )

		self.m_menu4 = wx.Menu()
		self.m_menuItem__multSel = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"Destination multiple selection", wx.EmptyString, wx.ITEM_CHECK )
		self.m_menu4.Append( self.m_menuItem__multSel )

		self.m_menuItem__autoNext = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"Auto select to next after link", wx.EmptyString, wx.ITEM_CHECK )
		self.m_menu4.Append( self.m_menuItem__autoNext )
		self.m_menuItem__autoNext.Check( True )

		self.m_menubar1.Append( self.m_menu4, u"Mode" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.mainFrame__onAct )
		self.m_listBox__src.Bind( wx.EVT_LISTBOX, self.src__onListBox )
		self.m_button__connect.Bind( wx.EVT_BUTTON, self.connect__onBtnClick )
		self.m_listBox__dest.Bind( wx.EVT_LISTBOX, self.dest__onListBox )
		self.m_button__destDisconnect.Bind( wx.EVT_BUTTON, self.destDisconnect__onBtnClick )
		self.Bind( wx.EVT_MENU, self.menu_moduleManager__onMenuSel, id = self.m_menuItem11.GetId() )
		self.Bind( wx.EVT_MENU, self.menu_addPoint__onMenuSel, id = self.m_menuItem4.GetId() )
		self.Bind( wx.EVT_MENU, self.menu_addPoint__destMultSel, id = self.m_menuItem__multSel.GetId() )
		self.Bind( wx.EVT_MENU, self.menu_addPoint__autoSel, id = self.m_menuItem__autoNext.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def mainFrame__onAct( self, event ):
		event.Skip()

	def src__onListBox( self, event ):
		event.Skip()

	def connect__onBtnClick( self, event ):
		event.Skip()

	def dest__onListBox( self, event ):
		event.Skip()

	def destDisconnect__onBtnClick( self, event ):
		event.Skip()

	def menu_moduleManager__onMenuSel( self, event ):
		event.Skip()

	def menu_addPoint__onMenuSel( self, event ):
		event.Skip()

	def menu_addPoint__destMultSel( self, event ):
		event.Skip()

	def menu_addPoint__autoSel( self, event ):
		event.Skip()


