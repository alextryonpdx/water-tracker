from django import forms
from django.db import models
from django.forms import ModelForm, DateInput, DateField, extras, CheckboxSelectMultiple
from django.forms.extras.widgets import SelectDateWidget

from .models import Guide, Entry

class GuideForm(forms.ModelForm):

    class Meta:
        model = Guide
        fields = ('FirstName', 'LastName', 'password', 'employee_type',)





class EntryForm(forms.ModelForm):

	class Meta:
		model = Entry
		fields = ("guide", "date" ,'river' , 'trip_type', 'leader', 'guides', 'rafts', 'kayaks', 'waterLevel', 'weather', 'general_description', 'problems', 'guest_problems')






# def get_guides():
# 	guides = Guide.objects.all()
# 	ALL = 'All Guides'
# 	choices = ( (ALL, 'All Guides'), )
# 	# for guide in guides:
# 	# 	guide.pk = guide.LastName
# 	# 	choice = (guide.pk, guide.LastName)
# 	# 	choices.append(choice)

# 	return(choices)


# class SortGuides(forms.ModelForm):

# 	class Meta():
# 		model = Guide
# 		fields = ['FirstName', 'LastName']



	# class SortDate(forms.Form):

		
	# 	start = forms.DateTimeField(widget=extras.SelectDateWidget())
	# 	end = forms.DateTimeField(widget=extras.SelectDateWidget())

	# 	guides = Guide.objects.all()
	# 	ALL = 'All Guides'
	# 	choices =  [(ALL, 'All Guides'), ]

	# 	for guide in guides:
	# 		LastName = guide.LastName
	# 		choice = (guide.pk, LastName)
	# 		choices.append(choice)

	# 	guide = forms.CharField(widget=CheckboxSelectMultiple, choices=choices)

# river = models.CharField(max_length=64,
# 							choices=River_Choices,
# 							null=True)

	# WHITE_SALMON_HALF = 'White Salmon Half-Day'
	# WHITE_SALMON_FULL = 'White Salmon Full-Day'
	# WIND = 'Wind River'
	# KLICKITAT = 'Klickitat River'
	# HOOD = 'Hood River'
	# FARMLANDS = 'The Farmlands'
	# TIETON = 'Tieton River'
	# River_Choices = (
	# 	(WHITE_SALMON_HALF, 'White Salmon Half-Day'),
	# 	(WHITE_SALMON_FULL, 'White Salmon Full-Day'),
	# 	(WIND, 'Wind River'),
	# 	(KLICKITAT, 'Klickitat River'),
	# 	(HOOD, 'Hood River'),
	# 	(FARMLANDS, 'The Farmlands'),
	# 	(TIETON, 'Tieton River')
	# )

	# def clean(self):
	# 	cleaned = super().clean()
	# 	start = cleaned.get('start')
	# 	end = cleaned.get('end')

	# guide = forms.CheckboxSelectMultiple( choices=get_guides() )
