from csk.views import *
from django.urls import path

app_name='something'

urlpatterns=[
    path('msd/',msd,name='msd'),
    path('dhoni/',dhoni,name='dhoni'),
]
