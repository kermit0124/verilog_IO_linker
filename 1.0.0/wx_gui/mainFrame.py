# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

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
		self.m_listBox__dest = wx.ListBox( sbSizer51.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox__destChoices, wx.LB_HSCROLL )
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
		self.m_menuItem41 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"Destination multiple selection", wx.EmptyString, wx.ITEM_CHECK )
		self.m_menu4.Append( self.m_menuItem41 )
		self.m_menuItem41.Check( True )

		self.m_menuItem5 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"Auto select to next after link", wx.EmptyString, wx.ITEM_CHECK )
		self.m_menu4.Append( self.m_menuItem5 )
		self.m_menuItem5.Check( True )

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
		self.Bind( wx.EVT_MENU, self.menu_addPoint__destMultSel, id = self.m_menuItem41.GetId() )
		self.Bind( wx.EVT_MENU, self.menu_addPoint__autoSel, id = self.m_menuItem5.GetId() )

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


###########################################################################
## Class CreatePointDialog
###########################################################################

class CreatePointDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Create point", pos = wx.DefaultPosition, size = wx.Size( 477,220 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer44 = wx.BoxSizer( wx.VERTICAL )

		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		m_choice__create_wireIO_typeChoices = [ u"input", u"output", u"inout", u"wire" ]
		self.m_choice__create_wireIO_type = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice__create_wireIO_typeChoices, 0 )
		self.m_choice__create_wireIO_type.SetSelection( 0 )
		fgSizer4.Add( self.m_choice__create_wireIO_type, 0, wx.ALL, 5 )

		self.m_textCtrl__createName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl__createName.SetMinSize( wx.Size( 300,-1 ) )

		fgSizer4.Add( self.m_textCtrl__createName, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText144 = wx.StaticText( self, wx.ID_ANY, u"Bit width", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText144.Wrap( -1 )

		fgSizer4.Add( self.m_staticText144, 0, wx.ALL, 5 )

		self.m_textCtrl__createBit = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl__createBit.SetMinSize( wx.Size( 300,-1 ) )

		fgSizer4.Add( self.m_textCtrl__createBit, 1, wx.ALL, 5 )

		self.m_staticText140 = wx.StaticText( self, wx.ID_ANY, u"Wire assign code", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText140.Wrap( -1 )

		fgSizer4.Add( self.m_staticText140, 0, wx.ALL, 5 )

		self.m_textCtrl__createWireSeg = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl__createWireSeg.SetMinSize( wx.Size( 300,-1 ) )

		fgSizer4.Add( self.m_textCtrl__createWireSeg, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer44.Add( fgSizer4, 1, wx.EXPAND, 5 )

		self.m_staticline8 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer44.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer45 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText44 = wx.StaticText( self, wx.ID_ANY, u"Point info.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )

		bSizer45.Add( self.m_staticText44, 0, wx.ALL, 5 )

		self.m_staticText__pointInfo = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText__pointInfo.Wrap( -1 )

		bSizer45.Add( self.m_staticText__pointInfo, 0, wx.ALL, 5 )


		bSizer44.Add( bSizer45, 0, wx.EXPAND, 5 )

		self.m_button__create_wireIO = wx.Button( self, wx.ID_ANY, u"Create wire/IO", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer44.Add( self.m_button__create_wireIO, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer44 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button__create_wireIO.Bind( wx.EVT_BUTTON, self.create_wireIO__onBtnClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def create_wireIO__onBtnClick( self, event ):
		event.Skip()


###########################################################################
## Class VerilogCodeFrame
###########################################################################

class VerilogCodeFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 909,669 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		self.m_richText__showGen = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		bSizer15.Add( self.m_richText__showGen, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer15 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.VerilogCodeFrame__onAct )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def VerilogCodeFrame__onAct( self, event ):
		event.Skip()


###########################################################################
## Class ModuleManagerFrame
###########################################################################

class ModuleManagerFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1250,765 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

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

		m_listBox__parser_moduleChoices = []
		self.m_listBox__parser_module = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox__parser_moduleChoices, 0 )
		bSizer241.Add( self.m_listBox__parser_module, 1, wx.ALL|wx.EXPAND, 5 )

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

		m_listBox__instChoices = []
		self.m_listBox__inst = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox__instChoices, 0 )
		bSizer241.Add( self.m_listBox__inst, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer23.Add( bSizer241, 1, wx.EXPAND, 5 )

		self.m_staticline51 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer23.Add( self.m_staticline51, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer31 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText411 = wx.StaticText( self, wx.ID_ANY, u"Overrider parameters", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText411.Wrap( -1 )

		bSizer31.Add( self.m_staticText411, 0, wx.ALL, 5 )

		m_listBox__override_paramChoices = []
		self.m_listBox__override_param = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox__override_paramChoices, 0 )
		bSizer31.Add( self.m_listBox__override_param, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer30.Add( bSizer31, 1, wx.EXPAND, 5 )

		bSizer32 = wx.BoxSizer( wx.VERTICAL )

		bSizer35 = wx.BoxSizer( wx.VERTICAL )


		bSizer35.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button__param_mapping = wx.Button( self, wx.ID_ANY, u"Mapping ->>", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer35.Add( self.m_button__param_mapping, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer35.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer36 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button__overrideParamByConst = wx.Button( self, wx.ID_ANY, u"<<- Set constant", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button__overrideParamByConst.Hide()

		bSizer36.Add( self.m_button__overrideParamByConst, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl3.Hide()

		bSizer36.Add( self.m_textCtrl3, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer35.Add( bSizer36, 1, wx.EXPAND, 5 )


		bSizer35.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer32.Add( bSizer35, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer30.Add( bSizer32, 1, wx.EXPAND, 5 )

		bSizer33 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText4111 = wx.StaticText( self, wx.ID_ANY, u"Wrapper parameters", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4111.Wrap( -1 )

		bSizer33.Add( self.m_staticText4111, 0, wx.ALL, 5 )

		m_listBox__wrapper_paramChoices = []
		self.m_listBox__wrapper_param = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox__wrapper_paramChoices, 0 )
		bSizer33.Add( self.m_listBox__wrapper_param, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button__createNewParam = wx.Button( self, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer34.Add( self.m_button__createNewParam, 1, wx.ALL, 5 )

		self.m_button__del_wrapper_param = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer34.Add( self.m_button__del_wrapper_param, 1, wx.ALL, 5 )


		bSizer33.Add( bSizer34, 0, wx.EXPAND, 5 )

		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		bSizer21.Add( self.m_staticText19, 0, wx.ALL, 5 )

		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"value", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		bSizer21.Add( self.m_staticText20, 0, wx.ALL, 5 )


		bSizer20.Add( bSizer21, 0, wx.EXPAND, 5 )

		bSizer211 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl__newParam_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer211.Add( self.m_textCtrl__newParam_name, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl_newParam_value = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer211.Add( self.m_textCtrl_newParam_value, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer20.Add( bSizer211, 1, wx.EXPAND, 5 )


		bSizer33.Add( bSizer20, 0, wx.EXPAND, 5 )


		bSizer30.Add( bSizer33, 1, wx.EXPAND, 5 )


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
		self.m_button__param_mapping.Bind( wx.EVT_BUTTON, self.mapping__onBtnClick )
		self.m_button__overrideParamByConst.Bind( wx.EVT_BUTTON, self.overrideParamByConst__onBtnClick )
		self.m_button__createNewParam.Bind( wx.EVT_BUTTON, self.createNewParam__onBtnClick )

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

	def mapping__onBtnClick( self, event ):
		event.Skip()

	def overrideParamByConst__onBtnClick( self, event ):
		event.Skip()

	def createNewParam__onBtnClick( self, event ):
		event.Skip()


