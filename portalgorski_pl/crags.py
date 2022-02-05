from scrap_func import scrap_next_level
import csv

# crag = skala
url = 'http://topo.portalgorski.pl'

if __name__ == '__main__':

    sectors = []
    with open("sectors.csv", newline='', mode="r") as sectors_csv:
        reader = csv.DictReader(sectors_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            sectors.append(row)
    # print(sectors)

    sectors_status = []
    with open("sectors_status.csv", newline='', mode="r") as status_csv:
        reader = csv.DictReader(status_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for row in reader:
            sectors_status.append(row)
    # print(sectors_status)

    for sector in sectors:
        region_name = sector.get('region_name')
        sector_name = sector.get('sector_name')
        if not any(d['sector_name'] == sector_name for d in sectors_status):
            crags = scrap_next_level(url, [sector])

            with open("crags.csv", newline='', mode="a") as crags_csv:
                fieldnames = ['sector_name', 'name', 'link']
                writer = csv.DictWriter(crags_csv, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
                for crag in crags:
                    writer.writerow(crag)

            with open("sectors_status.csv", newline='', mode="a") as status_csv:
                writer = csv.writer(status_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
                writer.writerow([region_name, sector_name, 'completed'])

            print(f'CRAGS FROM REGION {region_name} SECTOR {sector_name} SCRAPING COMPLETED')
        else:
            continue
