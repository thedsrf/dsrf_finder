
from dsrf_finder import  dsrf_finder

url = 'https://en.wikipedia.org/wiki/Bengali_novels'
path = '//*[contains(concat( " ", @class, " " ), concat( " ", "wikitable", " " ))]//td[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]'

#rq = any name of column you want

rq = dsrf_finder.xpath_hfinder(url, path)

print(rq)
