import pandas as pd
import progressbar
import math
from shop.atomic.models import AtomicComponent, AtomicGroup
from shop.attribute.models import Attribute


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
                Attribute.objects.get_or_create(
                            key=attributeHeaders,
                            value=parameters[attributeHeaders]
                        )
    bar.finish()

    ##
    # Create group for Endfittings
    ##
    print("""
        Creating Endfitting group
    """)
    group = AtomicGroup.objects.get_or_create(
        name='Endfittings',
        description='List of endfittings for gas-springs'
    )[0]
    endfitting_ids = [627, 132, 192, 194, 195, 196, 199, 205, 214, 215, 217, 218, 225, 227, 228, 232, 233, 240, 241, 497, 122, 123, 127, 129, 133, 134, 136, 137, 138, 139, 141, 147, 148, 150, 805, 152, 154, 155, 158, 160, 180, 181, 186, 188, 222, 164, 170, 173, 528]
    bar = progressbar.ProgressBar(maxval=len(endfitting_ids),
                                  widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
    bar.start()
    bar_count = 0
    for id in endfitting_ids:
        bar_count = bar_count + 1
        bar.update(bar_count)
        stock_code = df.loc[df['Id'] == id, 'Stock_code']
        if len(stock_code.values) > 0:
            group.members.add(AtomicComponent.objects.filter(stock_code=stock_code.values[0]).first())
    group.save()
    bar.finish()
