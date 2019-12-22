from todolist import views
from django.urls import path

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('delete/<id>', views.deletetask, name='delete'),      #http://localhost:8000/task/delete/8
    path('edit/<id>', views.edittask, name='edit'), #http://localhost:8000/task/edit/1
    path('completetask/<id>',views.completetask, name='completetask'),
    path('pendingtask/<id>',views.pendingtask, name='pendingtask'),
    ]
  