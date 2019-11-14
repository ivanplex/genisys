from rest_framework.decorators import api_view
from rest_framework.response import Response
from shop.atomic.models import AtomicComponent, AtomicGroup
from shop.atomic.serializers import AtomicComponentConfiguratorSerializer
from shop.assembly.models import Blueprint, AtomicPrerequisite
from shop.attribute.models import Attribute
from shop.assembly.serializers import BlueprintConfiguratorSerializer
from shop.configurator.models import ConfiguratorStep
from shop.configurator.serializers import ConfiguratorStepSerializer


def show_materials(required=True):
    return [
            # {
            #     "id": 1,
            #     "name": "Super Duplex",
            #     "thumb_image": "https://dummyimage.com/50",
            #     "illustration_image": [
            #         {
            #             "url": "https://dummyimage.com/100",
            #             "offset_x": 3,
            #             "offset_y": 2
            #         },
            #         {
            #             "url": "https://dummyimage.com/100",
            #             "offset_x": 3,
            #             "offset_y": 2
            #         },
            #         {
            #             "url": "https://dummyimage.com/100",
            #             "offset_x": 3,
            #             "offset_y": 2
            #         }
            #     ]
            # },
            {
                "id": 2,
                "name": "Carbon",
                "thumb_image": "https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/E+-+Carbon+Steel+Painted-Current+View.png",
                "illustration_image": [
                    {
                        "url": "https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/G-E-15-BodyEnd-h50-l.png",
                        "offset_x": 0,
                        "offset_y": 0
                    },
                    {
                        "url": "https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/G-E-15-BodySpan-h50.png",
                        "offset_x": 0,
                        "offset_y": 0
                    },
                    {
                        "url": "https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/G-E-15-BodyEnd-h50-r.png",
                        "offset_x": 0,
                        "offset_y": 0
                    }
                ]
            },
            # {
            #     "id": 3,
            #     "name": "Titanium",
            #     "thumb_image": "https://dummyimage.com/50",
            #     "illustration_image": [
            #         {
            #             "url": "https://dummyimage.com/100",
            #             "offset_x": 3,
            #             "offset_y": 2
            #         },
            #         {
            #             "url": "https://dummyimage.com/100",
            #             "offset_x": 3,
            #             "offset_y": 2
            #         },
            #         {
            #             "url": "https://dummyimage.com/100",
            #             "offset_x": 3,
            #             "offset_y": 2
            #         }
            #     ]
            # },
            {
                "id": 4,
                "name": "Stainless Steel",
                "thumb_image": "https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/S+-+Stainless+Steel-Current+View.png",
                "illustration_image": [
                    {
                        "url": "https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/G-S-15-BodyEnd-h50-l.png",
                        "offset_x": 0,
                        "offset_y": 0
                    },
                    {
                        "url": "https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/G-S-15-BodySpan-h50.png",
                        "offset_x": 0,
                        "offset_y": 0
                    },
                    {
                        "url": "https://genisys-static-dev.s3.eu-west-2.amazonaws.com/configurator/G-S-15-BodyEnd-h50-r.png",
                        "offset_x": 0,
                        "offset_y": 0
                    }
                ]
            }
        ]


def show_models(material_id, required=True):
    material_id_mapping = {
        1: 'Super Duplex',
        2: 'Carbon',
        3: 'Titanium',
        4: 'Stainless Steel'
    }

    #TODO: fix this

    # gas_spring_models = Blueprint.objects.filter(attribute__value=material_id_mapping.get(material_id))
    attr = Attribute.objects.filter(key="material", value="Carbon").first()
    gas_spring_models = Blueprint.objects.filter(name="SS-6-15")
    serializer = BlueprintConfiguratorSerializer(gas_spring_models, many=True)
    return serializer.data


def show_stroke_length(model_id, required=True):
    blueprint = Blueprint.objects.filter(id=model_id).first()
    stroke = AtomicPrerequisite.objects.get(id=1)
    return {
        'minimum': stroke.min_quantity,
        'maximum': stroke.max_quantity
    }

def show_extension(model_id):
    extensions = AtomicComponent.objects.filter(stock_code="M5-13-EXT")
    serializer = AtomicComponentConfiguratorSerializer(extensions, many=True)
    empty = [{
                "id": "null",
                "stock_code": "None",
                "thumbnail_images": [
                    {
                        "url": "https://dummyimage.com/100"
                    }
                ],
                "illustration_images": [],
                "description_images": [],
                "retail_price": 0.0,
                "retail_price_per_unit": 0.0,
                "retail_unit_measurement": "null"
            }]
    return empty + serializer.data


def show_endfitting(model_id):
    endfittings = AtomicComponent.objects.filter(members__name="demo_group")
    serializer = AtomicComponentConfiguratorSerializer(endfittings, many=True)
    return serializer.data

def show_extended_length(model_id):
    length = AtomicPrerequisite.objects.get(id=2)
    return {
        'minimum': length.min_quantity,
        'maximum': length.max_quantity
    }

def show_force(model_id):
    force = AtomicPrerequisite.objects.get(id=3)
    return {
        'minimum': force.min_quantity,
        'maximum': force.max_quantity
    }


@api_view(['GET', 'POST'])
def interactions(request):
    if request.method == 'POST':
        steps = ConfiguratorStep.objects.all().order_by('id')
        raw_steps = ConfiguratorStepSerializer(steps, many=True).data

        material = request.data.get('material', None)
        model = request.data.get('model', None)
        stroke = request.data.get('stroke', None)
        extension = request.data.get('extension', None)
        rod_fitting = request.data.get('rod-fitting', None)
        body_fitting = request.data.get('body-fitting', None)
        extended_length = request.data.get('extended_length', None)
        force = request.data.get('force', None)

        if force is not None:
            raw_steps[7]['option'] = show_force(model)
            raw_steps[7]['selected'] = force
            raw_steps[6]['option'] = show_extended_length(model)
            raw_steps[6]['selected'] = extended_length
            raw_steps[5]['option'] = show_endfitting(model)
            raw_steps[5]['selected'] = body_fitting
            raw_steps[4]['option'] = show_endfitting(model)
            raw_steps[4]['selected'] = rod_fitting
            raw_steps[3]['option'] = show_extension(model)
            raw_steps[3]['selected'] = extension
            raw_steps[2]['range'] = show_stroke_length(model)
            raw_steps[2]['selected'] = stroke
            raw_steps[1]['options'] = show_models(material)
            raw_steps[1]['selected'] = model
            raw_steps[0]['options'] = show_materials()
            raw_steps[0]['selected'] = material

        elif extended_length is not None:
            raw_steps[7]['option'] = show_force(model)
            raw_steps[6]['option'] = show_extended_length(model)
            raw_steps[6]['selected'] = extended_length
            raw_steps[5]['option'] = show_endfitting(model)
            raw_steps[5]['selected'] = body_fitting
            raw_steps[4]['option'] = show_endfitting(model)
            raw_steps[4]['selected'] = rod_fitting
            raw_steps[3]['option'] = show_extension(model)
            raw_steps[3]['selected'] = extension
            raw_steps[2]['range'] = show_stroke_length(model)
            raw_steps[2]['selected'] = stroke
            raw_steps[1]['options'] = show_models(material)
            raw_steps[1]['selected'] = model
            raw_steps[0]['options'] = show_materials()
            raw_steps[0]['selected'] = material

        elif body_fitting is not None:
            raw_steps[6]['option'] = show_extended_length(model)
            raw_steps[5]['option'] = show_endfitting(model)
            raw_steps[5]['selected'] = body_fitting
            raw_steps[4]['option'] = show_endfitting(model)
            raw_steps[4]['selected'] = rod_fitting
            raw_steps[3]['option'] = show_extension(model)
            raw_steps[3]['selected'] = extension
            raw_steps[2]['range'] = show_stroke_length(model)
            raw_steps[2]['selected'] = stroke
            raw_steps[1]['options'] = show_models(material)
            raw_steps[1]['selected'] = model
            raw_steps[0]['options'] = show_materials()
            raw_steps[0]['selected'] = material

        elif rod_fitting is not None:
            raw_steps[5]['option'] = show_endfitting(model)
            raw_steps[4]['option'] = show_endfitting(model)
            raw_steps[4]['selected'] = rod_fitting
            raw_steps[3]['option'] = show_extension(model)
            raw_steps[3]['selected'] = extension
            raw_steps[2]['range'] = show_stroke_length(model)
            raw_steps[2]['selected'] = stroke
            raw_steps[1]['options'] = show_models(material)
            raw_steps[1]['selected'] = model
            raw_steps[0]['options'] = show_materials()
            raw_steps[0]['selected'] = material

        elif extension is not None:
            raw_steps[4]['option'] = show_endfitting(model)
            raw_steps[3]['option'] = show_extension(model)
            raw_steps[3]['selected'] = extension
            raw_steps[2]['range'] = show_stroke_length(model)
            raw_steps[2]['selected'] = stroke
            raw_steps[1]['options'] = show_models(material)
            raw_steps[1]['selected'] = model
            raw_steps[0]['options'] = show_materials()
            raw_steps[0]['selected'] = material

        elif stroke is not None:
            raw_steps[3]['option'] = show_extension(model)
            raw_steps[2]['range'] = show_stroke_length(model)
            raw_steps[2]['selected'] = stroke
            raw_steps[1]['options'] = show_models(material)
            raw_steps[1]['selected'] = model
            raw_steps[0]['options'] = show_materials()
            raw_steps[0]['selected'] = material
        elif model is not None:
            num_range = show_stroke_length(model)
            raw_steps[2]['range'] = num_range
            # raw_steps[2]['selected'] = num_range['minimum']
            raw_steps[1]['options'] = show_models(material)
            raw_steps[1]['selected'] = model
            raw_steps[0]['options'] = show_materials()
            raw_steps[0]['selected'] = material

        elif material is not None:
            options = show_models(material)
            raw_steps[1]['options'] = options
            # raw_steps[1]['selected'] = options[0]['id']
            raw_steps[0]['options'] = show_materials()
            raw_steps[0]['selected'] = material
        else:
            raw_steps[0]['options'] = show_materials()
            raw_steps[0]['selected'] = show_materials()[0]['id']

        return Response(raw_steps)



    # # ordered list
    # steps = {
    #          'material':        1,
    #          'model':           1,
    #          'stroke':          1,
    #          'ext':             0,
    #          'rod_fitting':     1,
    #          'body_fitting':    1,
    #          'extended_length': 1,
    #          'force':           1
    #          }
    #
    # if request.method == 'GET':
    #     return show_materials()
    #
    # if request.method == 'POST':
    #     material = request.data.get('material', None)
    #     if material is None:
    #         return show_materials()
    #     else:
    #         return show_models(material)


        # gas_spring_model = request.data.get('model', None)
        # if gas_spring_model is None:
        #     return show_models(gas_spring_model)

            # content = {'Error': "Incomplete dataset. Missing key `model`."}
            # return Response(content, status=status.HTTP_400_BAD_REQUEST)
        # blueprint = Blueprint.objects.filter(name=gas_spring_model).first()
        # if blueprint is None:
        #     content = {'Error': 'Gas spring model not found.'}
        #     return Response(content, status=status.HTTP_404_NOT_FOUND)
        # serializer = GasSpringBlueprintSerializer(blueprint)
        # return Response(serializer.data)
