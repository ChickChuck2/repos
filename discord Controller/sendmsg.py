import requests

TOKEN = open("token.txt").read()

headers = {'Authorization': TOKEN}

channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers).json()

consend = requests.post(f'https://discord.com/api/v9/channels/942528474017587251/messages', headers=headers,
    data={"content": "teste"})
print(consend.json())