from data_scraper import scrape_data
from data_adder import *

base_url = "https://myanimelist.net/anime/"
i_start = 0
i_end = 20

results = scrape_data(base_url, i_start, i_end)
for result in results:
    if not data_exists(result[0]):
        add_data(result)
    else:
        continue
