from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='todo-home'),
    path('create/', views.create, name='todo-creation')
]
