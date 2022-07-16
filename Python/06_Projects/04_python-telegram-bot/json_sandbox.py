import json

book_id_list = [100, 200, 300]
title_list = ['aaa', 'bbb', 'ccc']
link_list = ['link1', 'link2', 'link3']


# my_list = [(i, t, l) for (i, t, l) in zip(book_id_list, title_list, link_list)]

# d = {'0': {"id": "id_of_book", "content": {}}}
# d['0']['content'] = {'title': 'title1', "link": "http://blabla",
#                      "formats": {}, "cover": "link_to_cover"}

d={}
for i in range(len(book_id_list)):
    d[i] = {"id":book_id_list[i],"content":{}}
    d[i]["content"] = {'title': title_list[i], "link": link_list[i], "formats": {}, "cover": ""}




j_str = json.dumps(d)
p_obj = json.loads(j_str)

avbl_formats = ['fb2', 'epub', 'mobi', 'pdf']
avbl_formats_urls = ['url1', 'url2', 'url3', 'url4']
p_obj['0']['content']['formats'] = {f:l for (f,l) in zip(avbl_formats, avbl_formats_urls)}
pass
