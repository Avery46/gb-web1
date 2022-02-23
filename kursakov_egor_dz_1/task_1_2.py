import requests
import json
appid = 'b6907d289e10d714a6e88b30761fae22'
service = 'https://samples.openweathermap.org/data/2.5/weather'
req = requests.get(f'{service}?q=London,uk&appid={appid}')
data = json.loads(req.text)
dz = input('ввод номера дз- ')
num = input('ввод номера задания- ')
with open('kursakov_egor_dz_'+dz+'/rep_'+dz+'_'+num+'.json', 'w') as f:
    json_repo = json.dump(data, f)