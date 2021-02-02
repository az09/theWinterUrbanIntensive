import requests
import lxml
from bs4 import BeautifulSoup
import re

base_url = 'https://www.bustime.ru'
city = 'nizhniy-novgorod'
dt = '2021-01-29'
bus_id = 0 #8013
url = '%s/%s/transport/%s/?bus_id=%d' % (base_url, city, dt, bus_id)
#r = '<div class="ui grid" style="margin-top:1em"><div class="column"><div class="ui pagination right menu"><a class="active item" href="/nizhniy-novgorod/transport/2021-01-21/page-1">1</a><a class="item" href="/nizhniy-novgorod/transport/2021-01-21/page-2">2</a><a class="item" href="/nizhniy-novgorod/transport/2021-01-21/page-3">3</a><a class="item" href="/nizhniy-novgorod/transport/2021-01-21/page-4">4</a><a class="item" href="/nizhniy-novgorod/transport/2021-01-21/page-5">5</a><a class="item" href="/nizhniy-novgorod/transport/2021-01-21/page-6">6</a><a class="item" href="/nizhniy-novgorod/transport/2021-01-21/page-7">7</a><a class="item" href="/nizhniy-novgorod/transport/2021-01-21/page-8">8</a><a class="item" href="/nizhniy-novgorod/transport/2021-01-21/page-9">9</a><a class="item" href="/nizhniy-novgorod/transport/2021-01-21/page-10">10</a><a class="item" href="/nizhniy-novgorod/transport/2021-01-21/page-11">11</a><a class="item" href="/nizhniy-novgorod/transport/2021-01-21/page-12">12</a><a class="item" href="/nizhniy-novgorod/transport/2021-01-21/page-13">13</a><a class="item" href="/nizhniy-novgorod/transport/2021-01-21/page-14">14</a><a class="item" href="/nizhniy-novgorod/transport/2021-01-21/page-15">15</a><a class="item" href="/nizhniy-novgorod/transport/2021-01-21/page-16">16</a><a class="item" href="/nizhniy-novgorod/transport/2021-01-21/page-17">17</a><a class="item" href="/nizhniy-novgorod/transport/2021-01-21/page-18">18</a><a class="item" href="/nizhniy-novgorod/transport/2021-01-21/page-19">19</a><a class="item" href="/nizhniy-novgorod/transport/2021-01-21/page-20">20</a><a class="item" href="/nizhniy-novgorod/transport/2021-01-21/page-21">21</a><a class="item" href="/nizhniy-novgorod/transport/2021-01-21/page-22">22</a><a class="item" href="/nizhniy-novgorod/transport/2021-01-21/page-23">23</a><a class="item" href="/nizhniy-novgorod/transport/2021-01-21/page-24">24</a><a class="item" href="/nizhniy-novgorod/transport/2021-01-21/page-25">25</a><a class="item" href="/nizhniy-novgorod/transport/2021-01-21/page-26">26</a></div></div></div>'
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
#print(soup.prettify())
# марштуты в этот день
"""
m = soup.find('select', {'name': 'bus_id'})
#print(m, type(m))
with open('select.txt', 'w') as output_file:
    for opt in m:
        if opt['value'] != "0":
            output_file.write(opt['value']+'\t'+opt.text+'\n')
"""

def soup2head(s):
    spans = s.find_all('span', {'id': 'head'})
    res = []
    rex = re.compile(r'\/%s\/transport\/%s\/(\S*)\/' % (city, dt), flags=0)
    for span in spans:
        a = span.find('a')
        res.append({'id': rex.search(a.get('href'))[1], 'reg_num': a.text})
    return res

# .pagination
pages = soup.find('div', {'class': 'ui pagination right menu'}).find_all('a')
if pages is not None:
    #print(pages.prettify())
    # сэкономим на том, что первая уже загружена
    print(pages[0].get('href'))
    # if 1 == len(pages):
    #     print(pages[0].get('href'))
    # else:
    #     for a in pages[1:]::
    #         print(base_url + a.get('href'))
    heads = soup2head(soup)
    for head in heads:
        print(head)
    print(len(heads))