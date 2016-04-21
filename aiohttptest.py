import asyncio
import aiohttp

def fetch_page(session, url):
    with aiohttp.Timeout(10):
        with session.get(url) as response:
            assert response.status == 200
            return response.read()

loop = asyncio.get_event_loop()
with aiohttp.ClientSession(loop=loop) as session:
    content = loop.run_until_complete(
        fetch_page(session, 'https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/RiotSchmick?api_key=05047aed-e174-4bba-b294-c2c4ec3af4f0'))
    print(content)
