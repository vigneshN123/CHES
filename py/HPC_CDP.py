import meraki
from pprint import pprint
# Defining your API key as a variable in source code is not recommended
API_KEY = '6675ca84ec0b83d9046628678141799d0d418658'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

#response = dashboard.organizations.getOrganizations()

#serial = 'Q2HY-9JT7-L7DL'

#response = dashboard.devices.getDeviceLldpCdp(
#    serial
#)

#organization_id = '369218' -----> HPC org ID

#response = dashboard.organizations.getOrganizationDevicesStatusesOverview(
#    organization_id
#)

#response = dashboard.organizations.getOrganizationDevicesStatuses(
#    organization_id, total_pages='all')

with open("HPC_Dtype_MX67C-NA.txt") as f:
 data = f.read()
data = data.splitlines()

list_MX67C = []

for i in data:
        response = dashboard.devices.getDeviceLldpCdp(i)
        #pprint(f"Device serial number: {i} ")
        list_MX67C.append("----------------------")
        list_MX67C.append("Serial number: ")
        list_MX67C.append(i)
        list_MX67C.append(response)
        list_MX67C.append("----------------------")
        #print(list_MX67C)
        break

pprint(list_MX67C)
