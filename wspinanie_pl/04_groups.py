from scrap_func import get_subsequent_lst
import csv

main_url = 'https://wspinanie.pl/topo2'

if __name__ == '__main__':

    # read sectors from file
    sectors = []
    with open("./database/03_sectors.csv", mode="r", encoding='UTF-8') as sectors_csv:
        reader = csv.DictReader(sectors_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, doublequote=True)
        for row in reader:
            sectors.append(row)

    # get groups list
    items = get_subsequent_lst(main_url, sectors)

    # check for unordered crags in list and append items to adequate list

    groups = []
    crags = []
    for item in items:
        if 'skala' in item['link']:
            link = item.pop('link')
            new_item = item.pop('new_item')
            item.update({'group_name': f'{new_item}', 'new_item': f'{new_item}', 'link': f'{link}'})
            crags.append(item)
        else:
            groups.append(item)

    # write groups to file
    with open("./database/04_groups.csv", newline='', mode="a", encoding='UTF-8') as groups_csv:
        fieldnames = ['country', 'region_name', 'subregion_name', 'sector_name', 'new_item', 'link']
        writer = csv.DictWriter(groups_csv, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, doublequote=True)
        for group in groups:
            writer.writerow(group)

    # write unordered crags to file
    with open("./database/05_unordered_crags.csv", newline='', mode="a", encoding='UTF-8') as crags_csv:
        fieldnames = ['country', 'region_name', 'subregion_name', 'sector_name', 'group_name', 'new_item', 'link']
        writer = csv.DictWriter(crags_csv, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, doublequote=True)
        for crag in crags:
            writer.writerow(crag)

    print('GROUPS SCRAPING COMPLETED')
