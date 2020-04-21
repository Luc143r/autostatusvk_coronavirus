import vk
from coronapenza import parsepenza
from time import sleep

token = '3bbfeb7eb6b6ac946ee804565628cfba31ca60e341e0dd6018f7afdd6a36d844eb72d9acf7e4dbab73836'
kd = 120

session = vk.Session(access_token=token)
api = vk.API(session, v = "5.95")
print('Autostatus start')

while True:
    print('Autostatus update')
    status = parsepenza()
    api.status.set(text = status)
    sleep(kd)
    print('Not sleeping')
