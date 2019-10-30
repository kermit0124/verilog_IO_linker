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
## Class Frame1
###########################################################################

class Frame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"verilog IO linker", pos = wx.DefaultPosition, size = wx.Size( 1671,538 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Instance name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		gSizer5.Add( self.m_staticText15, 0, wx.ALL, 5 )

		self.m_textCtrl__instName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_textCtrl__instName, 0, wx.ALL, 5 )

		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Prefix", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		gSizer5.Add( self.m_staticText16, 0, wx.ALL, 5 )

		self.m_textCtrl__prefix = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_textCtrl__prefix, 0, wx.ALL, 5 )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Suffix", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		gSizer5.Add( self.m_staticText17, 0, wx.ALL, 5 )

		self.m_textCtrl__suffix = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_textCtrl__suffix, 0, wx.ALL, 5 )

		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Left comma mode", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		gSizer5.Add( self.m_staticText18, 0, wx.ALL, 5 )

		m_choice__left_commaChoices = [ u"false", u"true" ]
		self.m_choice__left_comma = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice__left_commaChoices, 0 )
		self.m_choice__left_comma.SetSelection( 0 )
		gSizer5.Add( self.m_choice__left_comma, 0, wx.ALL, 5 )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Module select", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		gSizer5.Add( self.m_staticText19, 0, wx.ALL, 5 )

		m_choice__modSelChoices = []
		self.m_choice__modSel = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice__modSelChoices, 0 )
		self.m_choice__modSel.SetSelection( 0 )
		gSizer5.Add( self.m_choice__modSel, 0, wx.ALL, 5 )

		self.m_button64 = wx.Button( self, wx.ID_ANY, u"Load source code", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button64.Enable( False )

		gSizer5.Add( self.m_button64, 0, wx.ALL, 5 )


		fgSizer3.Add( gSizer5, 1, wx.EXPAND, 5 )

		fgSizer5 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_richText__origSrc = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.ALWAYS_SHOW_SB|wx.HSCROLL|wx.VSCROLL )
		self.m_richText__origSrc.SetMinSize( wx.Size( 600,500 ) )

		fgSizer5.Add( self.m_richText__origSrc, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )


		bSizer7.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button70 = wx.Button( self, wx.ID_ANY, u"Generate\n>>>", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button70, 0, wx.ALL, 5 )


		bSizer7.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer5.Add( bSizer7, 1, wx.EXPAND, 5 )

		self.m_richText__genSrc = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.ALWAYS_SHOW_SB|wx.HSCROLL|wx.VSCROLL )
		self.m_richText__genSrc.SetMinSize( wx.Size( 600,500 ) )

		fgSizer5.Add( self.m_richText__genSrc, 1, wx.EXPAND |wx.ALL, 5 )


		fgSizer3.Add( fgSizer5, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_textCtrl__instName.Bind( wx.EVT_KEY_UP, self.OnKeyUp__instName )
		self.m_textCtrl__instName.Bind( wx.EVT_TEXT, self.onText__instName )
		self.m_richText__origSrc.Bind( wx.EVT_TEXT, self.rtxt_origSrc__onText )
		self.m_button70.Bind( wx.EVT_BUTTON, self.gen_code )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnKeyUp__instName( self, event ):
		event.Skip()

	def onText__instName( self, event ):
		event.Skip()

	def rtxt_origSrc__onText( self, event ):
		event.Skip()

	def gen_code( self, event ):
		event.Skip()


