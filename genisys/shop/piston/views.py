from django.http import HttpResponse
from .models import AtomicComponent, Blueprint, AtomicRequirement

def fail(request):
    a = AtomicComponent()
    a.save()
    return HttpResponse("Success")

def createComponents(request):

    components = [
        AtomicComponent(stock_code='U-Bolt', part_code='U-Bolt', quantity=8000),
        AtomicComponent(stock_code='T-Leg', part_code='T-Leg', quantity=50),
        AtomicComponent(stock_code='T-Top', part_code='T-Top', quantity=45)
    ]

    for c in components:
        c.save()
    return HttpResponse("Success")

def createTableBlueprint(request):

    tableRequirements = [
        AtomicRequirement(atomic_component=AtomicComponent.objects.get(stock_code='U-Bolt'), quantity=4),
        AtomicRequirement(atomic_component=AtomicComponent.objects.get(stock_code='T-Top'), quantity=4),
        AtomicRequirement(atomic_component=AtomicComponent.objects.get(stock_code='T-Leg'), quantity=4),
    ]

    b = Blueprint(name='Table')
    b.save()

    for r in tableRequirements:
        r.save()
        b.blueprint_equirements.add(r)


    return HttpResponse("Success")

def checkAvailable(request):



    return HttpResponse("Success")