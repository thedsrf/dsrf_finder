import dsrf_finder

link = 'https://en.wikipedia.org/wiki/List_of_chapters_in_the_Quran'
sura_name = '//*[@id="mw-content-text"]/div[1]/table/tbody/tr[*]/td[2]/a'

session = dsrf_finder.HTMLSession()
r = session.get(link)
x = r.html.xpath

#by function 1(hfinder)

name = dsrf_finder.hfinder(link, sura_name)
print(name)
print(name[0])
print(name[1])

#by function 2(phfinder)

name = dsrf_finder.phfinder(x, sura_name)
print(name)
print(name[0])
print(name[1])