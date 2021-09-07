import requests

Username = ''
Password = ''
Host = ''

MyIP = requests.get('https://domains.google.com/checkip').text
print(f'Current IP is {MyIP}.')

url = f'https://{Username}:{Password}@domains.google.com/nic/update?hostname={Host}&myip={MyIP}'
req = requests.get(url)
print(req.text)