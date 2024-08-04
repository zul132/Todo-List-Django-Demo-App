from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here. Views can be created for different routes that we can access on our website
def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})