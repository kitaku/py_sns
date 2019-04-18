from django.contrib import admin

from .models import Message,Friend,Good

admin.site.register(Message)
admin.site.register(Friend)
admin.site.register(Good)

# Register your models here.
