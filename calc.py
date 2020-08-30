# -*- coding: utf-8 -*-

import wx

class Calcu(wx.Frame):

    def __init__(self, *args, **keywd):
        wx.Frame.__init__(self, *args, **keywd)

        self.make_frame()
        self.make_menu()

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.display = wx.TextCtrl(self, -1, '', style=wx.TE_RIGHT)
        
        sizer.Add(self.display, 0, wx.EXPAND | wx.ALL, 4)
        gsizer = wx.GridSizer(5, 4, 4, 4)
        labels = ["+/-", "%", "C", "AC",
                  "7",   "8", "9", "÷",
                  "4",   "5", "6", "×",
                  "1",   "2", "3", "-",
                  "0",   ".", "=", "+" ]
        
        for label in labels:
            button = wx.Button(self, -1, label)
            gsizer.Add(button, 1, wx.EXPAND)
            self.Bind(wx.EVT_BUTTON, self.OnClick, button)

        sizer.Add(gsizer, 1, wx.EXPAND | wx.BOTTOM | wx.LEFT | wx.RIGHT, 4)
        self.SetSizer(sizer)

        self.disp_work = 0
        self.total = 0
        self.operator = ""


    def OnClick(self, event):
        label = event.GetEventObject().GetLabel()
        if label in "0123456789":
            self.disp_work = 10 * self.disp_work + int(label)
            self.display.SetValue(str(self.disp_work))
        elif label in "+-×÷":
            self.calc()
            self.display.SetValue(str(self.total))
            self.operator = label
            self.disp_work = 0
        elif label == "=":
            self.calc()
            self.display.SetValue(str(self.total))
            self.operator = ""
            self.disp_work = self.total
        elif label == "AC":
            self.disp_work = 0
            self.total = 0
            self.display.SetValue(str(self.total))

    def calc(self):
        if self.operator == "":
            self.total = self.disp_work
        elif self.operator == "+":
            self.total += self.disp_work
        elif self.operator == "-":
            self.total -= self.disp_work
        elif self.operator == "×":
            self.total *= self.disp_work
        else:
            self.total /= self.disp_work

    def make_frame(self):
        #フレームの作成
        self.SetTitle('電卓')
        self.SetSize(300,300)
        self.CreateStatusBar()

    def make_menu(self):
        #メニューの作成
        file = wx.Menu()
        exit = file.Append(-1, '終了\tCtrl-Q', '電卓を終了します')
        menubar = wx.MenuBar()
        menubar.Append(file, 'ファイル(&F)')
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.OnClose, exit)
        
    def OnClose(self, event):
        self.Close()

class myApp(wx.App):
    
    def OnInit(self):
        frame = Calcu(parent=None)
        frame.Show()
        self.SetTopWindow(frame)
        return True
    
app = myApp()
app.MainLoop()