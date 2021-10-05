
## dsrf-finder()

### Details
 **Name                     :** dsrf_ finder
 
 **versions                 :** 0.0.1, 0.0.2, 0.0.3
 
 **Developed and created by :** Anas Bin Hasn Bhuiyan

 **Eamil                    :** dsrf.anas@gmail.com

 **Date of development      :** 30 september 2021
 #

### Functions

 #### Function 1  : xpath_hfinder
 Part 1 (import)
 ```bash
    from dsrf_finder import dsrf_finder
 ```

 Part 2 (must write)

 ```bash
    url = ''
    #example
    url = 'https://en.wikipedia.org/wiki/Bengali_novels'
 ```
 Part 3 (no need to write)
 ```bash
    #session = dsrf_finder.HTMLSession()
    #r = session.get(url)
    #data = r.html.xpath
 ```
 Part 4 (xpath)

 ```bash
   path = 'any xpath'
   #example
   path = '//*[contains(concat( " ", @class, " " ), concat( " ", "wikitable", " " ))]//td[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]'
 ```
 Part 5 (let's get the data)

 ```bash
    #rq = any name of column you want
    rq = dsrf_finder.xpath_hfinder(url, path)
    print(rq)
 ```

 Example

 ```bash
   url = "https://golden.com/query/list-of-bitcoin-companies-YXZW"
   xpath_path = '//*[contains(concat( " ", @class, " " ), concat( " ", "css-xtsn96", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "legacyLink", " " ))]'
   name = xpath_hfinder(url, xpath_path)
 ```
 ##### To know more about xpath please visit : [xpath selection](https://github.com/thedsrf/dsrf_finder/blob/main/doc/xpath.md)

 #
 #### Function 2  : css_hfinder

  Part 1 (import)
 ```bash
    from dsrf_finder import dsrf_finder
 ```
 Part 2 (must write)

  ```bash
    url = ''
    #example
    url = 'https://en.wikipedia.org/wiki/Bengali_novels'
 ```
 Part 3 (no need to write)

 ```bash
    #session = dsrf_finder.HTMLSession()
    #r = session.get(link)
    #data = r.html.find
 ```
 Part 4 (css selector)
 ```bash
   path = 'any css selector path'
   #example
   path = '.wikitable td:nth-child(2)'
 ```
 Part 5 (let's get the data)
 ```bash
    #rq = any name of column you want
    rq = dsrf_finder.css_hfinder(url, path)
    print(rq)
 ```

 Example

 ```bash
   url = "https://golden.com/query/list-of-bitcoin-companies-YXZW"
   xpath_path = '//*[contains(concat( " ", @class, " " ), concat( " ", "css-xtsn96", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "legacyLink", " " ))]'
   name = xpath_hfinder(url, xpath_path)
 ```
 ##### To know more about css selector please visit : [css selector](https://github.com/thedsrf/dsrf_finder/blob/main/doc/css%20selector.md)

 #
 #### Function 3  : phfinder, css_loader, xpath_loader


  Part 1 (import)
 ```bash
    from dsrf_finder import dsrf_finder
 ```
  Part 2 (must write)

 ```bash
    url = ''
    #example
    url = 'https://en.wikipedia.org/wiki/Bengali_novels'
 ```
  Part 3 (css or xpath)

 ```bash
   path = 'any xpath or css path'

   #example

   #css selector path
   path = '.wikitable td:nth-child(2)'

   #xpath
   path = '//*[contains(concat( " ", @class, " " ), concat( " ", "wikitable", " " ))]//td[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]'
 
 ```

  Part 4 (must write)

 ```bash
    session = dsrf_finder.HTMLSession()
    r = session.get(url)

    #if path is xpath
    data = r.html.xpath

    #if path is css selector
    data = r.html.find
 ```
 
  Part 5 (let's get the data)
 ```bash
    #rq = any name of column you want
    rq = dsrf_finder.phfinder(data, path)
    print(rq)
 ```
  Example

 ```bash
   url = "https://golden.com/query/list-of-bitcoin-companies-YXZW"
   data = css_loder(url)

   css_path = '.css-xtsn96 .legacyLink'
   name = phfinder(data, css_path)

   xpath_path = '//*[contains(concat( " ", @class, " " ), concat( " ", "css-xtsn96", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "legacyLink", " " ))]'
   name = phfinder(data, xpath_path)
 ```
 #
 #### Function 4  : json_loder, json_finder
  Example

 ```bash
   link = 'https://golden.com/api/v1/queries/list-of-bitcoin-companies-YXZW/results/?page=1&per_page=100&order='
   json_pathraw = 'results[*].description.nodes[*].nodes[*].leaves[*].text'

   data = json_loder(link)

   description = json_finder(data, json_pathraw)
   print(description)
  ```
 #
 ##### To know more about css and xpath selector please visit : [css selector](https://github.com/thedsrf/dsrf_finder/blob/main/doc/css%20selector.md) , [xpath](https://github.com/thedsrf/dsrf_finder/blob/main/doc/xpath.md)
 
 #

