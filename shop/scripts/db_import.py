import csv
from shop.atomic.models import AtomicComponent, AtomicAttribute
from shop.group.models import AtomicGroup


def run():

    endfittings = []

    with open('shop/scripts/atomic_component.csv', newline='') as csvfile:
        has_header = csv.Sniffer().has_header(csvfile.read(1024))
        reader = csv.reader(csvfile, delimiter=',')
        if has_header:  # Skip header row.
            next(reader)

        for row in reader:
            print(', '.join(row))
            atom = AtomicComponent.objects.get_or_create(
                stock_code=row[3],
                part_code=row[2],
                warehouse_location=row[4],
                type=row[0]
            )[0]
            # endfittings.append(atom)
            # AtomicAttribute.objects.get_or_create(
            #     atomic_component=atom,
            #     key='Thread size',
            #     value=row[9]
            # )
            # AtomicAttribute.objects.get_or_create(
            #     atomic_component=atom,
            #     key='Outer Comp.Factor',
            #     value=row[11]
            # )

        # group = AtomicGroup.objects.get_or_create(
        #     name='Endfittings',
        #     description='List of endfittings for gas-springs'
        # )[0]
        # for member in endfittings:
        #     group.members.add(member)
        # group.save()

