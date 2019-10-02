import csv


def run():
    with open('shop/scripts/endfitting.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            print(', '.join(row))
