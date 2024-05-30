from django.shortcuts import render

from chats.models import Chat

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
    
    context = {"chat":chat}

    return render(request, "core/index.html", context)