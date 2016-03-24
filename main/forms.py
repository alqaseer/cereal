from django import forms
from main.models import Cereal
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[a-zA-Z]*$', 'Only LETTERS !!!!')

class CerealSearchForm(forms.Form):
	name = forms.CharField(required=True, validators=[alphanumeric])
	manufacturer = forms.CharField(required=True, validators=[alphanumeric])

class CerealEditForm(forms.ModelForm):
	class Meta:
		model = Cereal
		fields = '__all__'


class CerealCreateForm(forms.ModelForm):
	class Meta:
		model = Cereal
		fields = '__all__'





