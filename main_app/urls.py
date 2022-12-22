from django.urls import path

# from . says import all the functions in the 
# views file and attach them to the views object
from . import views

#SPELLING IMPORTANT
urlpatterns = [
	# localhost:8000 (the catcollector.urls is '')
	path('', views.home, name='home'), 
	path('about/', views.about, name='about'),
	path('cats/', views.cats_index, name='index'),
]