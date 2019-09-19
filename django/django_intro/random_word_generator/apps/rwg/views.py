from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    get_random_word  = get_random_string (length=14)
    context  =  {'random_word_generator' : get_random_word }
    return render( request, 'rwg/index.html', context=context)

def generate(request):
    return redirect("/")
