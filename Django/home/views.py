from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# uma funcao quando eu estiver na home
def home(request):
    print('home')
    return render(request,'home/home.html')