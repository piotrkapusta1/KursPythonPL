import os 
import urllib.request

data_dir = r"C:/Users/piotr.kapusta/Desktop/Python programs/Python kurs PL/Section 2/DataToLAB6/"

pages = [

    { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},

    { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'} ]

for page in pages:

    try:
        
        path = page.get("name") + ".html"
        print("Processing: {}  => {} ...".format(page["url"], path))
        urllib.request.urlretrieve(page.get("url"), data_dir + path )
        # print (path)
    except NameError:
        print( NameError)
else:
    print("All webs downloaded")
