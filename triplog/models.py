from django.db import models
from django.utils import timezone
from django import forms
from django.forms import CheckboxSelectMultiple


# Create your models here.
class Entry(models.Model):
	guide = models.ForeignKey('Guide')
	editDate = models.DateField(
            default=timezone.now)
	date = models.DateField(
		blank=True, null=False)
	WHITE_SALMON_HALF = 'White Salmon Half-Day'
	WHITE_SALMON_FULL = 'White Salmon Full-Day'
	WIND = 'Wind River'
	KLICKITAT = 'Klickitat River'
	HOOD = 'Hood River'
	FARMLANDS = 'The Farmlands'
	TIETON = 'Tieton River'
	River_Choices = (
		(WHITE_SALMON_HALF, 'White Salmon Half-Day'),
		(WHITE_SALMON_FULL, 'White Salmon Full-Day'),
		(WIND, 'Wind River'),
		(KLICKITAT, 'Klickitat River'),
		(HOOD, 'Hood River'),
		(FARMLANDS, 'The Farmlands'),
		(TIETON, 'Tieton River')
	)
	river = models.CharField(max_length=64,
							choices=River_Choices,
							null=True)

	KAYAK = 'Kayak'
	RAFT = 'Raft'
	TRIP_TYPE_CHOICES = (
		(KAYAK, 'Kayak'),
		(RAFT, 'Raft')
	)
	trip_type = models.CharField(max_length=64,
							choices=TRIP_TYPE_CHOICES,
								null=True)

	# MAKE THIS A BOOLEAN NOT A DROPDOWN. UNUSED INFO, CONVOLUTES THE POINT
	leader = models.ForeignKey('guide', unique=False, null=True, blank=True, related_name='leader', related_query_name='leader')
	# guides = models.ForeignKey('guide', unique=False, null=True, blank=True, related_name='guides', related_query_name='guides')

	rafts = models.IntegerField(null=True, 
								blank=True)
	kayaks = models.IntegerField(null=True, 
								blank=True)
	waterLevel = models.CharField(max_length=50, null=True, blank=True)
	weather = models.TextField(max_length=356,
								null=True,
								blank=True)
	general_description = models.TextField(max_length=356,
								null=True,
								blank=True)
	problems = models.TextField(max_length=356,
								null=True,
								blank=True)
	guest_problems = models.TextField(max_length=356,
								null=True,
								blank=True)
	



	def post(self):
		self.editDate = timezone.now()
		self.save

	def __str__(self):
		river = self.river
		guide = self.guide.LastName
		date = str(self.date)
		desc = date + ' - ' + guide + ' - ' + river
		return desc



class Guide(models.Model):
	FirstName = models.CharField(max_length=64)
	LastName = models.CharField(max_length=64)

	password = models.CharField(max_length=32)
	FULL_TIME = 'FT'
	PART_TIME = 'PT'
	ON_CALL = 'OC'
	EMPLOYMENT_CHOICES = (
		(FULL_TIME, 'Full Time'),
		(PART_TIME, 'Part Time'),
		(ON_CALL, 'On Call')
	)
	employee_type = models.CharField(max_length=2,
									choices=EMPLOYMENT_CHOICES)

	def __str__(self):
		return self.LastName







