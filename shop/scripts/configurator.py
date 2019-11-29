from shop.configurator.models import ConfiguratorStep


def run():
    ConfiguratorStep.objects.get_or_create(
        title='Material',
        description='',
        type='selector',
        slug='material'
    )

    ConfiguratorStep.objects.get_or_create(
        title='Model Size',
        description='',
        type='selector',
        slug='model'
    )

    ConfiguratorStep.objects.get_or_create(
        title='Stroke Length',
        description='',
        type='numerical_range',
        slug='stroke'
    )

    ConfiguratorStep.objects.get_or_create(
        title='Select Extension',
        description='',
        type='selector',
        slug='extension'
    )

    ConfiguratorStep.objects.get_or_create(
        title='Select Sleeves',
        description='',
        type='selector',
        slug='sleeves',
        disabled=False
    )

    ConfiguratorStep.objects.get_or_create(
        title='Rod Fitting',
        description='',
        type='selector',
        slug='rod-fitting'
    )

    ConfiguratorStep.objects.get_or_create(
        title='Body Fitting',
        description='',
        type='selector',
        slug='body-fitting'
    )

    ConfiguratorStep.objects.get_or_create(
        title='Extended Length',
        description='',
        type='numerical_range',
        slug='extended_length'
    )

    ConfiguratorStep.objects.get_or_create(
        title='Force',
        description='',
        type='numerical_range',
        slug='force'
    )
