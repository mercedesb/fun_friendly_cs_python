from django.urls import path

from . import views

app_name = 'set_theory'
urlpatterns = [
    path('', views.index, name='index'),
    path('intersection', views.intersection, name='intersection'),
    path('union', views.union, name='union'),
    path('difference', views.difference, name='difference'),
    path('relative_complement', views.relative_complement, name='relative_complement'),
    path('symmetric_difference', views.symmetric_difference, name='symmetric_difference'),
]