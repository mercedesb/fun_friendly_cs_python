from django.urls import path

from . import views

app_name = 'big_o_notation'
urlpatterns = [
    path('', views.index, name='index'),
    path('preheat_oven/<int:batches>', views.preheat_oven, name='preheat_oven'),
    path('combine_butter_and_sugar/<int:batches>', views.combine_butter_and_sugar, name='combine_butter_and_sugar'),
    path('add_eggs/<int:batches>', views.add_eggs, name='add_eggs'),
    path('combine_flour_and_baking_powder/<int:batches>', views.combine_flour_and_baking_powder, name='combine_flour_and_baking_powder'),
    path('combine_milk_flour_and_butter_mixture/<int:batches>', views.combine_milk_flour_and_butter_mixture, name='combine_milk_flour_and_butter_mixture'),
    path('bake/<int:batches>', views.bake, name='bake'),
    path('frost/<int:batches>', views.frost, name='frost'),
]