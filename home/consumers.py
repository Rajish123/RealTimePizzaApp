from channels.generic.websocket import WebsocketConsumer
import json
from .models import *   
from asgiref.sync import async_to_sync

class OrderProgress(WebsocketConsumer):
    def connect(self):
        # get order_id from asgi.py
        self.room_name = self.scope['url_route']['kwargs']['order_id']
        self.room_group_name = 'order_%s' % self.room_name
        print("Connect")
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        order = Order.giver_order_detail(self.room_name)
        self.send(text_data = json.dumps({
            'payload':order
        }))

    def receive(self,text_data):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'order_status',
                'payload':text_data
            }
        )

    def order_status(self,event):
        order = json.loads(event['value'])
        self.send(text_data = json.dumps({
            'payload':order
        }))

    def disconnect(self,close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

