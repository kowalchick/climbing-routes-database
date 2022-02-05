from scrap_func import lst_scraping, initial_digesting
import csv

# area = obszar
url = 'http://topo.portalgorski.pl'
areas_raw = lst_scraping(url)
areas = initial_digesting(url, areas_raw)

if __name__ == '__main__':
    with open("areas.csv", newline='', mode="a") as areas_csv:
        fieldnames = ['country', 'name', 'link']
        writer = csv.DictWriter(areas_csv, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for area in areas:
            writer.writerow(area)
        print('AREAS SCRAPING COMPLETED')
