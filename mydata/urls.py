from django.urls import path
from mydata import views

urlpatterns = [

   
	path('hello/', views.hello_world, name='hello-world'),
   	path("example1/", views.panda_data, name='panda-data'),
   	path('example2/', views.save_panda_data, name='save-panda-data'),
   	path('example3/', views.panda_table, name='panda-table'),
]
