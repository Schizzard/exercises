from msilib.schema import Class
import urllib.request
from bs4 import BeautifulSoup

class Scrapper:
    def __init__(self, site) -> None:
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all('a'):
            url = tag.get('href')
            if url is None or url.startswith('./'):
                continue
            if 'html' in url:
                print('\n' + url)
            print('\n' + url)

site  = 'https://news.google.com/'
Scrapper(site).scrape()