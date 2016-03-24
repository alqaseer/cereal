#!/usr/bin/env python

import csv
import os
import sys
sys.path.append('..')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
from main.models import Cereal, manufacturer
import django
django.setup()

Cereal.objects.all().delete()

dir_path = os.path.dirname(os.path.abspath(__file__))

Cereal_csv = os.path.join(dir_path, 'cereal.csv')

csv_file = open(Cereal_csv, 'r')

reader = csv.DictReader(csv_file)

for row in reader:
	new_manu, created = manufacturer.objects.get_or_create(manufacturer_name=row['Manufacturer'])
	new_manu.manufacturer_name = row['Manufacturer']
	new_manu.save()

	new_cereal, created = Cereal.objects.get_or_create(name=row['Cereal Name'])

	new_cereal.name = row['Cereal Name']
	new_cereal.manufacturer = new_manu
	new_cereal.cereal_type = row['Type']
	new_cereal.clories = row['Calories']
	new_cereal.protien = row['Protein (g)']
	new_cereal.fat = row['Fat']
	new_cereal.sodium = row['Sodium']
	new_cereal.dietery_fiber = row['Dietary Fiber']
	new_cereal.carbs = row['Carbs']
	new_cereal.sugars = row['Sugars']
	new_cereal.display_shelf = row['Display Shelf']
	new_cereal.potassium = row['Potassium']
	new_cereal.vitamins = row['Vitamins and Minerals']
	new_cereal.serving_size = row['Serving Size Weight']
	new_cereal.cups_per_serving = row['Cups per Serving']

	new_cereal.save()