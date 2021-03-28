import requests
from pprint import pprint
import json
from time import sleep

# Realiza request al token y luego lo usa como header para obtener una lista
print("Ejecutandose...")
response = requests.post(
    'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token',
    headers={'Authorization':'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='})
response.raise_for_status()
payload=response.json()
while True: 
	response = requests.get(
	    'https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device',
	    headers={'X-Auth-Token': payload['Token']})
	Dict = response.json()['response']
	nameList = {}
	nameList['Dispositivos'] = []
	for i in range(len(Dict)):
		
		nameList['Dispositivos'].append({
						'Nombre':  Dict[i]['hostname'], 
						'Estatus': Dict[i]['reachabilityStatus']})

	with open('Jsonfile','a') as file:
		json.dump(nameList,file, indent=4)

	pprint(nameList)
	sleep(300)
	

