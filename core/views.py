from django.shortcuts import render

from chats.models import Chat, Message

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    user = request.user
    chat, created = Chat.objects.get_or_create(user = user)
    return HttpResponseRedirect(reverse("core:chat", kwargs = {"hash":chat.hash}))

@login_required
def chat_view(request, hash):
    try:
        chat = Chat.objects.get(hash = hash)
    except Chat.DoesNotExist:
        return HttpResponseRedirect(reverse("core:index"))
    
    messsages = Message.objects.filter(chat = chat)

    context = {"chat":chat, "messages":messsages}

    return render(request, "core/index.html", context)

@login_required
def delete_chat(request):
    chat = Chat.objects.get(user=request.user)
    chat.delete()
    return HttpResponseRedirect(reverse("core:index"))

def login_view(request):
    return render(request, "core/login.html")

def signup_view(request):
    return render(request, "core/signup.html")

