import requests
from bs4 import BeautifulSoup
import unicodedata

# general list scrapping


def lst_scraping(url):
    headers = {'user-agent': 'my-app/0.0.1'}
    raw_lst = []
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    raw_lst += soup.select('.leaf > a')
    return raw_lst


# initial level (areas) list digesting


def initial_digesting(url, lst_raw):
    url_lst = []
    for i in lst_raw:
        name = i.getText()
        link = i.get('href')
        url_lst.append({'country': 'Polska', 'name': name, 'link': f'{url}{link}'})
    return url_lst


# next levels' list digesting


def subsequent_digesting(url, lst_raw, pass_name):
    url_lst = []
    for i in lst_raw:
        name = i.getText()
        link = i.get('href')
        url_lst.append({f'{pass_name[1][0]}': f'{pass_name[1][1]}', 'name': name, 'link': f'{url}{link}'})
    return url_lst


# next levels' list scraping & digesting


def scrap_next_level(url, previous_level):
    nxt_lvl_lst = []
    for i in previous_level:
        pass_name = list(i.items())
        lst_raw = lst_scraping(i['link'])
        i_lst = subsequent_digesting(url, lst_raw, pass_name)
        nxt_lvl_lst.extend(i_lst)
    return nxt_lvl_lst


# crag details scrapping

def crag_details_scrapping(url):
    raw_details = []
    headers = {'user-agent': 'my-app/0.0.1'}
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    raw_details += soup.select('td .data')
    return raw_details


# crag details digesting


def crag_details_digesting(crag_name, raw_details):
    crag_details = {
        'crag_name': crag_name,
        'geo': raw_details[0].getText(strip=True).replace("\n                                    , \n                                    ",","),
        'rock': raw_details[1].getText(),
        'no_routes': raw_details[2].getText(),
        'height': raw_details[3].getText(),
        'formations': raw_details[5].getText(strip=True).replace("\xa0 \n                                                                        ",","),
        'walk': raw_details[6].getText(),
        'kids': raw_details[7].getText(strip=True),
        'surrounding': raw_details[8].getText()
    }
    return crag_details



