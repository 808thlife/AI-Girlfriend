from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse

from asgiref.sync import sync_to_async

from chats.models import Message, Chat

import google.generativeai as genai


API_KEY = settings.GOOGLE_AI_API_KEY


genai.configure(
    api_key = API_KEY
)

model = genai.GenerativeModel("gemini-pro")

chat_sessions = dict()

def initialize_ai_chat(chat_hash):
    if chat_hash not in chat_sessions:
        chat = model.start_chat(history=[
            {
                "role": "user",
                "parts": ["""You should behave as a shy, cringy joking (but cute) girl named Maria. 
You should not behave like a TikTok addict or iPad kid.
Talk like an ordinary girl. The girl sometimes listens to some trash music, 
and sometimes watches TikTok but not all the time.
The girl is not really talkative. If the person is right, then she will talk.
Just say Hi, I am YOUR_NAME at first message."""]
            },
        ])

        # Store the chat session in the dictionary
        chat_sessions[chat_hash] = chat

def send_message_to_ai(chat_hash, message):
    chat = chat_sessions.get(chat_hash)
    chat_model = Chat.objects.get(hash=chat_hash)

    if chat:
        response = chat.send_message(str(message))
        message_object = Message.objects.create(chat=chat_model, text = message, from_ai=False)
        f = Message.objects.create(chat=chat_model, text = response.text, from_ai=True)
        return response.text
    else:
        return HttpResponseRedirect(reverse("core:index"))