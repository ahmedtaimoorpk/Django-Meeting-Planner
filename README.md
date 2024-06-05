# Django-Meeting-Planner 

> Django, Sqlite

## Install the latest Django release

`python -m pip install django`

## starting the project

`django-admin startproject __my-project-name__` (eg. meeting_planner)

## Run the development server

`python manage.py runserver` <mark>makesure your inside an app</mark>

## Stop server

Ctrl + C

## Add a new App

`python manage.py startapp __appname__`  make sure to add the app inside <mark>settings.py ==>`INSTALLED_APPS
= []</mark>

## Migrations

`python manage.py show migrations` to see pending migrations <br>
`python manage.py makemigrations` prepare database changes from models <br>
`python manage.py migrate` apply model changes to database <br>

## Create Database Tables in Django Admin

open admin.py file inside the app <br>
`from .models import __Model Name__` <br>
`admin.site.register(__Model Name__)`

## Create Django Admin Superuser

`python manage.py createsuperuser`

## Make Static Folder Global at Root

Add `STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]`
in settings.py

## Create modelForms

Add `from django.forms import modelform_factory` in views.py

## ModelForms example
    from datetime import date

    from django.forms import ModelForm, DateInput, TimeInput, TextInput, IntegerField
    from django.core.exceptions import ValidationError

    from .models import Meeting


    class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={"type": "date"}),
            'start': DateInput(attrs={"type": "time"}),
            'duration': DateInput(attrs={"type": "number", "min": "1", "max": "4"}),
        }

    def clean_date(self):
        d = self.cleaned_data.get("date")
        if d < date.today():
            raise ValidationError("Meeting cannot be in the past")
        return d



