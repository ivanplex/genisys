import csv


with open('ext/endfitting.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        print(', '.join(row))
