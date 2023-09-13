import meraki
from pprint import pprint

API_KEY = '6675ca84ec0b83d9046628678141799d0d418658'
dashboard = meraki.DashboardAPI(API_KEY)

with open("AP_serial.txt") as f:
 data = f.read()
data = data.splitlines()

ap_details = []
cdp_details = []

for i in data:
    ap_response = dashboard.devices.getDevice(i)
    cdp_response = dashboard.devices.getDeviceLldpCdp(i)
    if len(cdp_response) == 0:
        cdp_response["For serial num: "+ ap_response['serial']] = "No CDP/LLDP"

    ap_details.append(ap_response)
    #ap_details.append(ap_response['lanIp'])
    #ap_details.append(ap_response['mac'])
    #ap_details.append(ap_response['model'])
    #ap_details.append(ap_response['name'])
    ap_details.append(cdp_response)
    ap_details.append("-------------------------------------------")
    ap_details.append("-------------------------------------------")
    ap_details.append("-------------------------------------------")

print()
pprint(ap_details)
print()
print()
#pprint(cdp_details)
#pprint(new_list)
