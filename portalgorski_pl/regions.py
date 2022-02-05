from scrap_func import scrap_next_level
import csv

# region = region
url = 'http://topo.portalgorski.pl'

if __name__ == '__main__':

    areas = []
    with open("areas.csv", newline='', mode="r") as areas_csv:
        reader = csv.DictReader(areas_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            areas.append(row)

    raw_regions = scrap_next_level(url, areas)

    regions = []
    sectors = []
    crags = []
    for i in raw_regions:
        if 'region' in i['link']:
            regions.append(i)
        elif 'sektor' in i['link']:
            sectors.append(i)
        elif 'skala' in i['link']:
            crags.append(i)

    with open("regions.csv", newline='', mode="a") as regions_csv:
        fieldnames = ['area_name', 'name', 'link']
        writer = csv.DictWriter(regions_csv, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for region in regions:
            writer.writerow(region)

    with open("sectors.csv", newline='', mode="a") as sectors_csv:
        fieldnames = ['area_name', 'name', 'link']
        writer = csv.DictWriter(sectors_csv, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for sector in sectors:
            writer.writerow(sector)

    with open("crags.csv", newline='', mode="a") as crags_csv:
        fieldnames = ['area_name', 'name', 'link']
        writer = csv.DictWriter(crags_csv, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for crag in crags:
            writer.writerow(crag)

    print('REGIONS SCRAPING COMPLETED')
