from django.urls import path

from . import views

urlpatterns = [
    path('animals/', views.animals, name='animals')
]