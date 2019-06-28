import wx, os

class MyFrame(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(1280,720))
        self.control = wx.TextCtrl(self, style = wx.TE_MULTILINE)
        self.CreateStatusBar()
        self.dirname = ''
        self.filename = ''

        filemenu = wx.Menu()
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", "Information about this program")
        filemenu.AppendSeparator()
        menuNew = filemenu.Append(wx.ID_NEW, "&New", "Create a new file")
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open File", "Open a file")
        menuSave = filemenu.Append(wx.ID_SAVE, "&Save", "Save your file")
        menuSaveAs = filemenu.Append(wx.ID_SAVEAS, "&Save As", "Save file as")
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT, "&Exit", "Terminate the program")

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")
        self.SetMenuBar(menuBar)
        self.Show(True)

        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnNew, menuNew)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnSave, menuSave)
        self.Bind(wx.EVT_MENU, self.OnSaveAs, menuSaveAs)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

    def OnAbout(self, event):
        dlg = wx.MessageDialog(self, "A basic text editor made by Humza Ayub", "About Simple Text Editor")
        dlg.ShowModal()
        dlg.Destroy()

    def OnNew(self, event):
        warning = "You haven't saved your file yet!"
        question = "Are you sure you wish to create a new file?"
        file = open(os.path.join(self.dirname, self.filename), 'r')
        if self.control.GetValue() != file.read():
            dlg = wx.MessageDialog(self, warning + "\n" + question, "WARNING", \
                wx.ICON_WARNING | wx.YES_NO)
            answer = dlg.ShowModal()
            if answer == wx.ID_YES:
                pass
            else:
                return
        self.dirname = ''
        self.filename = ''
        self.control.SetValue('')

    def OnOpen(self, event):
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.FD_OPEN)

        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()

    def OnSave(self, event):
        itcontains = self.control.GetValue()
        filehandle = open(os.path.join(self.dirname, self.filename), 'w')
        filehandle.write(itcontains)
        filehandle.close()

    def OnSaveAs(self, event):
        self.dirname = ''
        dlg = wx.FileDialog(self,
        "Choose a file", self.dirname, "", "*.*", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            itcontains = self.control.GetValue()

            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            filehandle = open(os.path.join(self.dirname, self.filename),'w')
            filehandle.write(itcontains)
            filehandle.close()
        dlg.Destroy()

    def OnExit(self, event):
        self.Close(True)


if __name__ == "__main__":
    app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
    frame = MyFrame(None, "Simple Text Editor") # A Frame is a top-level window.
    app.MainLoop()