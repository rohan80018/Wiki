from re import search
from django.urls import path

from . import views

urlpatterns = [
    path("wiki/", views.index, name="index"),
    path("wiki/new_entry/", views.new_entry, name="new_entry"),
    path("wiki/<str:pk>", views.get_entry, name="data"),
    path("wiki/search/", views.search, name="search"),
    path("wiki/edit/", views.edit, name="edit"),
    path("wiki/edit/<str:pk>", views.save, name="save"),
    path("wiki/random/", views.random_entry, name="random")
]
    # path("wiki/search/<str:pk>", views.get_entry, name="search_data"),