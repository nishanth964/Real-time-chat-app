from django.shortcuts import render, HttpResponse
from .models import ChatRoom

# Create your views here.
def index(request):
    chatrooms=ChatRoom.objects.all()
    context={
        'chatrooms':chatrooms
    }
    return render(request, 'chatrooms/index.html', context)

def chats(request, slug):
    chatrooms=ChatRoom.objects.get(slug=slug)
    context={
        'chatrooms':chatrooms
    }
    return render(request, 'chatrooms/chats.html', context)