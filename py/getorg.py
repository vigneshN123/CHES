import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6675ca84ec0b83d9046628678141799d0d418658'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)


response = dashboard.organizations.getOrganizations()

print(response)