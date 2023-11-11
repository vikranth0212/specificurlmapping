from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def msd(request):
    return render(request,'msd.html')

def dhoni(request):
    return HttpResponse('this is dhoni')