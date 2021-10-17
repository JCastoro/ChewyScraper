from requestingPage import *
from TestingManyPages import *
import pandas

if __name__ == '__main__' :
    # pullPage()
    for page in range(0, 7):
        currPage = "https://www.chewy.com/app/product-reviews/rel" \
          "oad?partNumber=91615&id=119264&reviewSort=NEWEST&reviewFilter=ALL_STARS&pageNumber=" + str(page)
        print("Page: " + str(page))
        print("_____________________________________________")
        pull_pages(currPage)
        print("\n")



#requestingPage.pullPage()
