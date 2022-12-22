from django.db import models

# Create your models here.
class Cat(models.Model):
	# we're defining the columns and constraints on the rows for each column
	name = models.CharField(max_length=100)
	breed = models.CharField(max_length=100)
	description = models.TextField(max_length=250)
	age = models.IntegerField()