import csv
from shop.atomic.models import AtomicComponent, AtomicAttribute


def run():
    with open('shop/scripts/endfitting.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            print(', '.join(row))
            atom = AtomicComponent.objects.get_or_create(
                stock_code=row[3],
                part_code=row[2],
                warehouse_location=row[4],
                type=row[0]
            )
            AtomicAttribute.objects.get_or_create(
                atomic_component=atom[0],
                key='Thread size',
                value=row[9]
            )
            AtomicAttribute.objects.get_or_create(
                atomic_component=atom[0],
                key='Outer Comp.Factor',
                value=row[11]
            )

