from bs4 import BeautifulSoup as bs
import requests
import math


# better to have a function that creates the html object and pass that to these functions below
def pull_pages(url):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
        "Upgrade-Insecure-Requests": "1", "DNT": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate"}

    response = requests.get(url, headers=headers)
    html = response.content

    soup = bs(html, "lxml")
    all_reviews = soup.find_all("span", class_="ugc-list__review__display")
    for review in all_reviews:
        print(review.get_text(strip=True))
        print("\n")


def get_number_of_pages(url):
    reviews_per_page = 10
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
        "Upgrade-Insecure-Requests": "1", "DNT": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate"}

    response = requests.get(url, headers=headers)
    html = response.content
    soup = bs(html, "lxml")
    full_string = soup.find("h2", class_="ugc-list__reviews__heading").get_text()

    number_of_reviews = int(full_string[0:2])
    return math.ceil(number_of_reviews/reviews_per_page)
