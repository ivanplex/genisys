from shop.configurator.models import ConfiguratorStep


def run():
    ConfiguratorStep.objects.get_or_create(
        title='Material',
        description='',
        type='selector',
        slug='material'
    )

    ConfiguratorStep.objects.get_or_create(
        title='Model',
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
