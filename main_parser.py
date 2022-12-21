import requests
import time
import csv

def take_100_users():
    token = '#ADDYOURTOKEN'
    version = 5.92
    domain = '#ADDNAMEOFGROUP'
    count = 1000
    offset = 0
    all_users = []
    while offset < 100:
        response = requests.get('https://api.vk.com/method/groups.getMembers',
                                params = {
                                    'access_token': token,
                                    'v':version,
                                    'group_id': domain,
                                    'count': count,
                                    'offset': offset
                                })
        data = response.json()['response']['items']
        offset += 1
        all_users.extend(data)
        time.sleep(0.5)
    return all_users
def users_file(all_users):
    with open('users.csv','w') as file:
        a_pen = csv.writer(file)
        a_pen.writerow('names')
        for us in all_users:
            a_pen.writerow(us)

all_users = take_100_users()
users_file(all_users)



