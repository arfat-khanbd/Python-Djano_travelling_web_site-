from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
   path("", views.index, name='home'),
   path("cal",views.cal, name='cal'),
   path("dtl",views.dtl, name="dtl") 
]

