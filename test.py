import gumtreescraper
from gumtreescraper import SearchListing
from gumtreescraper import SearchAd
search = SearchListing()
searchResult = search.doSearch()
print (searchResult)

for i in searchResult:
    ad = SearchAd(i.url)
    ad.parsAd()
    print(i)



