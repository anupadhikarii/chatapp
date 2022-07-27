from django import forms
from app_one import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import  *

#-------------------------------------------------------------
#sighup from 

class sighupForm(UserCreationForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'type':"username",
            'class':"form-control",
            'id':"username", 
            'name':'text',
            "placeholder":"username"
        })
        self.fields['email'].widget.attrs.update({
            'type':"email",
            'class':"form-control",
            'id':"email", 
            'name':'email',
            "placeholder":"email"
        })
        self.fields['password1'].widget.attrs.update({
            'type':"password",
            'class':"form-control",
            'id':"password", 
            'name':'password1',
            "placeholder":"password"
        })
        self.fields['password2'].widget.attrs.update({
            'type':"password2",
            'class':"form-control",
            'id':"password2", 
            'name':'password',
            "placeholder":"Confirm-Password"
        })
    class Meta:        
        model = User
        fields = ['username','email','password1','password2']

#-----------------------------------------------------------
#user password changing form 

class Password_changing_form(PasswordChangeForm):
     def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({
            'type':"password",
            'value': "",
            'class':"form-control",
            'id':"id_old_password", 
            'name':'old_password',
            "placeholder":"Current Password"
        })
        self.fields['new_password1'].widget.attrs.update({
            'type':"password",
            'class':"form-control",
            'id':"new_password1", 
            'name':'old_password1',
            "placeholder":"New Password"
        })
        self.fields['new_password2'].widget.attrs.update({
            'type':"password",
            'class':"form-control",
            'id':"new_password2", 
            'name':'old_password2',
            "placeholder":"confirm Password"
        })
    
    
     class Meta:    
          model = User

#------------------------------------------------------------------------
# user detail changing form

class User_option_form(UserChangeForm):

     def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class':"form-control",
            "placeholder":"username"
        })
        self.fields['first_name'].widget.attrs.update({
            'class':"form-control",
            "placeholder":"first_name"
        })
        self.fields['last_name'].widget.attrs.update({
            'class':"form-control",
            "placeholder":"last_name"
        })
        self.fields['email'].widget.attrs.update({
            'class':"form-control",
            "placeholder":"email",
            
        })   
    
        password = None
        class Meta:
            model = User
            fields =[ 'username','first_name','last_name','email']
            label = {'enail':'Email'}

