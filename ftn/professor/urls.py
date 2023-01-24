from django.urls import path
from . import views

urlpatterns = [
    path('', views.professor_registration, name='professor-registration'),
]
