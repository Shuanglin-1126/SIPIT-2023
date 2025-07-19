import wx
import wx.xrc

# 自定义窗口类MyFrame
class MyFrame1(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="选择图片", size=(400, 400))
        self.Center()
        swindow = wx.SplitterWindow(parent=self, id=-1)
        top = wx.Panel(parent=swindow)
        bottom = wx.Panel(parent=swindow)
        # 设置左右布局的分割窗口left和right
        swindow.SplitHorizontally(top, bottom, 300)
        # 设置最小窗格大小，左右布局指左边窗口大小
        swindow.SetMinimumPaneSize(80)
        # 创建一棵树

        self.tree = self.CreateTreeCtrl(top)
        self.Bind(wx.EVT_TREE_SEL_CHANGING, self.on_click, self.tree)
        # 为left面板设置一个布局管理器
        vbox1 = wx.BoxSizer(wx.VERTICAL)
        top.SetSizer(vbox1)
        vbox1.Add(self.tree, 1, flag=wx.EXPAND | wx.ALL, border=5)
        # 为right面板设置一个布局管理器
        self.button = wx.Button(bottom, id=wx.ID_ANY, label="开始检测", pos=(105, 20), size=(150, 40))
        self.button.SetFont(wx.Font(16, 70, 90, 90, False, "宋体"))
        self.button.Bind(wx.EVT_BUTTON, self.btn_begin)

    def on_click(self, event):
        item = event.GetItem()
        self.st.SetLabel(self.tree.GetItemText(item))

    def CreateTreeCtrl(self, parent):
        tree = wx.TreeCtrl(parent)
        # 通过wx.ImageList()创建一个图像列表imglist并保存在树中
        imglist = wx.ImageList(16, 16, True, 2)
        imglist.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER, size=wx.Size(16, 16)))
        imglist.Add(wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, size=(16, 16)))
        tree.AssignImageList(imglist)
        # 创建根节点和单、多个变压器目录
        root = tree.AddRoot('变压器', image=0)
        item0 = tree.AppendItem(root, '相机', 1)
        item1 = tree.AppendItem(root, '1个变压器', 0)
        item2 = tree.AppendItem(root, '2个变压器', 0)
        item3 = tree.AppendItem(root, '3个变压器', 0)
        item4 = tree.AppendItem(root, '4个变压器', 0)
        tree.Expand(root)
        tree.SelectItem(item0)

        # 给item1节点添加5个子节点并展开
        tree.AppendItem(item1, '1', 1)
        tree.AppendItem(item1, '2', 1)
        tree.AppendItem(item1, '3', 1)
        tree.AppendItem(item1, '4', 1)
        tree.AppendItem(item1, '5', 1)
        tree.AppendItem(item1, '6', 1)
        tree.AppendItem(item1, '7', 1)
        tree.Expand(item1)

        # 给item2节点添加5个子节点并展开
        tree.AppendItem(item2, '1', 1)
        tree.AppendItem(item2, '2', 1)
        tree.AppendItem(item2, '3', 1)
        tree.AppendItem(item2, '4', 1)
        tree.AppendItem(item2, '5', 1)


        tree.AppendItem(item3, '1', 1)
        tree.AppendItem(item3, '2', 1)
        tree.AppendItem(item3, '3', 1)
        tree.AppendItem(item3, '4', 1)
        tree.AppendItem(item3, '5', 1)

        tree.AppendItem(item4, '1', 1)
        tree.AppendItem(item4, '2', 1)
        tree.AppendItem(item4, '3', 1)
        tree.AppendItem(item4, '4', 1)
        tree.AppendItem(item4, '5', 1)


        # 返回树对象
        return tree

    def btn_begin(self, event):
        self.Close()
        window2 = MyFrame2(None)
        window2.Show()

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
        self.textctrl_1 = wx.TextCtrl(self.panel, id=wx.ID_ANY, value="4", pos=(140, 45), size=(40, 30))
        self.textctrl_1.SetFont(wx.Font(12, 70, 90, 90, False, "宋体"))
        "中心点坐标"
        self.statictext_3 = wx.StaticText(self.panel, label="中心点坐标:", pos=(30, 120))
        self.statictext_3.Wrap(-1)
        self.statictext_3.SetFont(wx.Font(12, 70, 90, 90, False, "宋体"))
        self.textctrl_2 = wx.TextCtrl(self.panel, id=wx.ID_ANY, value="(450.9,279.6)", pos=(140, 115), size=(120, 30))
        self.textctrl_2.SetFont(wx.Font(12, 70, 90, 90, False, "宋体"))
        "旋转角度"
        self.statictext_4 = wx.StaticText(self.panel, label="旋转角度:", pos=(30, 200))
        self.statictext_4.Wrap(-1)
        self.statictext_4.SetFont(wx.Font(12, 70, 90, 90, False, "宋体"))
        self.textctrl_3 = wx.TextCtrl(self.panel, id=wx.ID_ANY, value="-83.83", pos=(140, 195), size=(70, 30))
        self.textctrl_3.SetFont(wx.Font(12, 70, 90, 90, False, "宋体"))
        self.statictext_6 = wx.StaticText(self.panel, label="度", pos=(220, 200))
        self.statictext_6.Wrap(-1)
        self.statictext_6.SetFont(wx.Font(12, 70, 90, 90, False, "宋体"))
        "角点坐标"
        self.statictext_5 = wx.StaticText(self.panel, label="夹爪张开距离:", pos=(30, 280))
        self.statictext_5.Wrap(-1)
        self.statictext_5.SetFont(wx.Font(12, 70, 90, 90, False, "宋体"))
        self.textctrl_4 = wx.TextCtrl(self.panel, id=wx.ID_ANY, value="25.26", pos=(140, 275), size=(50, 30))
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


app = wx.App()
window1 = MyFrame1()
window1.Show()
app.MainLoop()

