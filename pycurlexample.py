import pycurl
from io import BytesIO
from io import StringIO
response = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, 'https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/RiotSchmick?api_key=05047aed-e174-4bba-b294-c2c4ec3af4f0>')
c.setopt(c.WRITEFUNCTION, response.write)
c.setopt(c.HTTPHEADER, ['Content-Type: application/json','Accept-Charset: UTF-8'])
c.setopt(c.POSTFIELDS, '@request.json')
c.perform()
c.close()
print (response.getvalue())
response.close()
