import meraki
from pprint import pprint

API_KEY = '6675ca84ec0b83d9046628678141799d0d418658'

dashboard = meraki.DashboardAPI(API_KEY)

serial = 'Q2HY-7F8A-BDY3'

response = dashboard.devices.getDeviceClients(
    serial
)

pprint(response)