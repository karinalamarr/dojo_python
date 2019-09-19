from django.shortcuts import render, redirect, HttpResponse
def index(request):
    context = {
    	"name": "Noelle",
    	"favorite_color": "turquoise",
    	"pets": ["Brianna", "Fitz", "Georgie"]
    }
    return render(request, "app1/index.html", context)

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog and fuck you and all of you")

def create(request):
    return redirect(" / ")

def show(request, my_val):
    return HttpResponse("placeholder to display blog number:" + str(int(my_val)))

def edit(request, my_val):
    return HttpResponse("placeholder to edit blog number:" + str(int(my_val)))

def destroy(request, my_val):
    return redirect('/')



