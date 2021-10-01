#dsrf_ finder
#version: 1.0.1
#developed and created by: Anas Bin Hasn Bhuiyan
#EMAIL : dsrf.anas@gmail.com
#Date of development: 30 september 2021

from requests_html import HTMLSession


#function 1

def hfinder(link, path):

    session = HTMLSession()
    r = session.get(link)
    x = r.html.xpath(path)
    z = []
    k = []
    for item in (x):
        try:
            x = item.text
            z.append(x)
        except Exception as e:
            x = item
            z.append(x)
        try:
            x = item.attrs['href']
            k.append(x)
        except Exception as e:
            x = None
            k.append(x)
    return z, k


#function 2

def phfinder(x, y):
    x = x(y)
    
    z = []
    k = []
    for item in (x):
        try:
            x = item.text
            z.append(x)
        except Exception as e:
            x = item
            z.append(x)
        try:
            x = item.attrs['href']
            k.append(x)
        except Exception as e:
            x = None
            k.append(x)
    return z, k
