from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .models import reader, book
from .forms import *

# Create your views here.

def home(request):
    return render(request,'home.html',context={"current_tab": "home"})

def index(request):
    return render(request,'index.html',context={"current_tab": "index"})



def readers_tab(request):
    readers=reader.objects.all()
    return render(request,'readers.html',context={"current_tab": "readers","readers":readers})

def books_tab(request):
    books=book.objects.all()
    return render(request,'books.html',context={"current_tab": "books","books":books})
    

