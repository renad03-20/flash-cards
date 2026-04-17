from django.urls import path
from . import views

urlpatterns = [
    path('create_deck', views.create_deck, name='create_deck'),
    path('delete_deck/<int:deck_id>', views.delete_deck, name='delete_deck')
]
