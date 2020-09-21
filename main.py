import vk
from coronapenza import parsepenza
from time import sleep
token = 'token'
kd = 300
session = vk.Session(access_token=token)
api = vk.API(session, v = "5.95")
while True:
    print('Autostatus update')
    status = parsepenza()
    api.status.set(text = status)
    sleep(kd)
