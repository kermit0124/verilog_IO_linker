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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"verilog IO linker v0.0.0", pos = wx.DefaultPosition, size = wx.Size( 1346,677 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Module select", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		bSizer13.Add( self.m_staticText19, 0, wx.ALL, 5 )

		m_choice__modSelChoices = []
		self.m_choice__modSel = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice__modSelChoices, 0 )
		self.m_choice__modSel.SetSelection( 0 )
		self.m_choice__modSel.SetMinSize( wx.Size( 300,-1 ) )

		bSizer13.Add( self.m_choice__modSel, 0, wx.ALL, 5 )


		bSizer10.Add( bSizer13, 1, wx.EXPAND, 5 )

		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )

		gSizer4.SetMinSize( wx.Size( -1,400 ) )
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Instance name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		gSizer4.Add( self.m_staticText15, 0, wx.ALL, 5 )

		self.m_textCtrl__instName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_textCtrl__instName, 0, wx.ALL, 5 )

		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Prefix", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		gSizer4.Add( self.m_staticText16, 0, wx.ALL, 5 )

		self.m_textCtrl__prefix = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_textCtrl__prefix, 0, wx.ALL, 5 )

		self.m_staticText171 = wx.StaticText( self, wx.ID_ANY, u"Suffix", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText171.Wrap( -1 )

		gSizer4.Add( self.m_staticText171, 0, wx.ALL, 5 )

		self.m_textCtrl__suffix = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_textCtrl__suffix, 0, wx.ALL, 5 )

		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Left comma mode", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		gSizer4.Add( self.m_staticText18, 0, wx.ALL, 5 )

		m_choice__left_commaChoices = [ u"false", u"true" ]
		self.m_choice__left_comma = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice__left_commaChoices, 0 )
		self.m_choice__left_comma.SetSelection( 0 )
		gSizer4.Add( self.m_choice__left_comma, 0, wx.ALL, 5 )


		bSizer10.Add( gSizer4, 1, wx.EXPAND, 5 )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		self.m_button64 = wx.Button( self, wx.ID_ANY, u"Load source code", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button64.Enable( False )

		bSizer15.Add( self.m_button64, 0, wx.ALL, 5 )


		bSizer10.Add( bSizer15, 1, wx.EXPAND, 5 )


		bSizer8.Add( bSizer10, 1, wx.EXPAND, 5 )


		bSizer7.Add( bSizer8, 1, wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_richText__origSrc = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.ALWAYS_SHOW_SB|wx.HSCROLL|wx.VSCROLL )
		self.m_richText__origSrc.SetMinSize( wx.Size( 450,500 ) )

		bSizer9.Add( self.m_richText__origSrc, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )


		bSizer16.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button__genCode = wx.Button( self, wx.ID_ANY, u"Generate\n>>>", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_button__genCode, 0, wx.ALL, 5 )


		bSizer16.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer9.Add( bSizer16, 1, wx.EXPAND, 5 )

		self.m_richText__genSrc = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.ALWAYS_SHOW_SB|wx.HSCROLL|wx.VSCROLL )
		self.m_richText__genSrc.SetMinSize( wx.Size( 450,500 ) )

		bSizer9.Add( self.m_richText__genSrc, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer7.Add( bSizer9, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_choice__modSel.Bind( wx.EVT_KEY_UP, self.OnKeyUp__all_txtCtrl )
		self.m_textCtrl__instName.Bind( wx.EVT_KEY_UP, self.OnKeyUp__all_txtCtrl )
		self.m_textCtrl__instName.Bind( wx.EVT_TEXT, self.onText__instName )
		self.m_textCtrl__prefix.Bind( wx.EVT_KEY_UP, self.OnKeyUp__all_txtCtrl )
		self.m_textCtrl__suffix.Bind( wx.EVT_KEY_UP, self.OnKeyUp__all_txtCtrl )
		self.m_choice__left_comma.Bind( wx.EVT_KEY_UP, self.OnKeyUp__all_txtCtrl )
		self.m_richText__origSrc.Bind( wx.EVT_TEXT, self.rtxt_origSrc__onText )
		self.m_button__genCode.Bind( wx.EVT_BUTTON, self.gen_code )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnKeyUp__all_txtCtrl( self, event ):
		event.Skip()


	def onText__instName( self, event ):
		event.Skip()




	def rtxt_origSrc__onText( self, event ):
		event.Skip()

	def gen_code( self, event ):
		event.Skip()


