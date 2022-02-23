import requests
import time
import json

def get_data(url: str) -> dict:
    while True:
        time.sleep(1)
        response = requests.get(url)
        if response.status_code == 200:
            break
    return response.json()

username = input('Введите имя: ')
username = 'Avery46' if username == '' else username

url = 'https://api.github.com/users/' + username + '/repos'

response = get_data(url)
print(response)

repo = []
for itm in response:
    repo.append(itm['name'])
print(f'Репозитори {username}')
print(repo)
dz = input('ввод номера дз- ')
num = input('ввод номера задания- ')
with open('kursakov_egor_dz_'+dz+'/rep_'+dz+'_'+num+'.json', 'w') as f:
    json_repo = json.dump(repo, f)
