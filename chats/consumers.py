import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer

from asgiref.sync import sync_to_async

from ai_api.utils import chat_sessions, initialize_ai_chat, send_message_to_ai

from chats.models import Message, Chat


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["hash"]
        self.room_group_name = f"chat_{self.room_name}"

        await sync_to_async(initialize_ai_chat)(self.room_name)
        print("CHAT WAS CREATED!")
        print(len(chat_sessions))

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)
        message = text_data_json['message']
        chat_hash = text_data_json['chat_hash']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type":"chat_message",
                "message":message,
                "chat_hash":chat_hash
            }
        )
       
    async def chat_message(self, event):
        #chat = chat_sessions.get(event['chat_hash'])
        message = event['message']
        chat_hash = event['chat_hash']

        response = await self.send_ai_message(chat_hash=chat_hash, message=message)
        print(response)

        await self.send(text_data = json.dumps({
            "chat_hash":chat_hash,
            "message":response
        }))
    
   # @sync_to_async
    async def send_ai_message(self, chat_hash, message):
        response = await sync_to_async(send_message_to_ai)(chat_hash, message)
        return response  # Directly return the string response

   