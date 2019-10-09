import pandas as pd
import progressbar
import math
from shop.atomic.models import AtomicComponent, AtomicAttribute, AtomicGroup


def run():

    csv_headers = [
        'Id', 'code', 'Category', 'Location', 'Stock_code', 'Costs', 'RingRoll', 'RingRollDiameter',
        'Material', 'Weight', 'OuterDiameter', 'InnerDiameter', 'InnerCompFactor', 'OuterCompFactor', 'Viscosity',
        'WallThickness', 'OrificeSize', 'ErpID', 'UnityMeasureType'
    ]

    df = pd.read_csv('shop/scripts/atomic_component.csv',
                     skiprows=1,
                     names=csv_headers)

    # setup status bar
    print("""
        Importing all atomic components.
    """)
    bar = progressbar.ProgressBar(maxval=len(df.index),
                                  widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
    bar.start()
    bar_count = 0

    for k, parameters in df.iterrows():
        bar_count = bar_count + 1
        bar.update(bar_count)

        atom = AtomicComponent.objects.get_or_create(
            stock_code=parameters['Stock_code'],
            category=parameters['Category'],
            description=parameters['code'],
            warehouse_location=parameters['Location']
        )[0]

        for attributeHeaders in csv_headers[5:]:
            if not math.isnan(parameters[attributeHeaders]) and parameters[attributeHeaders] != 0:
                AtomicAttribute.objects.get_or_create(
                            atomic_component=atom,
                            key=attributeHeaders,
                            value=parameters[attributeHeaders]
                        )

    # group = AtomicGroup.objects.get_or_create(
    #     name='Endfittings',
    #     description='List of endfittings for gas-springs'
    # )[0]
    # for member in endfittings:
    #     group.members.add(member)
    # group.save()

    bar.finish()
