from django.db import models
from django.core.exceptions import ValidationError

class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class AtomicComponent(TimestampedModel):

	stock_code = models.CharField(max_length=255, null=False)
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
	min_quantity = models.PositiveIntegerField(default=1, null=False, blank=False)
	max_quantity = models.PositiveIntegerField(default=1, null=False, blank=False)

	# def available(self):
	# 	return True if self.quantity <= self.atomic_component.availability else False

	def __str__(self):
		return "AtomicRequirement: {} - {}".format(self.atomic_component.stock_code, self.quantity)

class BlueprintRequirement(TimestampedModel):

	blueprint_component = models.ForeignKey('Blueprint', on_delete=models.PROTECT, related_name='components', null=False)
	min_quantity = models.PositiveIntegerField(default=1, null=False, blank=False)
	max_quantity = models.PositiveIntegerField(default=1, null=False, blank=False)

class Blueprint(TimestampedModel):

	name = models.CharField(max_length=250)
	atomic_requirements = models.ManyToManyField(AtomicRequirement, related_name='requirements', symmetrical=False)
	blueprint_requirements = models.ManyToManyField(BlueprintRequirement, related_name='requirements', symmetrical=False)

	def isEmpty(self):
		if len(self.atomic_requirements.all()) == 0 and len(self.blueprint_requirements.all()) == 0:
			return True
		else:
			return False

	# def available(self):
	# 	results = []
	# 	for atm_req in self.atomic_requirements.all():
	# 		results.append(atm_req.available())
	#
	# 	return all(results)

	def available(self):
		for requirement in self.listAtomicDependencies():
			if requirement.atomic_component.availability >= requirement.quantity:
				continue
			else:
				return False
		return True

	def getLocalAtomicDependencies(self):
		"""
		Return local AtomicRequirement only
		:return: list[AtomicRequirement]
		"""
		l = []
		for req in self.atomic_requirements.all():
			l.append(req)
		return l

	def listAtomicDependencies(self):
		"""
		Return all atomic dependencies recursively
		return list instead of queryset

		:return: list[AtomicRequirement]
		"""
		if len(self.blueprint_requirements.all()) == 0:
			# If no further blueprint dependencies
			return self.getLocalAtomicDependencies()
		else:
			atomicReq = self.getLocalAtomicDependencies()
			for bpReq in self.blueprint_requirements.all():
				atomicReq.extend(bpReq.blueprint_component.listAtomicDependencies())
			return atomicReq

	def getLocalAtomicDependencies(self):
		"""
		Return local AtomicRequirement only
		:return: list[AtomicRequirement]
		"""
		l = []
		for req in self.atomic_requirements.all():
			l.append(req)
		return l

	def listAtomicDependencies(self):
		"""
		Return all atomic dependencies recursively
		return list instead of queryset

		:return: list[AtomicRequirement]
		"""
		if len(self.blueprint_requirements.all()) == 0:
			# If no further blueprint dependencies
			return self.getLocalAtomicDependencies()
		else:
			atomicReq = self.getLocalAtomicDependencies()
			for bpReq in self.blueprint_requirements.all():
				atomicReq.extend(bpReq.blueprint_component.listAtomicDependencies())
			return atomicReq







