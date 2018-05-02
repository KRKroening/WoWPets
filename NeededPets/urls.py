from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:creatureId>/individualPage/',views.individualPage, name='individualPage'),
    path('UpdateNeededCollection/', views.UpdateNeededCollection, name='UpdateNeededCollection'),
    path('<int:creatureId>/RemoveFromCollection/', views.RemoveFromCollection, name='RemoveFromCollection')

]