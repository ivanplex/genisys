import pandas as pd
import progressbar
import math
from modular_assembly.atomic.models import AtomicComponent, AtomicGroup
from modular_assembly.attribute.models import Attribute
from modular_assembly.models import URL, OffsetImageURL



def run():

    csv_headers = [
        'Id', 'code', 'Category', 'Location', 'sku', 'Costs', 'RingRoll', 'RingRollDiameter',
        'Material', 'Weight', 'OuterDiameter', 'InnerDiameter', 'InnerCompFactor', 'OuterCompFactor', 'Viscosity',
        'WallThickness', 'OrificeSize', 'ErpID', 'UnityMeasureType'
    ]

    df = pd.read_csv('modular_assembly/scripts/atomic_component.csv',
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
            sku=parameters['sku'],
            category=parameters['Category'],
            description=parameters['code'],
            warehouse_location=parameters['Location']
        )[0]

        atom.image_urls.add(URL.objects.get_or_create(url='https://dummyimage.com/300')[0])
        atom.image_urls.add(URL.objects.get_or_create(url='https://dummyimage.com/250')[0])
        atom.image_urls.add(URL.objects.get_or_create(url='https://dummyimage.com/200')[0])
        atom.offset_image_urls.add(OffsetImageURL.objects.get_or_create(url='https://dummyimage.com/100')[0])
        atom.offset_image_urls.add(OffsetImageURL.objects.get_or_create(url='https://dummyimage.com/150')[0])
        atom.save()

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
        sku = df.loc[df['Id'] == id, 'sku']
        if len(sku.values) > 0:
            group.members.add(AtomicComponent.objects.filter(sku=sku.values[0]).first())
    group.save()
    bar.finish()
