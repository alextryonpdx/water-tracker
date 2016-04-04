from django.db import models
from django.utils import timezone

# Create your models here.
class Entry(models.Model):
	employee = models.ForeignKey('auth.User')
	editDate = models.DateTimeField(
            default=timezone.now)
	date = models.DateTimeField(
		blank=True, null=False)
	waterLevel = models.CharField(max_length=50)


	def post(self):
		self.editDate = timezone.now()
		self.save

	def __str__(self):
		return self.waterLevel