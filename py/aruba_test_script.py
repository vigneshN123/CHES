from pycentral.base import ArubaCentralBase
from pprint import pprint
import requests

#central_info = {
#    "base_url": "https://apigw-prod2.central.arubanetworks.com",
#    "token": {
#        "access_token": "W5y3uqhbf7X91Px9DFRf4438ie2pzvEt"
#    }
#}

central_info = {
        "username": "nagarajan.vignesh@cleanharbors.com",
        "password": "Anarki1986!",
        "client_id": "8V2MM3tvwWCRlVQ9WUTVdVI6xmtpYOQl",
        "client_secret": "ztleC1bzW7VEIL59PN16RcVZUlkSxXw2",
        "customer_id": "2003389",
        "base_url": "https://apigw-prod2.central.arubanetworks.com"
    }

ssl_verify = True
central = ArubaCentralBase(central_info=central_info,ssl_verify=ssl_verify)

apiPath = "/configuration/v2/groups"
apiMethod = "GET"
apiParams = {
    "limit": 5,
    "offset": 0
}

base_resp = central.command(apiMethod=apiMethod,apiPath=apiPath,apiParams=apiParams)

pprint(base_resp)
