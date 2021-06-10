from django.shortcuts import render
from django.urls.conf import re_path

# Create your views here.

def index(request):
    return render(request,'chatapp/index.html',{})



def room(request,room_name):
    return render(request,'chatapp/chatroom.html',{'room_name':room_name})
