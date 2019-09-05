from django.db import models
from django.core.exceptions import ValidationError
from shop.models import TimestampedModel, AtomicRequirementModel, BlueprintRequirementModel

class AtomicRequirement(AtomicRequirementModel):

	min_quantity = models.PositiveIntegerField(default=1, null=False, blank=False)
	max_quantity = models.PositiveIntegerField(default=1, null=False, blank=False)

	# def available(self):
	# 	return True if self.quantity <= self.atomic_component.availability else False

	def __str__(self):
		return "AtomicRequirement: {} - {}".format(self.atomic_component.stock_code, self.quantity)

class BlueprintRequirement(BlueprintRequirementModel):

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







