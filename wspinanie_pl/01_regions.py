from scrap_func import lst_scraping, initial_digesting
import csv

url = 'https://wspinanie.pl/topo2/page,topo-kraj,kraj,6.html'
main_url = 'https://wspinanie.pl/topo2'

if __name__ == '__main__':

    # get regions list
    regions_raw = lst_scraping(url)
    regions = initial_digesting(main_url, regions_raw)

    # write regions list to file
    with open("./database/01_regions.csv", newline='', mode="a", encoding='UTF-8') as regions_csv:
        fieldnames = ['country', 'region_name', 'link']
        writer = csv.DictWriter(regions_csv, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, doublequote=True)
        for region in regions:
            writer.writerow(region)

    print('REGIONS SCRAPING COMPLETED')
