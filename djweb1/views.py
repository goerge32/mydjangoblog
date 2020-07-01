from django.shortcuts import render
from django.shortcuts import HttpResponse
 

def about(request):
    #return HttpResponse('hi there')
    return render(request, 'about.html' )

def home(request):
    #return HttpResponse('home')
    return render(request, 'home.html' )

def mainRoom(request):
    #return HttpResponse('main room is here!')
    return render(request, 'mainRoom.html')