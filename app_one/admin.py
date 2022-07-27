from django.contrib import admin
from app_one.models import Rooms, global_message ,Room_message
# Register your models here.

admin.site.register(global_message)
admin.site.register(Room_message)

@admin.register(Rooms)
class Rooms_(admin.ModelAdmin):
    list_display = ['id', 'room', 'admin' ]



