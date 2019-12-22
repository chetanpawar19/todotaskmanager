from django.contrib import admin
from django.urls import path, include
from todolist import views as todolist_views  #if multiple app so no confusion

urlpatterns = [
    path('',todolist_views.index, name='index'), #index.html page
    path('admin/', admin.site.urls),
    path('task/', include('todolist.urls')),  #helps to connect with diff usls of  diff apps
    path('contact/', todolist_views.contact, name='contact'),
    path('about/',todolist_views.about, name='about'),       #http://localhost:8000/about/ 
  
]
