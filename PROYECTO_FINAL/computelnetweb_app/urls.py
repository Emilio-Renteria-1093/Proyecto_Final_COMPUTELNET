from django.urls import path
from computelnetweb_app import views

urlpatterns=[
    path("",views.inicio_vista,name="views.inicio_vista")
]