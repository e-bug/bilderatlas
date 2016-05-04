# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 18:27:20 2016

@author: Emanuele
"""

#! python3
# deleteImagesExcel.py - delete images in the database

import openpyxl
import requests

DBurl = "http://replica.dhlabdemo.org:5009/api/v1/database/id/"

print('Opening workbook')
wb = openpyxl.load_workbook('toBeEliminated.xlsx')
sheets = ['ToEliminate']

for s in range(0, len(sheets)):
    print('Reading', sheets[s])
    sheet = wb.get_sheet_by_name(sheets[s])
    print('Reading rows')
    for r in range(2, sheet.max_row+1): # skip the first row
		
        imageID = sheet['A' + str(r)].value
        if(imageID is None):
            print("Missing image ID at ", sheet, "-", r)
            exit()
        else:
            url = DBurl + str(imageID)
        
        req = requests.delete(url)
        print(req)

 