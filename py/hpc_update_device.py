import meraki
from pprint import pprint
import pandas as pd

API_KEY = '6675ca84ec0b83d9046628678141799d0d418658'

dashboard = meraki.DashboardAPI(API_KEY)

#serial = 'Q2HY-GG4Z-78BD'

#response = dashboard.devices.updateDevice(
#    serial, 
#    name='1235-NCF-FW1 - US-CA-SACR2', 
#)

with open('hpc_device_nameupdate_serial.txt') as f:
    fdata = f.read()

fdata = fdata.splitlines()

with open('hpc_device_nameupdate_names.txt') as f:
    fname = f.read()

fname = fname.splitlines()

for (i,j) in zip(fdata,fname):
    response = dashboard.devices.updateDevice(i, name = j)
    pprint(response)
    #break


