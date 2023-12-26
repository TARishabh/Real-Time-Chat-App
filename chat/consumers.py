import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    # connect method for initial request that comes from the client.
    
    def connect(self):
        self.room_group_name = 'test' # this will come from frontend
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept() # accept the connection from client.
        
        '''
        # self.send(text_data=json.dumps({
        #     'type': 'connection_established',
        #     'message': 'You are now connected!!'
        # }))
        '''
    
    # when we recieve messages from the client.
    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # print('Message:',message)
        
        '''
        # self.send(text_data=json.dumps({
        #     'type':'chat',
        #     'message':message
        # }))
        '''
        
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message
            }
        )
    
    def chat_message(self,event):
        message = event['message']
        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message
        }))

    ''' when a client disconnects from the consumer.'''
    # def disconnect(self, code):
    #     return super().disconnect(code)
