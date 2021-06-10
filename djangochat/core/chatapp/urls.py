from django.conf import urls
from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

app_name='chat'

urlpatterns=[path('',views.index,name='index'),
path('<str:room_name>/',views.room,name='room')
]