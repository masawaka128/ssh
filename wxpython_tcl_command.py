import wx

class myFrame(wx.Frame):
    
    def __init__(self, *args, **keywd):
        wx.Frame.__init__(self, *args, **keywd)
        self.SetTitle('Cadence Sigrity PI用 tcl command作成')
        self.CreateStatusBar()

        self.create_menu()
        bitmap = wx.Image('WxPython-logo.png').ConvertToBitmap()
        bitmap2 = wx.Image('WxPython-logo2.png').ConvertToBitmap()
        self.b1 = wx.StaticBitmap(parent=self,
                        bitmap=bitmap,
                        size=bitmap.GetSize(),
                        )

        self.b2 = wx.StaticBitmap(parent=self,
                        bitmap=bitmap2,
                        size=bitmap2.GetSize(),
                        )
        
        self.b2.Hide()
        self.SetClientSize(self.b1.GetSize())
        self.b1.Bind(wx.EVT_LEFT_DOWN, self.OnClick)
        self.b2.Bind(wx.EVT_LEFT_DOWN, self.OnClick)
        self.sw = 0

    def OnClick(self, event):
        self.sw = 1 -self.sw
        if self.sw == 1:
            self.b1.Hide()
            self.b2.Show()
        else:
            self.b1.Show()
            self.b2.Hide()

    def create_menu(self):
        f_menu = wx.Menu() #ファイルメニュー
        f_menu.Append(-1, "新規")
        f_menu.Append(-1, "終了") 

        s_menu = wx.Menu() #選択メニュー
        s_menu.Append(-1, "Port Setting")
        s_menu.Append(-1, "Target spec比較")   

        m_bar = wx.MenuBar()  
        m_bar.Append(f_menu, "ファイル")
        m_bar.Append(s_menu, "選択メニュー")
        self.SetMenuBar(m_bar)  

class myApp(wx.App):

    def OnInit(self):
        frame = myFrame(parent=None)
        frame.Show()
        self.SetTopWindow(frame)
        return True

app = myApp()
app.MainLoop()
