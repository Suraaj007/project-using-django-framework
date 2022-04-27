from django.contrib import admin
from django.urls import path
from Home import views


urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('contacts',views.contacts,name='contacts'),
    path('services2',views.services2,name='services2')

]

