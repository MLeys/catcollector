from django.shortcuts import render


# import the cbv
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
from django.http import HttpResponse
from .models import Cat
from .forms import FeedingForm


class CatUpdate(UpdateView):
  model = Cat
  # disallow the update of the name
  fields = ['breed', 'description', 'age']
  # the is redirect happens on the model def get_absolute_url

# Template expectation (the same as create it reuses the page!)
# templates/<name of app>/<model name>_form.html
# example: templates/main_app/cat_form.html



class CatDelete(DeleteView):
  model = Cat
  # want to define the success_url, since when we delete something we can't redirect to the detail page
  success_url = '/cats/' # <- redirects to the cats_index page




# CREATE for our cats
# this will handle the Post request
# and the get request which renders the form!
class CatCreate(CreateView):
  model = Cat 
  
  # specify what fields we want on our form
  # ['name', 'breed', 'description'] <- specify whats keys from the model
  # in a list
  fields = '__all__' # two _ this specifies every field on the model (all keys)
# CONVENTION ALERT!
# CBV expects a template with the following naming
# templates/<name of app>/<model name>_form.html
# example: templates/main_app/cat_form.html

### REDIRECT is on the model for the POST ^


def home(request):
	return render(request, 'home.html')


def about(request):
	return render(request, 'about.html')


def cats_index(request):
	# the key on the dictionary is the variable name
	# in the template (index.html)
  #Cat is our model, that can talk to sql and retrieve all the rows in our table
  cats = Cat.objects.all()
  return render(request, 'cats/index.html', {'cats': cats})


# cat_id is coming from the urls.py, params 
#path('cats/<int:cat_id>/' <--------
# they must be the same, Django convention!
def cats_detail(request, cat_id):
  # use our model Cat (Capital cat) to retrieve whatever row
  # from our db the cat_id matches
  cat = Cat.objects.get(id=cat_id)

  # instiate our form class, to create a form from the class 
  # feeding_form is the instance of our class, aka a form
  feeding_form = FeedingForm()
  # cats/detail.html <- refers to a template
  # render responds to the client
  return render(request, 'cats/detail.html', {'cat': cat, 'feeding_form': feeding_form})