from django.urls import path
from .views import create_sharewish_entry, get_sharewish_entries

urlpatterns = [
    path("add-entry/", create_sharewish_entry, name="add-entry"),
    path('entries/', get_sharewish_entries, name='get_sharewish_entries'),
]