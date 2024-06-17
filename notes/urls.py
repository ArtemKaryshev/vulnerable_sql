from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_notes, name='search_notes'),
    path('create/', views.create_note, name='create_note'),
]