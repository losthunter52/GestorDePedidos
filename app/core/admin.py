from django.contrib import admin
from core.models import *

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'email')
    fields = ['nome', 'cpf', 'email']

admin.site.register(Cliente, ClienteAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'categoria')
    fields = ['descricao', 'categoria']

admin.site.register(Item, ItemAdmin)