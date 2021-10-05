
from requests_html import HTMLSession
import requests
from jsonpath_ng import  parse


'''
url = "https://golden.com/query/list-of-bitcoin-companies-YXZW"
xpath_path = '//*[contains(concat( " ", @class, " " ), concat( " ", "css-xtsn96", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "legacyLink", " " ))]'
name = xpath_hfinder(url, xpath_path) 
'''


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


'''
url = "https://golden.com/query/list-of-bitcoin-companies-YXZW"

css_path = '.css-xtsn96 .legacyLink'
name = css_hfinder(url, css_path)

'''


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



"""
url = "https://golden.com/query/list-of-bitcoin-companies-YXZW"
data = css_loder(url)

css_path = '.css-xtsn96 .legacyLink'
name = phfinder(data, css_path)

xpath_path = '//*[contains(concat( " ", @class, " " ), concat( " ", "css-xtsn96", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "legacyLink", " " ))]'
name = phfinder(data, xpath_path)
"""


def css_loder(url):
    session = HTMLSession()
    r = session.get(url)
    data = r.html.find
    return data



def xpath_loder(url):
    session = HTMLSession()
    r = session.get(url)
    data = r.html.xpath
    return data



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



"""
link = 'https://golden.com/api/v1/queries/list-of-bitcoin-companies-YXZW/results/?page=1&per_page=100&order='
json_pathraw = 'results[*].description.nodes[*].nodes[*].leaves[*].text'

data = json_loder(link)

description = json_finder(data, json_pathraw)
print(description)

"""

def json_loder(url):
    r = requests.get(url)
    data = r.json()
    return data


def json_finder(data, json_path):
    input = parse(json_path)
    z = []
    for match in input.find(data):
        try:
            output = match.value
            z.append(output)
        except Exception as e:
            output  = None
            z.append(output)
    return z
