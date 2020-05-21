import urllib.request
import shutil
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
def make_soup(url):
    req = urllib.request.Request(url, headers={'User-Agent' : "Mozilla/5.0"}) 
    html = urllib.request.urlopen(req)
    return BeautifulSoup(html, 'html.parser')
def get_images(url):
    soup = make_soup(url)
    images = [img for img in soup.findAll('img',)]
    print (str(len(images)) + " images found.")
    print('Downloading images to current working directory.')
    image_links = [each.get('src') for each in images]
    for each in image_links:
        print(f"{each} ")
        try:
            filename = each.strip().split('/')[-1].strip()
            src = urljoin(url, each)
            print('src ' ,  src)
            print('Getting: ' , filename)
            response = requests.get(src, stream=True)
            with open(filename, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
        except:
            print('An error occured. Continuing.')
    print('Done.')
get_images('http://truyentranhtam.com/kemono-giga-chap-1')