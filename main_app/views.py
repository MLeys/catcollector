from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Cat

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
  # cats/detail.html <- refers to a template
  # render responds to the client
  return render(request, 'cats/detail.html', {'cat': cat})