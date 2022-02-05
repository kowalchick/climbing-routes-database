from scrap_func import scrap_next_level
import csv

# sector = sektor
url = 'http://topo.portalgorski.pl'

if __name__ == '__main__':

    regions = []
    with open("regions.csv", newline='', mode="r") as regions_csv:
        reader = csv.DictReader(regions_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            regions.append(row)

    raw_sectors = scrap_next_level(url, regions)

    sectors = []
    crags = []
    other = []
    for i in raw_sectors:
        if 'sektor' in i['link']:
            sectors.append(i)
        elif 'skala' in i['link']:
            crags.append(i)
        else:
            other.append(i)

    print('OTHER THAN SECTOR AND CRAG:')
    print(other)

    with open("sectors.csv", newline='', mode="a") as sectors_csv:
        fieldnames = ['region_name', 'name', 'link']
        writer = csv.DictWriter(sectors_csv, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for sector in sectors:
            writer.writerow(sector)

    with open("crags.csv", newline='', mode="a") as crags_csv:
        fieldnames = ['region_name', 'name', 'link']
        writer = csv.DictWriter(crags_csv, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for crag in crags:
            writer.writerow(crag)

    print('SECTORS SCRAPING COMPLETED')
