import requests, random, time

TOKEN = open("token.txt").read()

headers = {
        'Authorization': TOKEN,
        'Content-Type': 'application/json'
}

r_status_code = requests.get("https://discord.com/api/v8/users/@me", headers=headers).status_code

default = True
if r_status_code == 200:
    if default == False:
        r_json = requests.get("https://discord.com/api/v8/users/@me/settings", headers=headers).json()
        print(r_json)
        from storage import languages, modes, boolean, status

        for i in range(100):
            time.sleep(0.12)

            setting = {
                'locale': next(languages),
                'message_display_compact': next(boolean),
                'status': next(status)
            }

            if random.randrange(0,100) >=30:
                setting['theme'] = next(modes)
            requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=setting)
    else:
        setting = {
            'locale': 'pt-BR',
            'message_display_compact': False,
            'status': 'online',
            'custom_status': {
                    'text': 'A vida que queima no inferno e a mesma que queima no teu cu',
                    'expires_at': None
            }
        }

        if random.randrange(0,100) >=30:
            setting['theme'] = 'dark'
        requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=setting)