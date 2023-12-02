from django.shortcuts import render

from django.http import HttpResponse
def home(res):
    return render(res , 'home.html')