import datetime

from django.shortcuts import render

# Create your views here.

def current_datetime(request): 
    now = datetime.datetime.now () 
    context = {'datetime': now}
    return render (request, 'current_datetime.html', context)
