import csv
from shop.atomic.models import AtomicComponent


def run():
    with open('shop/scripts/endfitting.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            print(', '.join(row))
            AtomicComponent.objects.create(
                stock_code=row[3],
                part_code=row[2],
                warehouse_location=row[4]
            )
