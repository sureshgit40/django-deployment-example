from django.conf.urls import url
from django.urls import path
from basic_app import views

#Template tagging
app_name = 'basic_app' # say django check in basic _app & find url

urlpatterns= [
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
]
