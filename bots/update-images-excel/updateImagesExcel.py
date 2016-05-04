# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 18:17:22 2016

@author: e-bug
"""

#! python3
# updateImagesExcel.py - update images in the database

import openpyxl
import requests

DBurl = "http://replica.dhlabdemo.org:5009/api/v1/database/id/"

excel_file = 'toBeUpdated.xlsx'
sheets = ['ToUpdate']


wb = openpyxl.load_workbook(excel_file)

for s in range(0, len(sheets)):
    sheet = wb.get_sheet_by_name(sheets[s])
	
    for r in range(2, sheet.max_row+1): # skip the first row
        imageID = sheet['A' + str(r)].value
        if(imageID is None):
            print("Missing image ID at ", sheet, "-", r)
            exit()
        else:
            url = DBurl + str(imageID)
        author = sheet['B' + str(r)].value
        if(author is None):
            author = ""
        title = sheet['C' + str(r)].value
        if(title is None):
            title = ""
        date = sheet['D' + str(r)].value
        if(date is None):
            date = ""
        school = sheet['E' + str(r)].value
        if(school is None):
            school = ""
        form = sheet['F' + str(r)].value
        if(form is None):
            form = ""
        typeImg = sheet['G' + str(r)].value
        if(typeImg is None):
            typeImg = ""
        
        jsonData = {"metadata": {"author": str(author),
                             "title": str(title),
                             "date": str(date),
                             "school": str(school),
                             "form": str(form),
                             "type": str(typeImg)
                             },
               }
        req = requests.put(url, json = jsonData)
        print(req)

 