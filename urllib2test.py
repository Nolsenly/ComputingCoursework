import urllib2
request = urllib2.Request('https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/RiotSchmick?api_key=05047aed-e174-4bba-b294-c2c4ec3af4f0')
html = response.read()
print(html)
