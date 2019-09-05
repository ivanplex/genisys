# from django.db import models
# from shop.models import AtomicComponent, Blueprint, AtomicRequirement
#
# class PistonComponent(AtomicComponent):
#
# 	COMPONENT_TYPE = (
# 			('Piston','Piston'),
# 			('Tube','Tube'),
# 			('Rod','Rod'),
# 			('Inner','Inner'),
# 			('Rod_Component','Rod_Component'),
# 			('Component','Component'),
# 			('Endfitting','Endfitting'),
# 			('Valve_Block','Valve_Block'),
# 			('Spacer','Spacer'),
# 			('Sleeve','Sleeve'),
# 			('Inner_Tube','Inner_Tube'),
# 			('End_Block','End_Block'),
# 			('CNC_Component','CNC_Component'),
# 			('Ratio_Pseudo','Ratio_Pseudo'),
# 		)
#
# 	c_type = models.CharField(max_length=255, choices=COMPONENT_TYPE, null=True)