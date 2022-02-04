from scrap_func import get_routes_lst, routes_det_scrapping, route_det_digesting
import csv

main_url = 'https://wspinanie.pl/topo2'

if __name__ == '__main__':

    # read crags from file
    # remove crag height as it is average crag height and routes differ in height
    crags = []
    with open("./database/05_crags.csv", mode="r", encoding='UTF-8') as crags_csv:
        reader = csv.DictReader(crags_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, doublequote=True)
        for row in reader:
            row.pop('height')
            crags.append(row)

    print(crags[1])