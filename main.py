from TestingManyPages import *
from DataStorage import *

import numpy as np
import pandas as pd

# Think there is a better way to construct the URL using requests
#   each partNumber and partId is unique to the product, this is all we will need to change
#   Base url will be the same
#   Thinking we store products in a dict with k: str productName v: tuple partNumber, partId
partNumber = 91615
partId = 119264
products_to_scrape = {"multivitamin peanut butter flavored..etc": (91615, 119264),


                      }

rootURL = "https://www.chewy.com/app/product-reviews/rel" \
          "oad?partNumber=" + str(partNumber) + "&=" + str(partId) + "&reviewSort=NEWEST&reviewFilter=ALL_STARS&" \
          "pageNumber="


if __name__ == '__main__':
    load_data()



#requestingPage.pullPage()
