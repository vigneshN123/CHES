import meraki
from pprint import pprint 


API_KEY = '6675ca84ec0b83d9046628678141799d0d418658'

dashboard = meraki.DashboardAPI(API_KEY)

with open("AP_serial.txt") as f:
 data = f.read()
data = data.splitlines()

AP_dets = []
list_APS = []
for i in data:
    response = dashboard.devices.getDevice(i)
    list_APS.append(response)
 

pprint(list_APS) 
