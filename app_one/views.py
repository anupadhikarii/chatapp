'''
     Python Django Chatappication project 
     This project have Authentication: sighup , login, logout, userdetailchange and password changing form 
     websocket implemented( Global chatroom , Riya(chating bot), join and creating room feature, realtime Text communication )
     Every message interaction are saved in database . Database used is DBSQlite

'''
#-------------------------------------------------------------------------------------------------------------
from email import message
from django.shortcuts import redirect, render, HttpResponseRedirect, HttpResponse
from django.contrib import auth, messages
from .forms import Password_changing_form, User_option_form, sighupForm
from app_one.models import global_message, Rooms,User,Room_message
from .chatBot import *




# rendering home page
def home(request):
    if request.user.is_authenticated:
       
        users = User.objects.all()
        
        return render(request,'app_one/chat_app.html',{'users':users})
    else:
     
        return redirect('/')   


#------------------------------------------------------------------
#login form 

def login(request):
    
    if request.user.is_authenticated:
   
      return HttpResponseRedirect('home')
   
    else:
   
        if request.method == 'POST':
            
            username = request.POST['username']
            password = request.POST['password']
            
            if username == None :
   
                messages.error(request, 'fill up all')
                return redirect('/')

            else:        
   
                user = auth.authenticate(username = username,  password=password ) 
                
                if user is not None:
    
                    auth.login(request,user)
                    return HttpResponseRedirect('home')
                
                else:
    
                    messages.error(request,'username/password didnot match')
                    return redirect('/')    
            
        else:    
    
            return render(request,'app_one/login.html')    

#----------------------------------------------------------------------
# user sighup form 

def sigh_up(request):
    
    if request.user.is_authenticated:             
   
         return HttpResponseRedirect('home')
   
    else:
    
        if request.method == 'POST':

            username = request.POST['username']
            
            if User.objects.filter(username=username):

                messages.error(request,'username exist')                
                return redirect('sigh_up')

            fm = sighupForm(request.POST)
        
            if fm.is_valid():
        
                fm.save()
                return HttpResponseRedirect('/')
        
            else:
        
                fm = sighupForm()
                messages.error(request, 'plz provide correct keywords')
        
        else:
        
                fm = sighupForm()
        
        return render(request, 'app_one/sigh_up.html',{'forms':fm})

#----------------------------------------------------------------------
# loging out the user

def logout(request):

    auth.logout(request)
    return redirect('/')    

#----------------------------------------------------------------------
# password changingoption

def password_changing(request):
    
    if request.user.is_authenticated:
  
        if request.method == 'POST':
  
            fm = Password_changing_form(request.user,request.POST)
  
            if fm.is_valid():
  
                user = fm.save()
                auth.update_session_auth_hash(request,user)              #--> after sucessfully changing password users session won't expire
                messages.info(request, 'password changed succesfully')
                return HttpResponseRedirect('home')
  
            else:
  
                messages.error(request, 'Error')
  
        else:
  
            fm = Password_changing_form(request.user)

        return render(request, 'app_one/password_changing.html',{'form':fm})    
  
    else:
  
       return HttpResponseRedirect('home')

#----------------------------------------------------------------------
# joinroom pade rendering 

def join_room(request ):
  
    if request.user.is_authenticated:
  
        rooms = Rooms.objects.order_by('?')[:3]       #--> takes only 3 random rooms to show on frontend
        dic = {'rooms':rooms }
                
        messages.info(request,'Note: To Create New room You need to tick Create room cheak box.')      
        return render(request, 'app_one/join_room.html', dic)
    
    else:
         
         return HttpResponseRedirect('home')

#-------------------------------------------------------------------------------------------------------
# changing user details

def profile_view(request):
  
    if request.user.is_authenticated:

        if request.method == 'POST':
  
            fm = User_option_form(request.POST, instance= request.user)
            
            if fm.is_valid():
 
                fm.save()
                messages.success(request,'saved')
 
            else: 

                messages.error(request,'Error couldn\'t be saved')

        else:
 
                fm = User_option_form(instance=request.user) 

        
        dic = {'user_option_form':fm}
        return render(request, 'app_one/profile.html',dic) 
    
    else:
    
        return redirect('/')    

#-------------------------------------------------------------------
# this runs only after providing valid room credentials
# here joining room and creating room is done
def secure_room(request):     
    
        if request.method == 'POST':
        
            admin = request.POST['admin']
            room = request.POST['room']
            password = request.POST['password']
            
            try:
           
             create_new_room = request.POST['create_new_room']              #---->for creating room
           
            except:
           
             create_new_room = 'no_new_room'                                  #---->for joining room
           
            if room == '' or password == '':
        
                messages.error(request,'error')
                return HttpResponseRedirect('join_room')
        
            else:

                if create_new_room == 'create_new_room':                  
                 # creating room 

                 if Rooms.objects.filter(room=room).exists():            #----> to see if room name exist or not
                
                   messages.error(request,'room name already exist')
               
                   return HttpResponseRedirect('join_room')  
                                       
                 else:                                                    #---> thats means room name doesn't exist so room can be created
               
                    new_room = Rooms(admin=admin, room=room, password=password)
                    new_room.save()
                    messages.success(request, ' Room have been sucessfully created .Now you can join the room and can invite your friend')
              
                    return HttpResponseRedirect('join_room')
               
                elif create_new_room == 'no_new_room':                      #--> for joining room
                 
                    if Rooms.objects.filter(room=room).exists():            #--> to weather the room exist or not
              
                     room_password = Rooms.objects.get(room=room)
              
                     if room_password.password == password:
              
                        room_name = Rooms.objects.get(room=room)
                        admin = room_name.admin                      
                        rooms = Rooms.objects.filter(room=room).first()
              
                        if rooms:
              
                            room_messages = Room_message.objects.filter(room=rooms)     #--> retreving message from data base
              
                        else:
                                     
                            room_messages = Room_message.objects.get(room=room)    
                      
                        dic = {'room':room, 'admin':admin,'room_message':room_messages}
              
                        return render (request,'app_one/secureRoom.html', dic )    
                
                     else:
                
                         messages.error(request,'wrong password')
              
                         return HttpResponseRedirect('join_room')
                         
                     
                    else: 

                         messages.error(request,'room name does not exist')
            
                         return HttpResponseRedirect('join_room')
        
        else: 
            return HttpResponseRedirect('/')

#--------------------------------------------------------------
def globalroom(request):
   
    if  global_message.objects.all().count() >= 50:        
    #if global chatroom reaches more then 50 message then 10 message will be deleted  
        
        for i in range(10):
         
            delete_message = global_message.objects.filter().order_by('date')[0]
            delete_message.delete()
    
    globol_messages = global_message.objects.all()     #retriving message from database 
    
    users = User.objects.all()
    dic = {'users':users, 'g_message': globol_messages }
    
    return render(request, 'app_one/globalroom.html',dic)    