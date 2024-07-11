from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-detail'),
    path('directors', views.show_all_directors, name='list-directors'),
    path('directors/<int:id_director>', views.show_one_director, name='director-info'),
]
