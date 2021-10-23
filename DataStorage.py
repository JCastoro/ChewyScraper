from TestingManyPages import *
import re
import pandas as pd


def load_data(rootURL):
    page = 1
    maxPages = 1

    review_id = 1  # this will work for now but will need more advanced hashing system

    star_rating_list = []
    review_list = []
    data_content_list = []
    author_list = []
    date_list = []
    media_list = []

    while page <= int(maxPages):

        #data_content_list_this_page = []

        currPage = rootURL + str(page)

        curr_page_soup = pull_pages(currPage)


        #all_data_content_ids = curr_page_soup.find_all("li", class_="js-content")
        data_content_list = get_list_of_data_content(curr_page_soup, data_content_list)
        #data_content_list = get_list_of_data_content(curr_page_soup, data_content_list_this_page)


        all_data_blocks = curr_page_soup.find_all("li", class_="js-content")
        for data_block in all_data_blocks:
            data_content_id = data_block.find("data-content-id")
            long_star_rating = str(data_block.find("meta", itemprop="ratingValue"))
            star_rating = process_star_rating(long_star_rating)
            star_rating_list.append(star_rating)

        all_reviews = curr_page_soup.find_all("span", class_="ugc-list__review__display")
        for review in all_reviews:
            review_text = (review.get_text(strip=True))
            review_list.append(review_text)
            # iterate up review_id for unique keys (This will not work for pulling only certain pages at a time
            # needs to change if we ever want to pull just newest page etc.
            review_id += 1

        all_authors = curr_page_soup.find_all("span", itemprop="author")
        for author in all_authors:
            author_list.append(author.getText())

        all_dates = curr_page_soup.find_all("span", itemprop="datePublished")
        for date in all_dates:
            date_list.append(date.getText())


        blocks = curr_page_soup.find_all("li", {"class": "js-content"})
        # iterates through each block
        for block in blocks:
            if (block.find("li", role="presentation")):
                media_list.append(process_image_text(block))
            else:
                media_list.append("None")


        #print(curr_page_soup.find("li", {"data-content-id": entry}).find("li", role="presentation"))

        # iterating
        maxPages = get_number_of_pages(currPage)
        page += 1

    # creating dataFrame
        # Date of review, UserName, star rating, review text, media as boolean

    d = {
        "Date": pd.Series(date_list, index=data_content_list),
        "Author": pd.Series(author_list, index=data_content_list),
        "Star Rating": pd.Series(star_rating_list, index=data_content_list),
        "Review Text": pd.Series(review_list, index=data_content_list),
        "Media": pd.Series(media_list, index=data_content_list)
        }

    df = pd.DataFrame(d)
    df.to_csv("ReviewData.csv", index=False)
    print(df)


def create_series(list_of_soup_objects, list_for_series):
    for item in list_of_soup_objects:
        list_for_series.append(item)


def create_series_get_text(list_of_soup_objects, list_for_series):
    for item in list_of_soup_objects:
        list_for_series.append(item.getText())



def process_star_rating(long_text):
    # <meta content="5" itemprop="ratingValue"/>
    # pulls out the number in content which is the star rating
    long_text = long_text.strip()
    processed_text = int(re.search(r'\d+', long_text).group())
    return processed_text


def get_list_of_data_content(curr_page_soup, data_content_list):
    test2 = curr_page_soup.find_all("li", {"class": "js-content"})

    for tester in test2:
        tester = str(tester)
        idx_of_num = tester.find("data-content-id=")
        number = tester[idx_of_num + 17:(idx_of_num + 25)]

        data_content_list.append(number)

    return data_content_list

def process_image_text(js_content_block):
    images = js_content_block.find_all("li", role="presentation")
    for image in images:
        to_process = str(image)
        idx_of_url = to_process.find("url")
        idx_of_endof_url = to_process.find(");")
        return to_process[idx_of_url+4:idx_of_endof_url]