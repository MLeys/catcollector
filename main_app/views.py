from django.shortcuts import render, redirect


# import the cbv
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# Create your views here.
from django.http import HttpResponse
from .models import Cat, Toy
from .forms import FeedingForm



def add_feeding(request, cat_id):
  # create a ModelForm instance using the data from the 
  # post request (when our form submits from the client to server)
  # request.POST is the contents of the form, when submitted
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # save an instance in memoery
    new_feeding = form.save(commit=False)
    # new_feeding.cat_id comes from the model key on Feeding called cat
    # remember the _id is automatically appended to it 
    new_feeding.cat_id = cat_id
    new_feeding.save()
    # we always redirect when we change data in the database
    # in this case we added a feeding to a cat
    # cat_id on the left refers to the param in url
    # cats/<int:cat_id>/' for the details
    # cat_id on the right is referring to the actually id, we 
    # reusing the cat_id from form submission that is argument to add_feeding 
    # function above
  return redirect('detail', cat_id=cat_id)


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
  fields = ['name', 'breed', 'description', 'age'] # two _ this specifies every field on the model (all keys)
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
  toys_cat_doesnt_have = Toy.objects.exclude(id__in = cat.toys.all().values_list('id'))


  # instiate our form class, to create a form from the class 
  # feeding_form is the instance of our class, aka a form
  feeding_form = FeedingForm()
  # cats/detail.html <- refers to a template
  # render responds to the client
  return render(request, 'cats/detail.html', 
    {
      'cat': cat, 
      'feeding_form': feeding_form,
      'toys': toys_cat_doesnt_have
    })


def assoc_toy(request, cat_id, toy_id):
  # Note that you can pass a toy's id instead of the whole object
  Cat.objects.get(id=cat_id).toys.add(toy_id)
  return redirect('detail', cat_id=cat_id)


class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'