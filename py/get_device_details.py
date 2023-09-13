import meraki
from pprint import pprint
import pandas as pd

# Defining your API key as a variable in source code is not recommended
API_KEY = '6675ca84ec0b83d9046628678141799d0d418658'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

#serial = 'Q2HY-EMFP-DTG3'

with open("HPC_meraki_serial.txt") as f:
    data = f.read()
data = data.splitlines()

list_response = []

for sno in data:
    response = dashboard.devices.getDevice(sno)
    list_response.append(response)

#pprint(response)

df = pd.DataFrame(list_response)
df.to_csv('device_info_test.csv',index=False,header=True)
