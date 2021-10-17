from bs4 import BeautifulSoup as bs
import requests


def pullPage():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
        "Upgrade-Insecure-Requests": "1", "DNT": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate"}

    url = "https://www.chewy.com/app/product-reviews/rel" \
          "oad?partNumber=91615&id=119264&reviewSort=NEWEST&reviewFilter=ALL_STARS&pageNumber=1"
    test = "https://www.bookdepository.com/bestsellers"

    response = requests.get(url, headers=headers)
    html = response.content
    print(response)

    soup = bs(html, "lxml")
    all_reviews = soup.find_all("span", class_="ugc-list__review__display")
    for review in all_reviews:
        print(review.get_text(strip=True))
        print("\n")



