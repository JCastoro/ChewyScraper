from TestingManyPages import *
import re
import pandas as pd


def load_media(rootURL):
    page = 1
    currPage = rootURL + str(page)
    curr_page_soup = pull_pages(currPage)

    count = 0

     # generates list of js-content blocks
    blocks = curr_page_soup.find_all("li", {"class": "js-content"})

    # iterates through each block
    for block in blocks:
        # Date of review, UserName, star rating, review text, media as boolean

        # get Date of review
            #add it to date list

        # do same for all others
        # for media will need to add None to list if no media

        # create dataFrame for



        review = block.find("span", class_="ugc-list__review__display")

        if(block.find("li", role="presentation")):
            process_image_text(block)


        count += 1
        # print("----------------------------------\n")
        # print("review: ")
        # print(review.get_text())
        # print("\n")
        # print(block)
    print(count)



def process_image_text(js_content_block):
    images = js_content_block.find_all("li", role="presentation")
    for image in images:
        to_process = str(image)
        idx_of_url = to_process.find("url")
        idx_of_endof_url = to_process.find(");")
        print(to_process[idx_of_url+4:idx_of_endof_url])
