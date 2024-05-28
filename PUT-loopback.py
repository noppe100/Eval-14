import json
import requests
requests.packages.urllib3.disable_warnings()

api_url = "https://172.17.6.66/restconf/data/ietf-interfaces:interfaces/interface=Loopback1"

headers = { "Accept": "application/yang-data+json",
 "Content-type":"application/yang-data+json"
 }

basicauth = ("developer", "cisco")

yangConfig = {
 "ietf-interfaces:interface": {
 "name": "Loopback1",
 "description": "My second RESTCONF loopback",
 "type": "iana-if-type:softwareLoopback",
 "enabled": True,
 "ietf-ip:ipv4": {
 "address": [
 {
 "ip": "200.200.200.200",
 "netmask": "255.255.255.240"
 }
 ]
 },
 "ietf-ip:ipv6": {}
 }
}

resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth,
headers=headers, verify=False)

if(resp.status_code >= 200 and resp.status_code <= 299):
 print("STATUS OK: {}".format(resp.status_code))

else:
 print('Error. Status Code: {} \nError message:{}'.format(resp.status_code,resp.json()))