from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "mi_nav_bar.html")
def login(request):
    return render (request, "my_login.html")