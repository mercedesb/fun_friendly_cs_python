from django.urls import path
from . import views

app_name = 'tree'
urlpatterns = [
    path('', views.index, name='index'),
    path('harry_worst_iterative', views.harry_worst_iterative, name='harry_worst_iterative'),
    path('harry_worst_recursive', views.harry_worst_recursive, name='harry_worst_recursive'),
    path('harry_best_iterative', views.harry_best_iterative, name='harry_best_iterative'),
    path('harry_best_recursive', views.harry_best_recursive, name='harry_best_recursive'),
    path('cedric_worst_iterative', views.cedric_worst_iterative, name='cedric_worst_iterative'),
    path('cedric_worst_recursive', views.cedric_worst_recursive, name='cedric_worst_recursive'),
    path('cedric_best_iterative', views.cedric_best_iterative, name='cedric_best_iterative'),
    path('cedric_best_recursive', views.cedric_best_recursive, name='cedric_best_recursive'),
]