from scrap_func import get_subsequent_lst
import csv

main_url = 'https://wspinanie.pl/topo2'

if __name__ == '__main__':

    # read regions list from file
    regions = []
    with open("./database/01_regions.csv", mode="r", encoding='UTF-8') as regions_csv:
        reader = csv.DictReader(regions_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, doublequote=True)
        for row in reader:
            regions.append(row)

    # get subregions list
    items = get_subsequent_lst(main_url, regions)

    # check for unordered crags in list and append items to adequate list
    subregions = []
    crags = []
    for item in items:
        if 'skala' in item['link']:
            link = item.pop('link')
            new_item = item.pop('new_item')
            item.update({'region_name': f'{new_item}', 'sector_name': f'{new_item}', 'group_name': f'{new_item}',
                         'new_item': f'{new_item}', 'link': f'{link}'})
            crags.append(item)
        else:
            subregions.append(item)

    # write subregions to file
    with open("./database/02_subregions.csv", newline='', mode="a", encoding='UTF-8') as subregions_csv:
        fieldnames = ['country', 'region_name', 'new_item', 'link']
        writer = csv.DictWriter(subregions_csv, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, doublequote=True)
        for subregion in subregions:
            writer.writerow(subregion)

    # write unordered crags to file
    with open("./database/05_crags_in_regions.csv", newline='', mode="a", encoding='UTF-8') as crags_csv:
        fieldnames = ['country', 'region_name', 'subregion_name', 'sector_name', 'group_name', 'new_item', 'link']
        writer = csv.DictWriter(crags_csv, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, doublequote=True)
        for crag in crags:
            writer.writerow(crag)

    print('SUBREGIONS SCRAPING COMPLETED')
