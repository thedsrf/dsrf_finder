
from requests_html import HTMLSession


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
