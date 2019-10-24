from shop.assembly.models import Blueprint, BlueprintGroup
from shop.attribute.models import Attribute


def run():

    options = {
        "Carbon": ["CA_6-15", "CA_8-18", "CA_10-23", "CA_10-28", "CA_14-28", "CA_22-38"],
        "Stainless Steel": ["SS_6-15", "SS_8-18", "SS_10-23", "SS_10-28", "SS_14-28", "SS_22-38"],
        "Titanium": ["TI_6-15", "TI_8-18", "TI_10-23", "TI_10-28", "TI_14-28", "TI_22-38"],
        "Super Duplex": ["SU_6-15", "SU_8-18", "SU_10-23", "SU_10-28", "SU_14-28", "SU_22-38"]
    }

    # Create gas-spring group
    gas_spring_group, create = BlueprintGroup.objects.get_or_create(name="Gas Spring")

    for material, model_set in options.items():
        print(model_set)
        group, create = BlueprintGroup.objects.get_or_create(name=material+" group")
        for model in model_set:
            blueprint, created = Blueprint.objects.get_or_create(name=model)
            gas_spring_group.members.add(blueprint)
            group.members.add(blueprint)
            material_attribute, created = Attribute.objects.get_or_create(key="material", value=material,
                                                                          visibility='online')
            blueprint.attribute.add(material_attribute)
            blueprint.save()
        group.save()

    gas_spring_group.save()
