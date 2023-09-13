import meraki
from pprint import pprint
import pandas as pd

API_KEY = '6675ca84ec0b83d9046628678141799d0d418658'

dashboard = meraki.DashboardAPI(API_KEY)

with open("HPC_networkid2.txt") as f:
 data = f.read()
data = data.splitlines()

list_switches_ap = []
list_response = []

#network_id = 'N_636696397319543920'

for network_id in data:
    response = dashboard.networks.getNetworkClients(network_id, total_pages='all')
    list_response.append(response)


for i in list_response:
    for j in i:
        list_switches_ap.append(j)

df = pd.DataFrame(list_switches_ap)
df.to_csv('NetworkClients.csv',index=False,header=True)
