import wx

class myFrame(wx.Frame):
    
    def __init__(self, *args, **keywd):
        wx.Frame.__init__(self, *args, **keywd)
        self.make_frame()
        self.make_menu()

        #パネルの生成
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour((0, 200, 0))

        te1 = wx.TextCtrl(panel, -1, "te1", style=wx.TE_MULTILINE)
        te2 = wx.TextCtrl(panel, -1, "te2", style=wx.TE_MULTILINE)
        te3 = wx.TextCtrl(panel, -1, "te3", style=wx.TE_MULTILINE)
        te4 = wx.TextCtrl(panel, -1, "te4", style=wx.TE_MULTILINE)
        
        sizer = wx.GridSizer(2, 2, 0, 0)
        sizer.Add(te1, 1, wx.EXPAND | wx.ALL, 10)
        sizer.Add(te2, 1, wx.ALIGN_LEFT)
        sizer.Add(te3, 1, wx.EXPAND)
        sizer.Add(te4, 1, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        panel.SetSizer(sizer)

    def make_frame(self):
        #フレームの作成
        self.SetTitle('Sizer')       
        self.SetSize((500, 500))
        self.CreateStatusBar()           

    def make_menu(self):
        #メニュー作成
        file = wx.Menu()
        edit = wx.Menu()
        m_bar = wx.MenuBar()
        m_bar.Append(file,"ファイル(&F)")
        m_bar.Append(edit,"編集(&E)")
        self.SetMenuBar(m_bar)
    
class myApp(wx.App):
    
    def OnInit(self):
        frame = myFrame(parent=None)
        frame.Show()
        self.SetTopWindow(frame)
        return True

    
app = myApp()
app.MainLoop()