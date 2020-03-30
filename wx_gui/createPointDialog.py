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

		m_choice__create_point_typeChoices = [ u"input", u"output", u"inout", u"wire" ]
		self.m_choice__create_point_type = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice__create_point_typeChoices, 0 )
		self.m_choice__create_point_type.SetSelection( 0 )
		fgSizer4.Add( self.m_choice__create_point_type, 0, wx.ALL, 5 )

		self.m_textCtrl__point_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl__point_name.SetMinSize( wx.Size( 300,-1 ) )

		fgSizer4.Add( self.m_textCtrl__point_name, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText144 = wx.StaticText( self, wx.ID_ANY, u"Bit width", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText144.Wrap( -1 )

		fgSizer4.Add( self.m_staticText144, 0, wx.ALL, 5 )

		self.m_textCtrl__point_bit = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl__point_bit.SetMinSize( wx.Size( 300,-1 ) )

		fgSizer4.Add( self.m_textCtrl__point_bit, 1, wx.ALL, 5 )

		self.m_staticText140 = wx.StaticText( self, wx.ID_ANY, u"Wire assign code", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText140.Wrap( -1 )

		fgSizer4.Add( self.m_staticText140, 0, wx.ALL, 5 )

		self.m_textCtrl__wire_assign_code = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl__wire_assign_code.Enable( False )
		self.m_textCtrl__wire_assign_code.SetMinSize( wx.Size( 300,-1 ) )

		fgSizer4.Add( self.m_textCtrl__wire_assign_code, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer44.Add( fgSizer4, 1, wx.EXPAND, 5 )

		self.m_staticline8 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer44.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer45 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Point info.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer45.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.m_staticText__pointInfo = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText__pointInfo.Wrap( -1 )

		bSizer45.Add( self.m_staticText__pointInfo, 0, wx.ALL, 5 )


		bSizer44.Add( bSizer45, 0, wx.EXPAND, 5 )

		self.m_button__create_point = wx.Button( self, wx.ID_ANY, u"Create wire/IO to wrapper", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer44.Add( self.m_button__create_point, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer44 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_choice__create_point_type.Bind( wx.EVT_CHOICE, self.point_type__onChoice )
		self.m_textCtrl__point_name.Bind( wx.EVT_TEXT, self.point_name__onText )
		self.m_textCtrl__point_bit.Bind( wx.EVT_TEXT, self.point_bit__onText )
		self.m_textCtrl__wire_assign_code.Bind( wx.EVT_TEXT, self.wire_assign_code__onText )
		self.m_button__create_point.Bind( wx.EVT_BUTTON, self.create_point__onBtnClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def point_type__onChoice( self, event ):
		event.Skip()

	def point_name__onText( self, event ):
		event.Skip()

	def point_bit__onText( self, event ):
		event.Skip()

	def wire_assign_code__onText( self, event ):
		event.Skip()

	def create_point__onBtnClick( self, event ):
		event.Skip()


