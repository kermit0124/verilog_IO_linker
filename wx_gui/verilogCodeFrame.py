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
## Class VerilogCodeFrame
###########################################################################

class VerilogCodeFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Verilog Code Generator", pos = wx.DefaultPosition, size = wx.Size( 909,669 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		sbSizer16 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Generate code" ), wx.VERTICAL )

		self.m_richText__showGen = wx.richtext.RichTextCtrl( sbSizer16.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		self.m_richText__showGen.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		sbSizer16.Add( self.m_richText__showGen, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer15.Add( sbSizer16, 1, wx.EXPAND, 5 )

		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )

		sbSizer14 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"File directory" ), wx.VERTICAL )

		self.m_dirPicker1 = wx.DirPickerCtrl( sbSizer14.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		sbSizer14.Add( self.m_dirPicker1, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer26.Add( sbSizer14, 1, wx.EXPAND, 5 )

		sbSizer15 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"File name(.v)" ), wx.VERTICAL )

		bSizer27 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl__fileName = wx.TextCtrl( sbSizer15.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl__fileName.SetMinSize( wx.Size( 150,-1 ) )

		bSizer27.Add( self.m_textCtrl__fileName, 0, wx.ALL, 5 )

		self.m_button__genFile = wx.Button( sbSizer15.GetStaticBox(), wx.ID_ANY, u"Generate file", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.m_button__genFile, 0, wx.ALL, 5 )


		sbSizer15.Add( bSizer27, 1, wx.EXPAND, 5 )


		bSizer26.Add( sbSizer15, 0, wx.EXPAND, 5 )


		bSizer15.Add( bSizer26, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer15 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.VerilogCodeFrame__onAct )
		self.Bind( wx.EVT_CLOSE, self.VerilogCodeFrame__onClose )
		self.m_button__genFile.Bind( wx.EVT_BUTTON, self.genFile__onBtnClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def VerilogCodeFrame__onAct( self, event ):
		event.Skip()

	def VerilogCodeFrame__onClose( self, event ):
		event.Skip()

	def genFile__onBtnClick( self, event ):
		event.Skip()


