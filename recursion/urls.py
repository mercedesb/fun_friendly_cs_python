from django.urls import path

from . import views

app_name = 'recursion'
urlpatterns = [
    path('', views.index, name='index'),
    path('count', views.count, name='count'),
]