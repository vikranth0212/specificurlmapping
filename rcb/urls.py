from rcb.views import *
from django.urls import path
app_name='anything'
urlpatterns=[
    path('virat/',virat,name='virat'),
    path('kohli/',kohli,name='kohli'),
]