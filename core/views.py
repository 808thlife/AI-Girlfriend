from django.shortcuts import render

from chats.models import Chat, Message

from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    user = request.user
    chat, created = Chat.objects.get_or_create(user = user)
    return HttpResponseRedirect(reverse("core:chat", kwargs = {"hash":chat.hash}))
    
def chat_view(request, hash):
    try:
        chat = Chat.objects.get(hash = hash)
    except Chat.DoesNotExist:
        return HttpResponseRedirect(reverse("core:index"))
    
    messsages = Message.objects.filter(chat = chat)

    context = {"chat":chat, "messages":messsages}

    return render(request, "core/index.html", context)