from django.db import models

# Create your models here.
class Cereal(models.Model):
	name = models.CharField(max_length=100, null=True, blank=True)
	manufacturer = models.ForeignKey('main.manufacturer', null=True)
	cereal_type = models.CharField(max_length=10, null=True, blank=True)
	clories = models.CharField(max_length=100, null=True, blank=True)
	protien = models.CharField(max_length=100, null=True, blank=True)
	fat = models.CharField(max_length=100, null=True, blank=True)
	sodium = models.CharField(max_length=100, null=True, blank=True)
	dietery_fiber = models.CharField(max_length=100, null=True, blank=True)
	
	carbs = models.CharField(max_length=100, null=True, blank=True)
	sugars = models.CharField(max_length=100, null=True, blank=True)
	display_shelf = models.CharField(max_length=100, null=True, blank=True)

	potassium = models.CharField(max_length=100, null=True, blank=True)
	vitamins = models.CharField(max_length=100, null=True, blank=True)
	serving_size = models.CharField(max_length=100, null=True, blank=True)
	cups_per_serving = models.CharField(max_length=100, null=True, blank=True)
	def __unicode__(self):
		return self.name

class manufacturer(models.Model):
	manufacturer_name = models.CharField(max_length=100, null=True, blank=True)
	def __unicode__(self):
		return self.manufacturer_name
