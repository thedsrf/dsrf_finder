#dsrf_ finder
#version: 1.0.1
#developed and created by: Anas Bin Hasn Bhuiyan
#EMAIL : dsrf.anas@gmail.com
#Date of development: 30 september 2021

from requests_html import HTMLSession


#function 1

""" 
!no need to write this for xpath_hfinder

session = HTMLSession()
    #r = session.get(link)
    #data = r.html.xpath(xpath) (if path is xpath)
#path = 'any path css or xpath

"""

def xpath_hfinder(link, xpath):

    session = HTMLSession()
    r = session.get(link)
    x = r.html.xpath(xpath)
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

""" 
# !no need to write this for css_hfinder

session = HTMLSession()
    r = session.get(link)
    data = r.html.find(css_path) (if path is css)
path = 'any css path'

"""

def css_hfinder(link, css_path):
    session = HTMLSession()
    r = session.get(link)
    x = r.html.find(css_path)
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



#function 3

"""session = HTMLSession()
   r = session.get(link)
   data = r.html.find(css_path) (if path is css)
or,
   data = r.html.xpath(xpath) (if path is xpath)
path = 'any path css or xpath'
"""

def phfinder(data, path):
    x = data(path)
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
