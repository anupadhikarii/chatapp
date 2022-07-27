'''
    simple chatbot feature that replys few this  caught
    programmed using regression modeule, If else statement, loops anf functions
'''

import re
import random



#---------------------------------------------------------------------------------------
def chatbot_responce2(message):
    if re.findall('yourself', message):
       return 'My name is Riya and i am Bot'
    elif re.findall('your age?',message):
        return 'i am 22 years old lady robot'
    elif re.findall ('boyfriend ?',message ):    
        return ' i have boyfriend he is Anup Adhikary  one who programmed me hehe '
    elif re.findall ('boyfriend ',message ):
        return  ' No i am sorry i am bot '
    elif re.findall ('project',message ):
        return  ' This project is built by Mrs Anup adhikary. This python django project is completely about chating implemented by using websocket.To chat you should create Room First. Every chat message are store in Database so you can see message on room although you were not online. Their is  global chat option Too'        
    elif re.findall('hi',message):
        return ' hey '        
    elif re.findall('single',message):
        return ' No i am not '
    elif re.findall('too',message):
        return ' oh '             
    else:        
        return 'I didn\'t understood. '        
            



def chatbot_responce(messages):

    compliments = ['beautyfull','sexy','hot', 'talented','beautifull' ]       
    #list of complement
    compliement_replys = ["Thank you, but i know that hehe.","Thank you, you too","haha thnks alot ","ufff your flerting or what? hahah","is it april foolday today? haha",'tell me something i dont know.. Haha kidding']
    # list of reply of complement
    compliement_reply = random.choice(compliement_replys)
    if re.findall('setting', messages):
       return 'on (http://127.0.0.1:8000/profile ) or you can go through button of Topright Corner of Currentpage'
    elif re.findall('room',messages):
        return ' on (http://127.0.0.1:8000/join_room )  Note : RoomSystem is not completely made '
    elif re.findall('changePassword',messages):
        return ' on (http://127.0.0.1:8000/changing_password ) or you con go through Setting on topright corner'
    elif re.findall('profile',messages):
        return ' on (http://127.0.0.1:8000/profile )  or you con go through Setting on topright corner'         
    elif re.findall('help',messages):
        return ' yes! What is it?'
    elif re.findall('i love you',messages):
        return ' i love myself too hehe ' 
    elif re.findall('how are you',messages):
        return ' I am fine, you?'

    elif re.findall('haha',messages):
        return ' why you laughing '        


           
    else:
        num = 1
        while num != 6 :

          for i in compliments:

                if re.search(i,messages):
                  return compliement_reply
                else:
                    num = num + 1                
           
        responce_2 = chatbot_responce2(messages)
        return responce_2
    
#----------------------------------------------------------------------------------------------