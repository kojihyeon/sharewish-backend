from django.urls import path
from .views import create_sharewish_entry

urlpatterns = [
    path("add-entry/", create_sharewish_entry, name="add-entry"),
]