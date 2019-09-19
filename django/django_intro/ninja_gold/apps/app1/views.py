from django.shortcuts import render, redirect
import random 

def index(request):
    context = {'number' : request.session ['ninjagold']}
    return render(request, 'app1/index.html', context)

def farm(request, methods=['post']):
    print("got request from Farm")
    request.session['ninjagold'] += random.randrange(10,20,1)
    return redirect('/')


def cave(request, methods=['post']):
    print("got request from cave")
    request.session['ninjagold'] += random.randrange(5,10,1)
    return redirect('/')

def house(request, methods=['post']):
    print("got request from house")
    request.session['ninjagold'] += random.randrange(2,5,1)
    return redirect('/')

def casino(request, methods=['post']):
    print("got request from casino")
    request.session['ninjagold'] += random.randrange(-50,50,1)
    return redirect('/')

