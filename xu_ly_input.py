# import cac thu vien
import json
from setdata import admin_pass_check, device

# doc du lieu tu file input
f = open('./input/input.json')
data = json.load(f)
sub = data['Device']
f.close()

# lay luong du lieu goc tu file ./setdata/device.py
setdata = device.device[sub['device']][sub['label']]
setdata["list pass"] = admin_pass_check.device[sub['device']][sub['label']][sub['type']]
# print(setdata)

