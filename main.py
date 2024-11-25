import requests

from config import settings


url = 'https://dexscreener.com/solana?rankBy=trendingScoreH6&order=asc&dexIds=raydium&minLiq=1000&minMarketCap=800000&maxFdv=200000000&maxAge=12&min24HVol=3500000&profile=1'
apikey = settings.ZENROWS_API_KEY
params = {
    'url': url,
    'apikey': apikey,
    'js_render': 'true',
    'premium_proxy': 'true',
}
response = requests.get('https://api.zenrows.com/v1/', params=params)
print(response.text)


with open('dexscreener.html', mode='w', encoding='utf-8') as file:
    file.write(response.text)
