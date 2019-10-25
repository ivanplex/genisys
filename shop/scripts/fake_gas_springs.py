from shop.assembly.models import Blueprint, BlueprintGroup
from shop.assembly.models import AtomicPrerequisite
from shop.attribute.models import Attribute


def run():

    options = {
        "Carbon": ["E-6-15", "E-8-18", "E-10-23", "E-10-28", "E-14-28", "E-22-38"],
        "Stainless Steel": ["S-6-15", "S-8-18", "S-10-23", "S-10-28", "S-14-28", "S-22-38"],
        "Titanium": ["T-6-15", "T-8-18", "T-10-23", "T-10-28", "T-14-28", "T-22-38"],
        "Super Duplex": ["D-6-15", "D-8-18", "D-10-23", "D-10-28", "D-14-28", "D-22-38"]
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
            product_type_attribute, created = Attribute.objects.get_or_create(key="product type", value="compression",
                                                                          visibility='online')
            blueprint.attribute.add(material_attribute)
            blueprint.attribute.add(product_type_attribute)

            # Stoke Length
            prerequisite, created = AtomicPrerequisite.objects.get_or_create(name="Stroke Length", virtual=True,
                                                     min_quantity=10, max_quantity=70)
            blueprint.atomic_prerequisites.add(prerequisite)
            blueprint.save()
        group.save()

    gas_spring_group.save()
