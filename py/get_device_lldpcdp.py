import meraki
from pprint import pprint
import pandas as pd
import ipdb

API_KEY = '6675ca84ec0b83d9046628678141799d0d418658'

with open('HPC_meraki_67CNA_serial.txt') as f:
    snum = f.read()

snum = snum.splitlines()

dashboard = meraki.DashboardAPI(API_KEY)

list_response = []


for i in snum:
    response = dashboard.devices.getDeviceLldpCdp(i)
    list_response.append(response)

#pprint(list_response)
#for (i,j) in zip(fdata,fname):
    #response = dashboard.devices.updateDevice(i, name = j)

new_list = []

for i,j in zip(list_response,snum):
    dict_response ={}
    if len(i) == 0:
        print(f"lldp for serial number: {j} has no data")
        pass
    else:
        for k in i['ports'].keys():
            #ipdb.set_trace()
            dict_response['serial num'] = j
            new_list.append(dict_response)
            if i['ports'][k].get('lldp') == None:
                pass
            else:
                new_list.append(i['ports'][k]['lldp'])

#pprint(new_list)
df = pd.DataFrame(new_list)
df.to_csv('lldp_meraki.csv',index=False,sep=",",header=True)

#serial = 'Q2HY-4R5K-XKRB'

#response = dashboard.devices.getDeviceLldpCdp(
#    serial
#)

#pprint(response)
