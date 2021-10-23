from TestingManyPages import *
from DataStorage import *
from processingByJSContent import *

import numpy as np
import pandas as pd

# Think there is a better way to construct the URL using requests
#   each partNumber and partId is unique to the product, this is all we will need to change
#   Base url will be the same
#   Thinking we store products in a dict with k: str productName v: tuple partNumber, partId
partNumber = 91615
partId = 119264
products_to_scrape = {"multivitamin peanut butter flavored..etc": (91615, 119264)


                      }

if __name__ == '__main__':
    rootURL = "https://www.chewy.com/app/product-reviews/rel" \
                     "oad?partNumber=" + str(partNumber) + "&id=" + str(partId) + "&reviewSort=NEWEST&reviewFilter=ALL_STARS&" \
                                                                             "pageNumber="
    #load_media(rootURL)


    for key in products_to_scrape:
        partNumber, partId = products_to_scrape[key]
        rootURL = "https://www.chewy.com/app/product-reviews/rel" \
                "oad?partNumber=" + str(partNumber) + "&id=" + str(partId) + "&reviewSort=NEWEST&reviewFilter=ALL_STARS&" \
                                                                            "pageNumber="
        print(key)
        load_data(rootURL)



