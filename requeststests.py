import requests
r = requests.get('https://euw.api.pvp.net/api/lol/euw/v1.4/summoner/by-name/kuurasov?api_key=05047aed-e174-4bba-b294-c2c4ec3af4f0')
print(r.json())
