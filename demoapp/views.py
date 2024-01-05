from wsgiref.simple_server import demo_app
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"data":"Home Page of Django App, testing CD, lol haha"}
    return render(request,'demoapp/index.html', context)
