from django.db import models
from django.core.exceptions import ValidationError

class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class AtomicComponent(TimestampedModel):

	stock_code = models.CharField(max_length=255, null=False, )
	part_code = models.CharField(max_length=255, null=True)
	description = models.TextField(blank=True, null=True)
	warehouse_location = models.IntegerField(blank=True, null=True)
	material = models.CharField(max_length=255, blank=True, null=True)
	weight = models.IntegerField(blank=True, null=True)
	image = models.CharField(max_length=1000, blank=True, null=True)
	availability = models.IntegerField(null=False, default=0)

	def save(self, *args, **kwargs):
		if self.stock_code is "":
			raise ValidationError('stock_code cannot be empty.')
		else:
			super(AtomicComponent, self).save(*args, **kwargs)

class AtomicRequirement(TimestampedModel):

	atomic_component = models.ForeignKey(AtomicComponent, on_delete=models.PROTECT, related_name='components', null=False)
	quantity = models.PositiveIntegerField(default=1, null=False, blank=False)

	def available(self):
		return True if self.quantity <= self.atomic_component.availability else False

class BlueprintRequirement(TimestampedModel):

	blueprint_component = models.ForeignKey('Blueprint', on_delete=models.PROTECT, related_name='components', null=False)
	quantity = models.PositiveIntegerField(default=1, null=False, blank=False)

class Blueprint(TimestampedModel):

	name = models.CharField(max_length=250)
	atomic_requirements = models.ManyToManyField(AtomicRequirement, related_name='requirements', symmetrical=False)
	blueprint_requirements = models.ManyToManyField(BlueprintRequirement, related_name='requirements', symmetrical=False)

	def available(self):
		results = []
		for atm_req in self.atomic_requirements.all():
			results.append(atm_req.available())

		return all(results)
