from shop.group.models import Group

def run():
    # Create material groups

    carbon, created = Group.objects.get_or_create(name="Carbon", description="Carbon Gas springs")
