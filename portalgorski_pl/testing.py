import csv


crags = []
with open("crags_test.csv", newline='', mode="r") as crags_csv:
  reader = csv.DictReader(crags_csv, delimiter=',', quotechar='', quoting=csv.QUOTE_NONE, doublequote=False, escapechar='"')
  for row in reader:
    crags.append(row)
print(crags)

areas = []
with open("areas.csv", newline='', mode="r") as areas_csv:
  reader = csv.DictReader(areas_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  for row in reader:
    areas.append(row)

print(areas)
