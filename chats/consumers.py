import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer

from asgiref.sync import sync_to_async

from ai_api.utils import chat_sessions, initialize_ai_chat


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
        message = text_data_json['message']
        self.send(text_data=json.dumps({
            'message': message
        }))

    #by chat i meant chat_hash.

    def create_message(self, chat):
        pass

    async def greeting(self, chat):
        pass
    
    async def response(self, chat):
        pass