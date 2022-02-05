from scrap_func import crag_details_scrapping,crag_details_digesting
import csv

if __name__ == '__main__':

    crags = []
    with open("crags.csv", newline='', mode="r") as crags_csv:
        reader = csv.DictReader(crags_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            crags.append(row)

    #crags_details = []
    for crag in [crags[0]]:
        print(crag)
        details = crag_details_digesting(crag['crag_name'], crag_details_scrapping(crag['link']))
        #crags_details.append(details)

        with open("crags_details.csv", newline='', mode="a") as crags_details_csv:
            fieldnames = ['crag_name', 'geo', 'rock', 'no_routes', 'height', 'formations', 'walk', 'kids', 'surrounding']
            writer = csv.DictWriter(crags_details_csv, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            writer.writerow(details)

        print('CRAG {0} DETAILS SCRAPPING COMPLETED'.format(crag['crag_name']))

