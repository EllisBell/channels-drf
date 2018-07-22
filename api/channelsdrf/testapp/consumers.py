from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

class TestConsumer(WebsocketConsumer):
    def connect(self):
        # Join group
        async_to_sync(self.channel_layer.group_add)(
            'test',
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave group
        async_to_sync(self.channel_layer.group_discard)(
            'test',
            self.channel_name
        )

    # Receive message from WebSocket, send to group
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'test_message',
                'message': message
            }
        )

    # Receive message from group
    def test_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))