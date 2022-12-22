import requests
import time
import csv
from tqdm import tqdm, tqdm_gui, trange

def take_100_users():
    token = input('Введите токен:')
    version = 5.92
    domain = input('Введите ID сообщества:')
    count = 1000
    offset = 0
    all_users = []
    while offset < 100:
        response = requests.get('https://api.vk.com/method/groups.getMembers',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'group_id': domain,
                                    'count': count,
                                    'offset': offset
                                })
        data = response.json()['response']['items']
        offset += 1
        all_users.extend(data)
    all_users = list(set(all_users))
    return all_users
def users_file(data):
    name_file = input('Как назовем файл?:')
    with open('%s.csv'%name_file, 'w') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('ids', ))
        for us in data:
            a_pen.writerow(('vk.com/id'+str(us), ))
    print('Файл готов')

all_users = take_100_users()
users_file(all_users)



