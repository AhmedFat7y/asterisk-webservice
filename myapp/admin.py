from django.contrib import admin
from myapp.models import Client, Server
# Register your models here.

admin.site.register(Client)
admin.site.register(Server)