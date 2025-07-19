# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,359 ), style = wx.DEFAULT_FRAME_STYLE|wx.ALWAYS_SHOW_SB|wx.CLIP_CHILDREN|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer2.AddSpacer( ( 0, 30), 1, wx.ALIGN_CENTER, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"用户登录", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 18, 75, 90, 92, False, "隶书" ) )
		
		bSizer2.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.ALIGN_CENTER, 5 )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer3.AddSpacer( ( 0, 0), 1, 0, 5 )
		
		
		bSizer1.Add( bSizer3, 1, 0, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer4.AddSpacer( ( 0, 0), 1, 0, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"账号", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		self.m_staticText4.SetFont( wx.Font( 14, 70, 90, 92, False, "宋体" ) )
		
		bSizer4.Add( self.m_staticText4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer4.AddSpacer( ( 0, 0), 1, 0, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl1.SetFont( wx.Font( 12, 70, 90, 90, False, "宋体" ) )
		
		bSizer4.Add( self.m_textCtrl1, 0, wx.ALL, 5 )
		
		
		bSizer4.AddSpacer( ( 0, 0), 1, 0, 5 )
		
		
		bSizer1.Add( bSizer4, 1, 0, 5 )
		
		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer41.AddSpacer( ( 0, 0), 1, 0, 5 )
		
		self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, u"密码", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )
		self.m_staticText41.SetFont( wx.Font( 14, 70, 90, 92, False, "宋体" ) )
		
		bSizer41.Add( self.m_staticText41, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer41.AddSpacer( ( 0, 0), 1, 0, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		self.m_textCtrl2.SetFont( wx.Font( 12, 70, 90, 90, False, "宋体" ) )
		
		bSizer41.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
		
		
		bSizer41.AddSpacer( ( 0, 0), 1, 0, 5 )
		
		
		bSizer1.Add( bSizer41, 1, 0, 5 )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer9.AddSpacer( ( 0, 10), 1, 0, 5 )
		
		
		bSizer1.Add( bSizer9, 1, 0, 5 )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"登录", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button1.SetFont( wx.Font( 14, 70, 90, 92, False, "宋体" ) )
		
		bSizer8.Add( self.m_button1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer8, 1, 0, 5 )
		
		bSizer91 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer91.AddSpacer( ( 0, 10), 1, 0, 5 )
		
		
		bSizer1.Add( bSizer91, 1, 0, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.btn_begin )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btn_begin( self, event ):
		event.Skip()
	

###########################################################################
## Class MyFrame3
###########################################################################

class MyFrame3 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.Colour( 0, 128, 255 ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../传统检测/digital_img-main/01.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_bitmap1, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer9 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

