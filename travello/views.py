from django.shortcuts import render
from .models import Destination

# Create your views here.

def essay(request):
    return render(request,"essayhome.html")

def world(request):
    return render(request,"world.html")

def Uno(request):
    return render(request,"Uno.html")

def Smarttaps(request):
    return render(request,"Smart-taps.html")

def protohome(request):
    dests= Destination.objects.all()
    return render(request,"protohome.html",{'dests':dests})

def essaynuclear(request):
    return render(request,"essaynuclear.html")

def essayair(request):
    return render(request,"essayair.html")

def index(request):
    dests= Destination.objects.all()

    return render(request,"index.html",{'dests':dests})

def prototypes(request):
    return render(request,"prototypes.html")

