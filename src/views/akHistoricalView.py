# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.0b3 on Fri Feb 16 14:01:02 2018
#

import wx
import wx.adv

from src.views.akDownloadView import AkDownloadView
from src.views.akImportView import AkImportView

class AkHistoricalView(wx.Dialog):
    def __init__(self, parent, controller):
        style = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER
        super(AkHistoricalView, self).__init__(parent, style=style)
        self.SetInitialSize((766, 537))
        
        self.controller = controller
        self.controller.Register(self)
        
        self._notebook = wx.Notebook(self, wx.ID_ANY)
        self._importView = AkImportView(self._notebook, self.controller)
        self._downloadView = AkDownloadView(self._notebook, self.controller)

        self.__set_properties()
        self.__do_layout()
        self.__set_bindings()        

#------------------------------------------------------------------------------
# Private methods
#------------------------------------------------------------------------------

    def __set_bindings(self):
        self.Bind(wx.EVT_CLOSE, self.OnCloseView_Handler)
        self.Bind(wx.EVT_WINDOW_DESTROY, self.OnDestroyView_Handler)

    def __set_properties(self):
        self.SetTitle("Historical Data Manager")

    def __do_layout(self):                
        sizer = wx.BoxSizer(wx.VERTICAL)

        self._notebook.AddPage(self._importView, "Import")
        self._notebook.AddPage(self._downloadView, "Download")              
        sizer.Add(self._notebook, 1, wx.EXPAND, 0)
        
        self.SetSizer(sizer)
        self.Layout()

#------------------------------------------------------------------------------        
# Get/Set methods
#------------------------------------------------------------------------------
    def GetNotebook(self):
        return self._notebook

    def GetImportView(self):
        return self._importView
    
    def GetDownloadView(self):
        return self._downloadView

#------------------------------------------------------------------------------
# Event Handlers
#------------------------------------------------------------------------------
        
    def OnCloseView_Handler(self, event):
        print("Event handler 'OnCloseView_Handler' not implemented!")
        event.Skip()

    def OnDestroyView_Handler(self, event):
        print("Event handler 'OnDestroyView_Handler' not implemented!")
        event.Skip()