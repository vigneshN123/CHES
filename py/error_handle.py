import meraki
from pprint import pprint
import pdb

API_KEY = '6675ca84ec0b83d9046628678141799d0d418658'

dashboard = meraki.DashboardAPI(API_KEY)

serial = 'Q2HY-7S6E-RGKL'

#pdb.set_trace()

try:
    response = dashboard.devices.getDeviceLldpCdp(serial)
except ValueError as e:
    print(e.status)
    print(e.reason)
    print(e.message)
