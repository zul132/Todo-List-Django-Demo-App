#Create your URL routes here and then connect them to your Views.

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("todos/", views.todos, name="Todos")
]
