import wx
import wx.xrc
import sys



class MyFrame2(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(700, 450),
                          style=wx.DEFAULT_FRAME_STYLE | wx.ALWAYS_SHOW_SB | wx.CLIP_CHILDREN | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        self.panel = wx.Panel(self)
        "变压器型号"
        self.statictext_2 = wx.StaticText(self.panel, label="变压器型号:", pos=(30, 50))
        self.statictext_2.Wrap(-1)
        self.statictext_2.SetFont(wx.Font(12, 70, 90, 90, False, "宋体"))
        self.textctrl_1 = wx.TextCtrl(self.panel, id=wx.ID_ANY, value="12", pos=(140, 45), size=(40, 30))
        self.textctrl_1.SetFont(wx.Font(12, 70, 90, 90, False, "宋体"))
        "中心点坐标"
        self.statictext_3 = wx.StaticText(self.panel, label="中心点坐标:", pos=(30, 120))
        self.statictext_3.Wrap(-1)
        self.statictext_3.SetFont(wx.Font(12, 70, 90, 90, False, "宋体"))
        self.textctrl_2 = wx.TextCtrl(self.panel, id=wx.ID_ANY, value="12", pos=(140, 115), size=(100, 30))
        self.textctrl_2.SetFont(wx.Font(12, 70, 90, 90, False, "宋体"))
        "旋转角度"
        self.statictext_4 = wx.StaticText(self.panel, label="旋转角度:", pos=(30, 200))
        self.statictext_4.Wrap(-1)
        self.statictext_4.SetFont(wx.Font(12, 70, 90, 90, False, "宋体"))
        self.textctrl_3 = wx.TextCtrl(self.panel, id=wx.ID_ANY, value="12", pos=(140, 195), size=(50, 30))
        self.textctrl_3.SetFont(wx.Font(12, 70, 90, 90, False, "宋体"))
        self.statictext_6 = wx.StaticText(self.panel, label="度", pos=(200, 200))
        self.statictext_6.Wrap(-1)
        self.statictext_6.SetFont(wx.Font(12, 70, 90, 90, False, "宋体"))
        "角点坐标"
        self.statictext_5 = wx.StaticText(self.panel, label="夹爪张开距离:", pos=(30, 280))
        self.statictext_5.Wrap(-1)
        self.statictext_5.SetFont(wx.Font(12, 70, 90, 90, False, "宋体"))
        self.textctrl_4 = wx.TextCtrl(self.panel, id=wx.ID_ANY, value="12", pos=(140, 275), size=(50, 30))
        self.textctrl_4.SetFont(wx.Font(12, 70, 90, 90, False, "宋体"))
        "按钮"
        self.button = wx.Button(self.panel, id=wx.ID_ANY, label="更换图片", pos=(60, 340), size=(150, 40))
        self.button.SetFont(wx.Font(16, 70, 90, 90, False, "宋体"))
        self.button.Bind(wx.EVT_BUTTON, self.btn_begin)
        "图片"
        self.statictext_7 = wx.StaticText(self.panel, label="图片", pos=(460, 20))
        self.statictext_7.Wrap(-1)
        self.statictext_7.SetFont(wx.Font(16, 70, 90, 90, False, "宋体"))
        self.staticbitmap = wx.StaticBitmap(self.panel, id=wx.ID_ANY,
                                            bitmap=wx.Bitmap(r"F:\毕设\实验\图像分类与检测\GUI\01.jpg", wx.BITMAP_TYPE_ANY),
                                            pos=(270, 50), size=(400, 350))

    def __del__(self):
        pass

    def btn_begin(self, event):
        self.Close()
        window2 = MyFrame1()
        window2.Show()


