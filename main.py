import requests
from bs4 import BeautifulSoup, ResultSet, Tag

from config import settings
from utils import logger


def main():
    dex = input("Enter DEX to search for token (Raydium, Orca, Uniswap, Pancakeswap…): ").strip().lower()
    min_liquid = input("Enter the minimum amount of liquid: ")
    # etc. filter by any data

    url = f'https://dexscreener.com/solana?rankBy=trendingScoreH6&order=asc&dexIds={dex}&minLiq={min_liquid}&minMarketCap=800000&maxFdv=200000000&maxAge=12&min24HVol=3500000&profile=1'
    apikey = settings.ZENROWS_API_KEY
    params = {
        'url': url,
        'apikey': apikey,
        'js_render': 'true',
        'premium_proxy': 'true',
    }
    response = requests.get('https://api.zenrows.com/v1/', params=params)
    dexscreener_html = response.text


    soup = BeautifulSoup(dexscreener_html, "lxml")

    tokens: ResultSet[Tag] = soup.find_all(class_='ds-dex-table-row')


    for token in tokens:
        token_div: Tag = token.find(class_='ds-table-data-cell')
        token_name: Tag = token_div.find(class_='ds-dex-table-row-base-token-symbol')
        logger.info(f"Token <g>'{token_name.text}'</g>")


if __name__ == "__main__":
    print(settings.START_TEXT)
    main()
