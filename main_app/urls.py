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
	path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
	# as_view() must be called on an Class Based View (CBV)
	path('cats/create/', views.CatCreate.as_view(), name='cats_create'),
	# CONVENTION ALERT # CBV's update and delete, they expect params to be called pk (primary key) aka the id
	path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cats_update'),
	path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cats_delete'),
	path('cats/<int:cat_id>/add_feeding/', views.add_feeding, name='add_feeding'),
]