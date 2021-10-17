from requestingPage import *
from TestingManyPages import *
import numpy as np
import pandas as pd

# Think there is a better way to construct the URL using requests
#   each partNumber and partId is unique to the product, this is all we will need to change
#   Base url will be the same
#   Thinking we store products in a dict with k: str productName v: tuple partNumber, partId
partNumber = 91615
partId = 119264
rootURL = "https://www.chewy.com/app/product-reviews/rel" \
          "oad?partNumber=" + str(partNumber) + "&=" + str(partId) + "&reviewSort=NEWEST&reviewFilter=ALL_STARS&" \
          "pageNumber="


if __name__ == '__main__':
    # pullPage()
    page = 1
    maxPages = 1
    while page <= int(maxPages):

        currPage = "https://www.chewy.com/app/product-reviews/rel" \
          "oad?partNumber=91615&id=119264&reviewSort=NEWEST&reviewFilter=ALL_STARS&pageNumber=" + str(page)
        print("Page: " + str(page))
        print("_____________________________________________")
        pull_pages(currPage)
        print("\n")
        #maxPages = get_number_of_pages(currPage)

        # iterating
        maxPages = get_number_of_pages(currPage)
        page += 1



#requestingPage.pullPage()
