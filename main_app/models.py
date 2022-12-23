from django.db import models
from django.urls import reverse # aka a way to redirect
# Create your models here.


# all intances of Cat, since there is a One to Many relationship to Feedings
# We can access the many side
# <model instance>.<many side lowercase model name>_set
# cat.feeding_set.get(id=3)
# cat.feeding_set.all() find all the feedings that belong to the cat
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



# adding this below the Cat model, since we have to relate to it, 
# SO Cat must defined before we create relationship

MEALS = (
	('B', 'Breakfast'),
	('L', 'Lunch'),
	('D', 'Dinner'),
)


class Feeding(models.Model):
	date = models.DateField('Feeding date')
	meal = models.CharField(
		max_length=1,
		# this will help us make a select menu when a form is created from this model
		choices=MEALS, 
		default=MEALS[0][0])

	# create a cat_id FK (Cat is our model)
	cat = models.ForeignKey(Cat, on_delete=models.CASCADE) # <- If you delete cat, delete all the feeding associated with the cat as well
	
	def __str__(self):
		# get_meal_display() is a method django creates for  Charfields that have choices (Select menu)
		# get_<property name>_display() -> automatically shows the humnan readable value, so if meal's value is "B", the method
		# will return Breakfast, (look at the tuple!)
		return f"{self.get_meal_display()} on {self.date}"


