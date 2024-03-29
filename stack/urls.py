from django.urls import path

from . import views

app_name = 'stack'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('delete', views.delete, name='delete'),
]