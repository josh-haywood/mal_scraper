import urllib
from bs4 import BeautifulSoup as bs
from datetime import datetime

def scrape_data(base_url, i_start, i_end):
    # data values to be searched for
    title = None
    rating = None
    num_eps = None
    status = None
    start_date = None
    end_date = None
    results = []

    # iterate over all posible url's on MAL
    for i in range(i_start, i_end):
        # try to open webpage
        # skip page if exception is thrown
        try:
            page = urllib.request.urlopen(base_url + str(i))
        except:
            continue

        # create HTML parser with BeautifulSoup
        soup = bs(page, 'html.parser')

        # fetch anime title
        title = soup.find('span', attrs={'itemprop':'name'}).text.strip()

        # fetch anime rating
        rating = soup.find('div', attrs={'data-title':'score'}).text.strip()

        # getting airing data, number of episodes, and airing status is non-trivial
        # iterate over all posible div-span combos and look for certain strings
        spans = soup.find_all('span', attrs={'class':'dark_text'})
        for span in spans:
            # get the parent div
            parent_div = span.parent

            # get text from div object
            content = parent_div.text.strip()

            # parse data given by content
            # case: Episodes
            if "Episodes:" in content:
                num_eps = content.replace(" ", "").replace("\n","")[9:].strip()
            # case: Status
            elif "Status:" in content:
                status = content.replace("\n","")[7:].strip()
            # case: Aired
            elif "Aired:" in content:
                # split start and ending dates
                dates = content.strip().replace("\n","")[6:].split("to")

                # check to see if end date is valid
                if len(dates) < 2:
                    end_date = ""
                elif dates[1].strip() == "?":
                    end_date = ""
                else:
                    end_date_dt = datetime.strptime(dates[1].strip(), "%b %d, %Y")
                    end_date = str(end_date_dt).split(" ")[0]

                # get start date
                start_date_dt = datetime.strptime(dates[0].strip(), "%b %d, %Y")
                start_date = str(start_date_dt).split(" ")[0]
        result_tup = (title, rating, num_eps, status, start_date, end_date, 0)
        results.append(result_tup)
    return results
