from django.urls import path
from . import views

urlpatterns = [
    path('<int:deck_id>/options/', views.options, name='options'),
    path('<int:deck_id>/add_card/', views.add_card, name='add_card'),
    path('<int:deck_id>/study/', views.study, name='study'),
]