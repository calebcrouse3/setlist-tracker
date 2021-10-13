# Steps for django project

create project folder (or just use github repo) \
`mkdir setlist_tracker` \
`cd setlist_tracker`

create virtual env \
`virtualenv env` \
`source env/bin/activate` \
`pi3p install django`

create django project \
`django-admin startproject setlist_tracker .` \
pst ( dont forget the dot ".") \

create data base \
`python manage.py migrate`

start server \
`python manage.py runserver`

create an app within the project \
`python manage.py startapp setlist_tracker_app`

folder structure should look like \
`ls setlist_tracker`
```
|-env
|-db.sqlite3
|-manage.py
|-setlist_tracker (main project)
|-setlist_tracker_app (main app)
```

define models in `setlist_tracker_app/models.py`

add app to project in `settings.py`
```
INSTALLED_APPS = [
    # my apps
    'setlist_tracker_app'

    ...
]
```

make migration files for new models \
`python manage.py makemigrations setlist_tracker_app`

apply migrations \
`python manage.py migrate`

create super user \
`python manage.py createsuperuser` \
`user: admin` \
`password hint: classic jazz`

register models with the admin site in `admin.py`

check out admin site to make sure things are working \
`http://localhost:8000/admin/`

add song tracker app urls file to main `urls.py` file
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('song_tracker_app.urls')),
]
```
create `urls.py` in song_tracker_app and add home page url pattern \


create new function in `setlist_tracker_app/views.py` to map url patterns to functions and templates \


create new folder to hold templates \
`mkdir setlist_tracker/setlist_tracker_app/templates/setlist_tracker_app` (is a little weird but thats the best structure to not confuse django) \


create new `index.html` file
