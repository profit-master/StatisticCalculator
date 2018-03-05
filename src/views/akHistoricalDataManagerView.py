# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.0b3 on Fri Feb 16 14:01:02 2018
#

import wx
import wx.adv

from src.views.controls.akTreeControl import AkTreeControl
from src.views.controls.akListCtrl import AkListCtrl

class AkHistoricalDataManagerView(wx.Dialog):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((766, 537))
        self.notebook = wx.Notebook(self, wx.ID_ANY)
        
        self.__initImportPage()
        self.__initDownloadPage()

        self.notebook.AddPage(self.nb_Import, "Import")
        self.notebook.AddPage(self.nb_Download, "Download")      
        
        self.__set_properties()
        self.__do_layout()

    def __set_properties(self):
        self.SetTitle("Historical Data Manager")
        
        self.cb_Format.SetSelection(0)
        self.cb_TimeZone.SetSelection(0)
        self.btn_Download.SetMinSize((182, 26))
       
        self.dpStart.SetMinSize((123, 23))
        self.dpEnd.SetMinSize((123, 23))

    def __do_layout(self):
       
        self.__doImportPageLayout()
        self.__doDownloadPageLayout()
                
        vBox = wx.BoxSizer(wx.VERTICAL)
        vBox.Add(self.notebook, 1, wx.EXPAND, 0)
        self.SetSizer(vBox)
        self.Layout()

    def __initImportPage(self):
        self.nb_Import = wx.Panel(self.notebook, wx.ID_ANY)
        
        self.cb_Format = wx.ComboBox(self.nb_Import, wx.ID_ANY, choices=["Trade Workstation", "Metatrader 4"], style=wx.CB_DROPDOWN)
        self.cb_TimeZone = wx.ComboBox(self.nb_Import, wx.ID_ANY, choices=["UTC"], style=wx.CB_DROPDOWN)

        self.btn_Import = wx.Button(self.nb_Import, wx.ID_ANY, "Start Import")
     
    def __initDownloadPage(self):
        self.nb_Download = wx.Panel(self.notebook, wx.ID_ANY)       
        
        self.tr_Instruments = AkTreeControl(self.nb_Download, wx.ID_ANY)
        self.lst_Data = AkListCtrl(self.nb_Download, wx.ID_ANY, style=wx.LC_HRULES | wx.LC_REPORT | wx.LC_VRULES)
        
        self.btn_Download = wx.Button(self.nb_Download, wx.ID_ANY, "Download")
        self.btnFilter = wx.Button(self.nb_Download, wx.ID_ANY, "Filter")

        self.chbStart = wx.CheckBox(self.nb_Download, wx.ID_ANY, "")
        self.chbEnd = wx.CheckBox(self.nb_Download, wx.ID_ANY, "")

        self.dpStart = wx.adv.DatePickerCtrl(self.nb_Download, wx.ID_ANY)
        self.dpEnd = wx.adv.DatePickerCtrl(self.nb_Download, wx.ID_ANY)
        

    def __doImportPageLayout(self):    
        lblInpurFormat = wx.StaticText(self.nb_Import, wx.ID_ANY, "Data Input Format")
        lblTimeZone = wx.StaticText(self.nb_Import, wx.ID_ANY, "Time zone of imported data:")
        
        vBox_Labels = wx.BoxSizer(wx.VERTICAL)
        vBox_Labels.Add(lblInpurFormat, 0, wx.ALL, 20)
        vBox_Labels.Add(lblTimeZone, 0, wx.ALL, 20)
        
        vBox_Inputs = wx.BoxSizer(wx.VERTICAL)
        vBox_Inputs.Add(self.cb_Format, 0, wx.ALL | wx.EXPAND, 15)
        vBox_Inputs.Add(self.cb_TimeZone, 0, wx.ALL | wx.EXPAND, 15)
        vBox_Inputs.Add(self.btn_Import, 0, wx.ALL, 15)
        
        sBox = wx.StaticBoxSizer(wx.StaticBox(self.nb_Import, wx.ID_ANY, ""), wx.HORIZONTAL)
        sBox.Add(vBox_Labels, 1, wx.EXPAND, 0)
        sBox.Add(vBox_Inputs, 2, wx.EXPAND, 0)
        
        self.nb_Import.SetSizer(sBox)
       
    def __doDownloadPageLayout(self):
        lblSymbols = wx.StaticText(self.nb_Download, wx.ID_ANY, "Symbols:")        
        lbl_Database = wx.StaticText(self.nb_Download, wx.ID_ANY, "Database:")

        lblStartDate = wx.StaticText(self.nb_Download, wx.ID_ANY, "Start date:")
        lblEndDate = wx.StaticText(self.nb_Download, wx.ID_ANY, "End date:")
 
        vBox_Tree = wx.BoxSizer(wx.VERTICAL)
        vBox_Tree.Add(lblSymbols, 0, wx.BOTTOM | wx.TOP, 5)
        vBox_Tree.Add(self.tr_Instruments, 1, wx.EXPAND, 0)
        vBox_Tree.Add(self.btn_Download, 0, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 15)

        fxGrid = wx.FlexGridSizer(0, 3, 0, 0)
        fxGrid.Add(lblStartDate, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        fxGrid.Add(self.chbStart, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        fxGrid.Add(self.dpStart, 0, wx.ALIGN_CENTER | wx.ALL, 5)        
        fxGrid.Add(lblEndDate, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        fxGrid.Add(self.chbEnd, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        fxGrid.Add(self.dpEnd, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        vBox_Grid = wx.BoxSizer(wx.VERTICAL)
        vBox_Grid.Add(fxGrid, 1, wx.ALIGN_CENTER | wx.EXPAND, 0)
        vBox_Grid.Add(self.btnFilter, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        sBox_Filter = wx.StaticBoxSizer(wx.StaticBox(self.nb_Download, wx.ID_ANY, "Filter data"), wx.HORIZONTAL)
        sBox_Filter.Add(vBox_Grid, 0, wx.EXPAND, 0)
        sBox_Filter.Add((60, 0), 1, 0, 0)
        
        vBox_List = wx.BoxSizer(wx.VERTICAL)     
        vBox_List.Add(lbl_Database, 0, wx.BOTTOM | wx.TOP, 5)
        vBox_List.Add(self.lst_Data, 1, wx.EXPAND, 0) 
        vBox_List.Add(sBox_Filter, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.BOTTOM | wx.EXPAND | wx.TOP, 0)       

        hBox = wx.BoxSizer(wx.HORIZONTAL)
        hBox.Add(vBox_Tree, 1, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)       
        hBox.Add(vBox_List, 2, wx.EXPAND, 0) 
        
        self.nb_Download.SetSizer(hBox)