from django.urls import path
from . import views

urlpatterns = [

    path('items/', views.item_list, name='item_list'),
    path('items/<int:id>/', views.item_detail, name='item_detail'),

    path('moves/', views.move_list, name='move_list'),
    path('moves/<int:id>/', views.move_detail, name='move_detail'),

    path('pokemons', views.pokemon_list, name='pokemon_list'),
    path('pokemons/', views.pokemon_detail, name='pokemon_search'),

]