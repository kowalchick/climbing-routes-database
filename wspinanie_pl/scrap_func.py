import requests
from bs4 import BeautifulSoup

# general list scrapping


def lst_scraping(url):
    headers = {'user-agent': 'my-app/0.0.1'}
    raw_lst = []
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    raw_lst += soup.select('.nazwa_big')
    return raw_lst


# initial level (areas) list digesting


def initial_digesting(url, lst_raw):
    url_lst = []
    for i in lst_raw:
        name = i.getText()
        link = i.get('href')
        url_lst.append({'country': 'Polska', 'region_name': name, 'link': f'{url}/{link}'})
    return url_lst


# subsequent levels' list digesting


def subsequent_digesting(url, lst_raw, prev_dict):
    url_lst = []
    for i in lst_raw:
        new_dict = {}
        name = i.getText()
        link = i.get('href')
        new_dict.update(prev_dict)
        new_dict.pop('link')
        new_dict.update({'new_item': name, 'link': f'{url}/{link}'})
        url_lst.append(new_dict)
    return url_lst


# subsequent levels' list scraping & digesting


def get_subsequent_lst(url, previous_level_dict):
    nxt_lvl_lst = []
    for i in previous_level_dict:
        prev_dict = i
        lst_raw = lst_scraping(i['link'])
        i_lst = subsequent_digesting(url, lst_raw, prev_dict)
        nxt_lvl_lst.extend(i_lst)
    return nxt_lvl_lst

# adhoc additional levels list digesting


def adhoc_lst_digesting(url, lst_raw, prev_dict):
    url_lst = []
    for i in lst_raw:
        new_dict = {}
        name = i.getText()
        link = i.get('href')
        new_dict.update(prev_dict)
        new_dict.pop('link')
        new_dict.pop('new_item')
        new_dict.update({'new_item': name, 'link': f'{url}/{link}'})
        url_lst.append(new_dict)
    return url_lst


# adhoc levels' list scraping & digesting


def get_adhoc_lst(url, previous_level_dict):
    nxt_lvl_lst = []
    for i in previous_level_dict:
        prev_dict = i
        lst_raw = lst_scraping(i['link'])
        i_lst = adhoc_lst_digesting(url, lst_raw, prev_dict)
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


# crag details

def crag_det_scrapping(url):
    raw_det = []
    counter = []
    headers = {'user-agent': 'my-app/0.0.1'}
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    # collect all <tr> on page in order to adjust the select methods
    counter += soup.select('.podtable_topo > tr')
    if len(counter) == 6:
        raw_det += soup.select('.podtable_topo > tr > td + td')
        raw_det += soup.select('.podtable_topo > tr:nth-child(5)')
    elif len(counter) == 7:
        raw_det += soup.select('.podtable_topo > tr:nth-child(n+2) > td + td')
        raw_det += soup.select('.podtable_topo > tr:nth-child(6)')
    raw_det += soup.select('.nazwa_sektora')
    return raw_det


def crag_det_digesting(raw_det):
    details = []
    for i in raw_det:
        value = i.getText().strip()
        details.append(value)
    return details


# ROUTES list scrapping


def routes_lst_scrapping(url):
    headers = {'user-agent': 'my-app/0.0.1'}
    raw_lst = []
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    raw_lst += soup.select('.ranking_row_droga > td > a')
    return raw_lst


def routes_lst_digesting(url, lst_raw, prev_dict):
    url_lst = []
    for i in lst_raw:
        new_dict = {}
        name = i.getText()
        link = i.get('href')
        new_dict.update(prev_dict)
        new_dict.pop('link')
        new_dict.update({'new_item': name, 'link': f'{url}/{link}'})
        url_lst.append(new_dict)
    return url_lst


def get_routes_lst(url, crags):
    routes_lst = []
    for i in crags:
        prev_dict = i
        lst_raw = routes_lst_scrapping(i['link'])
        i_lst = routes_lst_digesting(url, lst_raw, prev_dict)
        routes_lst.extend(i_lst)
    return routes_lst


# ROUTES details scraping

def routes_det_scrapping(url):
    raw_det = []
    counter = []
    headers = {'user-agent': 'my-app/0.0.1'}
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    counter += soup.select('.topo_skaly > tr > .sektor + td > .podtable_topo > tr')
    if len(counter) == 6:
        raw_det += soup.select('.topo_skaly > tr > .sektor + td > .podtable_topo > tr:nth-child(n+2) > td + td')
    elif len(counter) == 5:
        raw_det += soup.select('.topo_skaly > tr > .sektor + td > .podtable_topo > tr > td + td')
    raw_det += soup.select('.sektor')
    return raw_det


def route_det_digesting(raw_det):
    details = []
    for i in raw_det:
        value = i.getText().strip()
        details.append(value)
    split_elem = details[5].split('\n\r\n                        ')
    details.pop(5)
    details.extend(split_elem)
    return details

