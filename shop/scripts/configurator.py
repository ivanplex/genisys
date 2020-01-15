from shop.configurator.models import ConfiguratorStep


def run():
    ConfiguratorStep.objects.get_or_create(
        title='Material',
        description='',
        type='selector',
        slug='material',
        order=1
    )

    ConfiguratorStep.objects.get_or_create(
        title='Model Size',
        description='',
        type='selector',
        slug='model',
        order=2
    )

    ConfiguratorStep.objects.get_or_create(
        title='Stroke Length',
        description='',
        type='numerical_range',
        slug='stroke',
        order=3
    )

    ConfiguratorStep.objects.get_or_create(
        title='Select Extension',
        description='',
        type='selector',
        slug='extension',
        order=4
    )

    ConfiguratorStep.objects.get_or_create(
        title='Select Sleeves',
        description='',
        type='selector',
        slug='sleeves',
        disabled=False,
        order=5
    )

    ConfiguratorStep.objects.get_or_create(
        title='Rod Fitting',
        description='',
        type='selector',
        slug='rod-fitting',
        order=6
    )

    ConfiguratorStep.objects.get_or_create(
        title='Body Fitting',
        description='',
        type='selector',
        slug='body-fitting',
        order=7
    )

    ConfiguratorStep.objects.get_or_create(
        title='Extended Length',
        description='',
        type='numerical_range',
        slug='extended_length',
        order=8
    )

    ConfiguratorStep.objects.get_or_create(
        title='Force',
        description='',
        type='numerical_range',
        slug='force',
        order=9
    )
