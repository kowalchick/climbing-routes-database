from scrap_func import get_subsequent_lst
import csv

main_url = 'https://wspinanie.pl/topo2'

if __name__ == '__main__':

    # read subregions from file
    subregions = []
    with open("./database/02_subregions.csv", mode="r", encoding='UTF-8') as subregions_csv:
        reader = csv.DictReader(subregions_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, doublequote=True)
        for row in reader:
            subregions.append(row)

    # get sectors list
    items = get_subsequent_lst(main_url, subregions)

    # check for unordered crags in list and append items to adequate list

    sectors = []
    crags = []
    for item in items:
        if 'skala' in item['link']:
            link = item.pop('link')
            new_item = item.pop('new_item')
            item.update({'sector_name': f'{new_item}', 'group_name': f'{new_item}', 'new_item': f'{new_item}', 'link': f'{link}'})
            crags.append(item)
        else:
            sectors.append(item)

    # write sectors to file
    with open("./database/03_sectors.csv", newline='', mode="a", encoding='UTF-8') as sectors_csv:
        fieldnames = ['country', 'region_name', 'subregion_name', 'new_item', 'link']
        writer = csv.DictWriter(sectors_csv, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, doublequote=True)
        for sector in sectors:
            writer.writerow(sector)

    # write unordered crags to file
    with open("./database/05_unordered_crags.csv", newline='', mode="a", encoding='UTF-8') as crags_csv:
        fieldnames = ['country', 'region_name', 'subregion_name', 'sector_name', 'group_name', 'new_item', 'link']
        writer = csv.DictWriter(crags_csv, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, doublequote=True)
        for crag in crags:
            writer.writerow(crag)

    print('SECTORS SCRAPING COMPLETED')
