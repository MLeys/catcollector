
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
	



	path('toys/', views.ToyList.as_view(), name='toys_index'),
	path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
	path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),


	path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
	path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),


  # associate a toy with a cat (M:M)
  	path('cats/<int:cat_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
	path('cats/<int:cat_id>/unassoc_toy/<int:toy_id>/', views.unassoc_toy, name='unassoc_toy'),
	path('accounts/signup/', views.signup, name='signup'),
]