import meraki
from pprint import pprint

API_KEY = '6675ca84ec0b83d9046628678141799d0d418658'

dashboard = meraki.DashboardAPI(API_KEY)

network_id = 'N_636696397319541884'

response = dashboard.networks.getNetworkClients(
    network_id, total_pages='all'
)

pprint(response)