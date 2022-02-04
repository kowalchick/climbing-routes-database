from scrap_func import get_subsequent_lst, get_adhoc_lst, crag_det_scrapping, crag_det_digesting
import csv

main_url = 'https://wspinanie.pl/topo2'

if __name__ == '__main__':

    #  read groups list
    groups = []
    with open("./database/04_groups.csv", mode="r", encoding='UTF-8') as groups_csv:
        reader = csv.DictReader(groups_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, doublequote=True)
        for row in reader:
            groups.append(row)

    # get crag lists from groups
    items = get_subsequent_lst(main_url, groups)

    # check if all items are crags
    crags = []
    subgroups = []
    for item in items:
        if 'skala' in item['link']:
            crags.append(item)
        else:
            subgroups.append(item)

    # first it was checked manually, if appending is logically adequate to replace subgroup name with crag name
    # get crag list from subgroups
    items2 = get_adhoc_lst(main_url, subgroups)
    for item in items2:
        crags.append(item)

    # read unordered crags from file
    unordered_crags = []
    with open("./database/05_unordered_crags.csv", mode="r", encoding='UTF-8') as groups_csv:
        fieldnames = ['country', 'region_name', 'subregion_name', 'sector_name', 'group_name', 'new_item', 'link']
        reader = csv.DictReader(groups_csv, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, doublequote=True)
        for row in reader:
            unordered_crags.append(row)

    # append unordered crags scrapped in previous levels
    # omit first row (headers) because fieldnames were specified in DictReader to match scraped data
    for crag in unordered_crags[1:]:
        crags.append(crag)

    # get crags details
    for crag in crags:
        details = crag_det_digesting(crag_det_scrapping(crag.get('link')))
        crag.update({'rock_type': details[0], 'height': details[1], 'geo': details[3], 'exposure': details[4]})

    # write crags list and details to new file
    with open("./database/05_crags.csv", newline='', mode="a", encoding='utf-8') as crags_csv:
        fieldnames = ['country', 'region_name', 'subregion_name', 'sector_name', 'group_name', 'new_item', 'link' ,'rock_type', 'height', 'geo', 'exposure']
        writer = csv.DictWriter(crags_csv, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, doublequote=True)
        for crag in crags:
            writer.writerow(crag)

    print('CRAGS SCRAPING COMPLETED')
