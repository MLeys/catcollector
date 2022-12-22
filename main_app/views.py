from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

##############################################
# THIS IS SIMULATING A MODEL, JUST FOR TODAY, 
# SO WE HAVE DATA TO INJECT INTO OUR TEMPLATES
class Cat:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

# This the array, we are injecting into the template
cats = [
  Cat('Lolo', 'tabby', 'foul little demon', 3),
  Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Cat('Raven', 'black tripod', '3 legged cat', 4)
]


# After this lesson this code will not be used
# because we'll use a REAL MODEL that can talk to 
# the DB
##############################################

def home(request):
	return render(request, 'home.html')


def about(request):
	return render(request, 'about.html')


def cats_index(request):
	# the key on the dictionary is the variable name
	# in the template (index.html)
	return render(request, 'cats/index.html', {'cats': cats})