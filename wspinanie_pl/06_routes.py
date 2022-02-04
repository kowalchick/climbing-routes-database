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

    # get routes list from crags
    routes = get_routes_lst(main_url, crags)

    # get routes details
    for route in routes:
        details = route_det_digesting(routes_det_scrapping(route.get('link')))
        route.update({'grade': details[0], 'height': details[1], 'pitches': details[2], 'bolts': details[3], 'anchor': details[4], 'type': details[5], 'steepness': details[6]})

    # write routes list and details to file
    with open("./database/06_routes.csv", newline='', mode="a", encoding='UTF-8') as routes_csv:
        fieldnames = ['country', 'region_name', 'subregion_name', 'sector_name', 'group_name', 'crag_name', 'new_item', 'rock_type', 'geo', 'exposure', 'link', 'grade', 'height', 'pitches', 'bolts', 'anchor', 'type', 'steepness']
        writer = csv.DictWriter(routes_csv, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, doublequote=True)
        for route in routes:
            if route:
                writer.writerow(route)

    print('ROUTES SCRAPING COMPLETED')
