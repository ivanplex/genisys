"""
Test BlueprintPrerequisites using API
"""

import json
import requests

from shop.atomic.models import AtomicComponent, AtomicPrerequisite
from shop.assembly.models import Blueprint, Product, ProductPrerequisite


def submit(url, payload):
    data = json.dumps(payload)
    return requests.post('https://dev-web-aw66scuunq-ew.a.run.app'+url, json=payload)


def run():
    tableTop = {
        'stock_code': 'TBT',
        'part_code': 'tableTop',
        'description': 'IKEA TABLE TOP',
        'warehouse_location': '2000',
        'weight': 100,
        'image': '/img/table_top.png',
        'availability': 80,
    }
    tableLeg = {
        'stock_code': 'TBL',
        'part_code': 'tableLeg',
        'description': 'IKEA TABLE LEG',
        'warehouse_location': '2001',
        'weight': 40,
        'image': '/img/table_leg.png',
        'availability': 200,
    }
    screws = {
        'stock_code': 'SRW',
        'part_code': 'screw',
        'description': 'screws',
        'warehouse_location': '80000',
        'weight': 1,
        'image': '/img/screws.png',
        'availability': 100000,
    }
    chairPlate = {
        'stock_code': 'CPT',
        'part_code': 'chairPlate',
        'description': 'IKEA Chair Back plate',
        'warehouse_location': '7000',
        'weight': 120,
        'image': '/img/chair_back_plate.png',
        'availability': 20,
    }
    chairleg = {
        'stock_code': 'CLG',
        'part_code': 'chairLeg',
        'description': 'IKEA Chair Leg',
        'warehouse_location': '7001',
        'weight': 30,
        'image': '/img/chair_leg.png',
        'availability': 55,
    }
    manual = {
        'stock_code': 'MNU',
        'part_code': 'manual',
        'description': 'IKEA assembly manual',
        'warehouse_location': '1',
        'weight': 15,
        'image': '/img/manual.png',
        'availability': 30,
    }
    atomic_comp = [
        tableTop,
        tableLeg,
        chairPlate,
        chairleg,
        screws,
        manual
    ]

    #Create each atomic component using API calls
    for comp in atomic_comp:
        url = '/atomic/component/create/'
        response = submit(url, comp)

    ###
    # Create Blueprints
    ###

    table_blueprint = {
        'name': 'Table',
        'atomic_prerequisites': [
            {
                'atomic_component': AtomicComponent.objects.filter(stock_code='TBT').first().id,
                'min_quantity': 1,
                'max_quantity': 1
            },
            {
                'atomic_component': AtomicComponent.objects.filter(stock_code='TBL').first().id,
                'min_quantity': 4,
                'max_quantity': 4
            },
            {
                'atomic_component': AtomicComponent.objects.filter(stock_code='SRW').first().id,
                'min_quantity': 8,
                'max_quantity': 8
            }
        ],
        'product_prerequisites': []
    }
    chair_blueprint = {
        'name': 'Chair',
        'atomic_prerequisites': [
            {
                'atomic_component': AtomicComponent.objects.filter(stock_code='CPT').first().id,
                'min_quantity': 1,
                'max_quantity': 1
            },
            {
                'atomic_component': AtomicComponent.objects.filter(stock_code='CLG').first().id,
                'min_quantity': 4,
                'max_quantity': 4
            },
            {
                'atomic_component': AtomicComponent.objects.filter(stock_code='SRW').first().id,
                'min_quantity': 4,
                'max_quantity': 4
            }
        ],
        'product_prerequisites': []
    }

    blueprints = [table_blueprint, chair_blueprint]
    for blueprint in blueprints:
        url = '/assembly/blueprint/create/'
        response = submit(url, blueprint)

    ###
    # Create Product table and chair
    ###

    table_product = {
        'name': 'Table',
        'sku': 'TBL',
        'availability': 0,
        'blueprint': Blueprint.objects.filter(name='Table').first().id,
        'atomic_specifications': [
            {
                'atomic_prereq': AtomicPrerequisite.objects.filter(atomic_component__stock_code='TBT').first().id,
                'quantity': 1
            },
            {
                'atomic_prereq': AtomicPrerequisite.objects.filter(atomic_component__stock_code='TBL').first().id,
                'quantity': 4
            },
            {
                'atomic_prereq': AtomicPrerequisite.objects.filter(atomic_component__stock_code='SRW').first().id,
                'quantity': 8
            }
        ],
        'product_specifications': []
    }
    chair_product = {
        'name': 'Chair',
        'sku': 'CHR',
        'availability': 10,
        'blueprint': Blueprint.objects.filter(name='Chair').first().id,
        'atomic_specifications': [
            {
                'atomic_prereq': AtomicPrerequisite.objects.filter(atomic_component__stock_code='CPT').first().id,
                'quantity': 1
            },
            {
                'atomic_prereq': AtomicPrerequisite.objects.filter(atomic_component__stock_code='CLG').first().id,
                'quantity': 4
            },
            {
                'atomic_prereq': AtomicPrerequisite.objects.filter(atomic_component__stock_code='SRW').first().id,
                'quantity': 4
            }
        ],
        'product_specifications': []
    }
    products = [table_product, chair_product]
    for product in products:
        url = '/assembly/product/create/'
        response = submit(url, product)

    ###
    # Build Table-set Blueprint
    ###
    table_set_blueprint = {
        'name': 'Table Set',
        'atomic_prerequisites': [
            {
                'atomic_component': AtomicComponent.objects.filter(stock_code='MNU').first().id,
                'min_quantity': 1,
                'max_quantity': 1
            }
        ],
        'product_prerequisites': [
            {
                'product': Product.objects.filter(name='Table').first().id,
                'min_quantity': 1,
                'max_quantity': 1
            },
            {
                'product': Product.objects.filter(name='Chair').first().id,
                'min_quantity': 2,
                'max_quantity': 4
            }
        ]
    }
    url = '/assembly/blueprint/create/'
    response = submit(url, table_set_blueprint)

    ###
    # Build Table-set Product
    ###
    table_set_product = {
        'name': 'Table Set',
        'sku': 'TBS',
        'availability': 10,
        'blueprint': Blueprint.objects.filter(name='Table Set').first().id,
        'atomic_specifications': [
            {
                'atomic_prereq': AtomicPrerequisite.objects.filter(atomic_component__stock_code='MNU').first().id,
                'quantity': 4
            }
        ],
        'product_specifications': [
            {
                'product_prereq': ProductPrerequisite.objects.filter(product__name='Table').first().id,
                'quantity': 1
            },
            {
                'product_prereq': ProductPrerequisite.objects.filter(product__name='Chair').first().id,
                'quantity': 4
            }
        ]
    }
    url = '/assembly/product/create/'
    response = submit(url, table_set_product)

