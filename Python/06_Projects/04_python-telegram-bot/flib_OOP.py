import requests
import json
from types import SimpleNamespace
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import os

formats = ['fb2', 'epub', 'mobi', 'pdf']
site = 'http://flibusta.is'

# TODO:(Превратить в ООП добавить класс Book)

def get_page(url):
    r = urllib.request.urlopen(url)
    html_bytes  = r.read()
    html = html_bytes.decode("utf-8")
    parser = "html.parser"
    soup = BeautifulSoup(html, parser)
    return soup


def scrape_books(request_text):
    query_text = urllib.parse.quote(request_text)
    url_mask = "http://flibusta.is/booksearch?ask={request_str}&cha=on&chb=on"
    url = url_mask.format(request_str = query_text)
    
    sp = get_page(url)

    target_div = sp.find('div', attrs={'class':'clear-block', 'id':'main'})
    target_ul = target_div.findChildren('ul', attrs={'class':''})[0]
    li_list = target_ul.find_all("li")


    link_list = [a for a in (("http://flibusta.is" + l.a.get('href') + '/') for l in li_list)]
    title_list = [b for b in (l.text for l in li_list)]
    book_id_list = [str(l.a.get('href')).replace('/b/','') for l in li_list]
    
    # book_list = json.dumps([(i, t, l) for (i, t, l) in zip(book_id_list, title_list, link_list)])

    d={} 
    for i in range(len(book_id_list)):
        d[i] = {"id":book_id_list[i],"content":{}}
        d[i]["content"] = {'title': title_list[i], "url": link_list[i], "formats": {}, "cover": {}}

    books_j = json.dumps(d)
    return books_j # DONE: 1

def get_book_by_id(id):
    book_url = site + '/' + id
    sp = get_page(book_url)
    target_div = sp.find('div', attrs={'class':'clear-block', 'id':'main'})
    target_h1 = target_div.find('h1', attrs={'class': 'title'})
    title = target_h1.text
    cover = 1
    formats = 1
    

def get_book_formats(book_url):
    available_formats = []
    for f in formats:
        resp_h = requests.head(book_url + f)
        if resp_h.status_code == 302:
            available_formats.append(f)
    return available_formats


def get_book_formats_urls(book_j):
    book = json.loads(book_j)
    book_url = book['content']['url']

    avbl_formats = get_book_formats(book_url)
    avbl_formats_urls = [book_url + format for format in avbl_formats]

    book['content']['formats'] = {f:l for (f,l) in zip(avbl_formats, avbl_formats_urls)}
    book_j = json.dumps(book)
    return book_j 


def get_book_cover_link(book_j):
    book = json.loads(book_j)
    book_url = book['content']['url']

    sp = get_page(book_url)
    target_div = sp.find('div', attrs={'class':'clear-block', 'id':'main'})
    target_img = target_div.find('img', attrs={'alt':'Cover image'})
    src = target_img.get('src')
    img_link = site + src

    book['content']['cover']['url'] = img_link
    book_j = json.dumps(book)
    return book_j 


def download_book(book_j, format):
    book = json.loads(book_j)
    
    book_id = book['id']
    book_url = book['content']['formats'][format]
    cover_url = book['content']['cover']['url']

    b_response = requests.get(book_url)

    indexx = str(b_response.headers['content-disposition']).index('=')
    b_filename = b_response.headers['content-disposition'][indexx+1::].replace('\"','')
    if b_filename.endswith('.fb2.zip'):
        b_filename = b_filename.removesuffix('.zip')

    b_full_path = os.path.join(os.getcwd(), "books", book_id, b_filename)
    os.makedirs(os.path.dirname(b_full_path), exist_ok=True)
    open(os.path.join(b_full_path), "wb").write(b_response.content)

    c_response = requests.get(cover_url)
    c_full_path = os.path.join(os.getcwd(), "books", book_id, 'cover.jpg')
    open(os.path.join(c_full_path), "wb").write(c_response.content)

    
def main():
    print("Введите название книги (без автора)")
    search_string = str(input())
    books_j = scrape_books(search_string)
    books = json.loads(books_j)

    print('Выберите книгу (номер)')
    for i in range(len(books)):
        print(str(i) + ' : ' + books[str(i)]["content"]['title'])

    chosen_book_n = str(input())

    book = books[chosen_book_n]
    book_j = json.dumps(book)
    book_j = get_book_formats_urls(book_j)
    book_j = get_book_cover_link(book_j)


    print('Выберите формат (ввести строкой)')
    chosen_format = str(input())

    download_book(book_j, chosen_format)
    pass

if __name__ == '__main__':
    main()