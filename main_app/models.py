from django.db import models
from django.urls import reverse # aka a way to redirect
# Create your models here.
class Cat(models.Model):
	# we're defining the columns and constraints on the rows for each column
	name = models.CharField(max_length=100)
	breed = models.CharField(max_length=100)
	description = models.TextField(max_length=250)
	age = models.IntegerField()

	# THIS HANDLES REDIRECTS FOR OUR CBV's
	def get_absolute_url(self):
		# first argument is a name of a url (looks at kwargs in urls.py)
		# self.id is referring to the id of the cat you just 
		# created and or updated
		return reverse('detail', kwargs={'cat_id': self.id})