import csv
from shop.atomic.models import AtomicComponent, AtomicAttribute, AtomicGroup


def run():

    endfittings = []

    with open('shop/scripts/endfitting.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            print(', '.join(row))
            atom = AtomicComponent.objects.get_or_create(
                stock_code=row[3],
                description=row[2],
                warehouse_location=row[4],
                category=row[0]
            )[0]
            endfittings.append(atom)
            AtomicAttribute.objects.get_or_create(
                atomic_component=atom,
                key='Thread size',
                value=row[9]
            )
            AtomicAttribute.objects.get_or_create(
                atomic_component=atom,
                key='Outer Comp.Factor',
                value=row[11]
            )

        group = AtomicGroup.objects.get_or_create(
            name='Endfittings',
            description='List of endfittings for gas-springs'
        )[0]
        for member in endfittings:
            group.members.add(member)
        group.save()
