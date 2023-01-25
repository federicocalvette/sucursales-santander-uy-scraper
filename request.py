import requests
import settings

def bank_request():

    bank_branch_json = requests.get(settings.WEB_URL)
    
    return bank_branch_json