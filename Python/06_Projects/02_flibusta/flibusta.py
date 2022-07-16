import requests
import json
from types import SimpleNamespace
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import os


def scrape(request_text):
    query_text = urllib.parse.quote(request_text)
    url_mask = "http://flibusta.is/booksearch?ask={request_str}&cha=on&chb=on"
    url = url_mask.format(request_str = query_text)
    
    r = urllib.request.urlopen(url)
    html_bytes  = r.read()
    html = html_bytes.decode("utf-8")
    parser = "html.parser"
    sp = BeautifulSoup(html, parser)

    target_div = sp.find('div', attrs={'class':'clear-block', 'id':'main'})
    target_ul = target_div.findChildren('ul', attrs={'class':''})[0]
    li_list = target_ul.find_all("li")
    first_li = li_list[0]
    link_to_first_book = first_li.a.get('href')

    book_url = "http://flibusta.is" + link_to_first_book

    response_fb2 = requests.get(book_url + '/fb2')
    response_epub = requests.get(book_url + '/epub')
    response_mobi = requests.get(book_url + '/mobi')
    response_pdf = requests.get(book_url + '/pdf')

    resp_list = [response_fb2, response_epub, response_mobi, response_pdf]
    book_id = str(link_to_first_book).replace('/b/','')

    for r in resp_list:
        if 'text' not in r.headers['Content-Type']:
            indexx = str(r.headers['content-disposition']).index('=')
            filename = r.headers['content-disposition'][indexx+1::].replace('\"','')
            full_path = os.path.join(os.getcwd(), "books", book_id, filename)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            open(os.path.join(full_path), "wb").write(r.content)

search_string = str(input())
response_2 = scrape(search_string)
