from unicodedata import name
from django.shortcuts import render

# Create your views here.

def Index(request):
    return render(request,'index.htm')