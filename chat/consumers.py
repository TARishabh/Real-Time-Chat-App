import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    # connect method for initial request that comes from the client.
    
    def connect(self): 
        self.accept() # accept the connection from client.
        self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'You are now connected!!'
        }))
        
    
    # when we recieve messages from the client.
    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print('Message:',message)
        
        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message
        }))
    
    
    # when a client disconnects from the consumer.
    # def disconnect(self, code):
    #     return super().disconnect(code)
