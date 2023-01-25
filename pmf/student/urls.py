from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.student_registration, name='student-registration'),
    path('', views.student_table, name='student-table')
]
