import urllib
from bs4 import BeautifulSoup as bs

url = "https://myanimelist.net/anime/35849/"
page = urllib.request.urlopen(url)
soup = bs(page, 'html.parser')

status = None
num_eps = None
spans = soup.find_all('span', attrs={'class':'dark_text'})
for span in spans:
    parent_div = span.parent
    content = parent_div.text.strip()
    if "Status:" in content:
        status = content.replace("\n","")[7:].strip()
    if "Episodes:" in content:
        num_eps = content.replace("\n","")[9:].strip()

print(status)
print(num_eps)
