from django.shortcuts import render, get_object_or_404
from .models import ChatRoom


def index(request):
    chatrooms = ChatRoom.objects.all()
    return render(
        request,
        "chatrooms/index.html",
        {"chatrooms": chatrooms},
    )


def chats(request, slug):
    chatroom = get_object_or_404(ChatRoom, slug=slug)
    messages = chatroom.messages.order_by("timestamp")

    return render(request, "chatrooms/chats.html", {
        "chatrooms": chatroom,
        "messages": messages,
    })