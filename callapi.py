import requests
import json
from requests.auth import HTTPBsicAuth

# Loading Credentials
with open('C:\\Users\\vadiraj.b\\Desktop\\Python\\com\\MTO_LOCAL\\credentials.json') as f:
    data = json.load(f)


def  getAllconnection():
    url = 'https://10.193.176.19/siebel/v1.0/service/MTO Bulk BIP Template Upload Service/UploadFile'
    headers = {'content-type': 'application/json'}
    r = requests.post(url = url, auth = HTTPBasicAuth(data["username"], data["password"]), headers = headers, verify = False)
    try:
        responseJson = r.json()
        print(responseJson)
        return responseJson
    except:
        print(r)
        return

getAllconnection()