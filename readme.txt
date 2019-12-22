
-open side panel - Extensions bar
-search "python"
-click on install
-now search "django"
-click on install base version 0.19.0
-create project folder "todotaskmanager"
-cmd>A:\django\todotaskmanager>pip install virtualenv
-cmd>A:\django\todotaskmanager>python -m venv venv
-cmd>A:\django\todotaskmanager>.\venv\Scripts\activate     
-cmd>(venv) A:\django\todotaskmanager>pip install django
-cmd>(venv) A:\django\todotaskmanager>pip freeze
Django==2.2.7
pytz==2019.3
sqlparse==0.3.0
-cmd>(venv) A:\django\todotaskmanager>django-admin startproject taskmate
-(venv) A:\django\todotaskmanager\taskmate>python manage.py runserver
-brower>localhost:8000
-(venv) A:\django\todotaskmanager\taskmate>python manage.py makemigrations
-(venv) A:\django\todotaskmanager\taskmate>python manage.py migrate
-#create superuser
(venv) A:\django\todotaskmanager\taskmate>python manage.py createsuperuser

username-admin
password-admin 

-(venv) A:\django\todotaskmanager\taskmate>python manage.py startapp todolist
-add 'todolist' app to settings.py - INSTALLED_APPS variable
-main urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', include('todolist.urls')), ]
-create urls.py in todolist app folder

-write todolist fun in views.py in todolist app
-create 'templates' folder.
 create todolisthome.html file in templates
-add 'templates' in settings.py TEMPLATES- DIR variable
-for todolisthome.html, getbootstrap-components-navbar 
-in templates folder, create contact.html, about.html page
-	localhost:8000/task/
	access http://localhost:8000/task/about/
-create 'templates' dir for base template files/comman
-manage base.html jinja2 etc
-block, endblock, DRY urls jinja2
-static folder
 create static folder under project -root
 create js, css, images folder under static folder
 in settings.py, update STATICFILES_DIRS = ['static'] variable
 -base.html
 	-<a class="navbar-brand" href="#"><img src="{% static 'images/applogo.png' %}" alt="ToDoApp"> </a>
 	-{% load static %}
 -check logo appears or not
-check admin panel
http://localhost:8000/admin/
-write models.py
-cmd>(venv) A:\django\todotaskmanager\taskmate>python manage.py makemigrations
-check file '0001_initial.py' under taskmate-todolist-migrations
-cmd>(venv) A:\django\todotaskmanager\taskmate>python manage.py migrate
-register task at admin.py
	from .models import TaskList
	admin.site.register(TaskList)

-(venv) A:\django\todotaskmanager\taskmate>python manage.py runserver
-check admin panel for tasklist task
	add few tasks manually
-views.py getting all tasks from model-db
 display data on todolist.html page
-manage task details in table format todolisthome.html page
-form
	tododlisthome.html add form tag 
	form.py file
	views.py import TaskForm
-add messages
	views.py update
	todolist update
-todolisthome.html table boostrap 
-CRUD
delete functionality
	add url.py
	path('delete/<task_id>', views.deletetask, name='delete'),
	write fun deletetask in view.spy 
	http://localhost:8000/task/delete/8 
	<td> <a href="{% url 'delete' task_obj.id %}">Delete</a></td>  <!--delete link to delete task in todolisthome.html-->
	
edit fuctionality
	urls.py = path('edit/<id>', views.edittask, name='edit'),
	views.py add fun
	create edit.html under templates folder
	write edit.html
	http://localhost:8000/task/edit/1
	update todolisthome.html                               <td>  <a href="{% url 'edit' task_obj.id %}">Edit</a> </td>

complete task/pending task
	urls.py
	views.py fun
	todolisthome.html
	localhost:8000/tasks
-pagination
 views.py   
	from django.core.paginator import Paginator
	views.py update todolist function
	browser>http://localhost:8000/task/?pg=4
	todolisthome.page section after table tag
-index home page
	urls.py
	views.py
	index.html
