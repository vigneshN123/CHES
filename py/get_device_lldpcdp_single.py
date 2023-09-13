import meraki
from pprint import pprint
import pandas as pd

API_KEY = '6675ca84ec0b83d9046628678141799d0d418658'

dashboard = meraki.DashboardAPI(API_KEY)

i = 'Q2HY-7424-3J54'

response = dashboard.devices.getDeviceLldpCdp(i)

pprint(response)
