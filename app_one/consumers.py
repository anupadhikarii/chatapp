'''
    django websocket topic implemented here
'''
from channels.consumer import AsyncConsumer,SyncConsumer ,StopConsumer, async_to_sync
from time import sleep
from app_one.models import global_message,Room_message,Rooms
from app_one.chatBot import chatbot_responce
import json

#-----------------------------------------------------------------------
#global chatroom

class Mysync(SyncConsumer):

    def websocket_connect(self,event):

        async_to_sync(self.channel_layer.group_add)('global2',self.channel_name)  
        self.send({
            'type':'websocket.accept'
        })

    def websocket_receive(self,event):
        data = json.loads(event['text'])                      #str into python dict obj
        message_global_save = global_message(message=data['msg'], message_send_by=data['user'])       #message being saved in database with user who send it
        message_global_save.save()

        async_to_sync(self.channel_layer.group_send)('global2',{
            'type':'chat_messages',
            'text': event['text']
        })
        

    def chat_messages(self,event):
        self.send({
            'type':'websocket.send',
            'text': event['text']
        })


    def websocket_disconnect(self,event):
        raise StopConsumer()
#-----------------------------------------------------------------------
# Room
class Myprivateroom(SyncConsumer):
  


    def websocket_connect(self,event):
        
          self.name= self.scope['url_route']['kwargs']['roomname']
          async_to_sync(self.channel_layer.group_add)(self.name, self.channel_name)
          self.send({
              'type':'websocket.accept'
          })

    def websocket_receive(self,event):
        data = json.loads(event['text'])
        room_name = Rooms.objects.get(room = self.name)
        Room_message_save = Room_message(room=room_name,room_message=data['msg'],message_send_by=data['user']  ) #message being saved
        Room_message_save.save()
        
        async_to_sync(self.channel_layer.group_send)(self.name, {
              'type':'chat.message',
              'message': event['text']
          })
    
    def chat_message(self,event):
        self.send({
              'type':'websocket.send',
              'text': event['message']
          })

    def websocket_disconnect(self,event):
        raise StopConsumer()

#-----------------------------------------------------------------------
#Here chat bot reply after catching the message coming from Frontend 
# Reply message comes from chatbot.py file
  
class Bot_reply(SyncConsumer):
    def websocket_connect(self,event):
        
         self.send({
            'type':'websocket.accept'
        })

    def websocket_receive(self,event):
        data = json.loads(event['text'])
        bot_reply = chatbot_responce(data['msg'])     #reply message
        bot_reply_ = {'msg': bot_reply, 'user':data['user'] , 'user_message':data['msg'] }
        bot_reply_dump = json.dumps(bot_reply_)       #changing str into json format
        print(bot_reply_dump)
        self.send({
            'type':'websocket.send',
            'text': bot_reply_dump
        })
        

    def websocket_disconnect(self,event):
        raise StopConsumer()