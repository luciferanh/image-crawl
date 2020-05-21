# Web crawl 
# Use  shutil, urllib , requests , bs4 , urllib.parse
import urllib.request
import shutil
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup 
def make_soup(url): 
    req = urllib.request.Request(url, headers={'User-Agent' : "Mozilla/5.0"}) #This class is an abstraction of a URL request.
    html = urllib.request.urlopen(req) # urlopen returns a bytes object
    return BeautifulSoup(html, 'html.parser') #the document is converted to Unicode, and HTML entities are converted to Unicode characters.Beautiful Soup transforms a complex HTML document into a complex tree of Python objects
def get_images(url):
    soup = make_soup(url)
    images = [img for img in soup.findAll('img')] # You cand add {"class": ".."} , if you can see and want to down these imgages in html
    print (str(len(images)) + " images found.") # How many 
    print('Downloading images to current working directory.')
    image_links = [each.get('src') for each in images] # I want to get src in title . In html , <img src=".." 
    for each in image_links:
        print(f"{each} ")
        try:
            filename = each.strip().split('/')[-1].strip() # i create a new file for a picture in my PC
            src = urljoin(url, each) # Construct a full (“absolute”) URL by combining a “base URL” (base) with another URL (url)
            print('Getting: ' , filename)
            response = requests.get(src, stream=True) #Get src to down
            with open(filename, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file) #download file
        except:
            print('An error occured. Continuing.')
    print('Done.')
get_images('http://truyentranhtam.com/kemono-giga-chap-1') # The link you want to download