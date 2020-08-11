
## Python with Django

Please find the steps to implement the Django Project

* Installation  Steps:

```
* pip install Django
* django-admin startproject project
* python manage.py runserver
* django-admin startapp user
```

* Understanding different scripts in Django

```
* URL.py --> URL Configuration script<br>
* form.py --> Form/Attribute creation scripts<br>
* models.py --> script which creates database schemas(class name would be considered as table name)<br>
* views.py --> script which takes in web request and throws web response(logic is written here to save the form and send the respective attributes to DB)<br>
* Settings.py --> script which contains default settings. we can add configurations like custom password validation and "app" name in here<br>
```

* Evaluation:

```
* python manage.py runserver<br>
* go to chrome and type http:127.0.0.1/ <br>
* register using your username(details like username, password, confirm password and emails should be entered) <br>
* login using your username(details like username, password should be entered) <br>
* create profile after login(details like firstname, lastname, contactno,email,.... should be entered) <br>
* To generate SQL commands to create the table --> python manage.py makemigrations
* To create the table in database  --> python manage.py migrate
* check the SQLLite DB Browser to view details of user profile
```
