from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def virat(request):
    return render(request,'virat.html')

def kohli(request):
    return HttpResponse('king kohli')
