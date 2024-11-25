from bs4 import BeautifulSoup, ResultSet, Tag

from utils import logger


with open('dexscreener.html', encoding='utf-8') as file:
    dexscreener_html = file.read()


soup = BeautifulSoup(dexscreener_html, "lxml")

tokens: ResultSet[Tag] = soup.find_all(class_='ds-dex-table-row')


for token in tokens:
    token_div: Tag = token.find(class_='ds-table-data-cell')
    token_name: Tag = token_div.find(class_='ds-dex-table-row-base-token-symbol')
    logger.info(f"Token <g>'{token_name.text}'</g>")

