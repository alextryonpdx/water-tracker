from django.db import models
from django.utils import timezone
from django import forms

# Create your models here.
class Entry(models.Model):
	guide = models.ForeignKey('guide')
	editDate = models.DateTimeField(
            default=timezone.now)
	date = models.DateTimeField(
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
	leader = models.BooleanField(default=False)
	rafts = models.IntegerField(null=True, 
								blank=True)
	kayaks = models.IntegerField(null=True, 
								blank=True)
	waterLevel = models.CharField(max_length=50)
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
		return self.river



class Guide(models.Model):
	FirstName = models.CharField(max_length=64)
	LastName = models.CharField(max_length=64)

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







