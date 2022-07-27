
from django.urls import path
from app_one import views
urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.login, name='login'),
    path('sighup',views.sigh_up, name='sigh_up'),
    path('logout',views.logout, name='logout'),
    path('password_changing',views.password_changing, name='password_changing'),
    path('profile',views.profile_view, name='profile'),
    path('join_room',views.join_room, name='join_room'),
    path('secure_room', views.secure_room, name='secure_room'),
    path('globalroom', views.globalroom, name='globalroom' )
    
]