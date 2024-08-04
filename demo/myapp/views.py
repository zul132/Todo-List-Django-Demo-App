from django.shortcuts import render, HttpResponse

# Create your views here. Views can be created for different routes that we can access on our website
def home(request):
    return render(request, "home.html")