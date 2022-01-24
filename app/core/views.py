from django.shortcuts import render
from core.models import *
from django.views.generic import ListView, DetailView

# Generico

def index(request):
    num_clientes = Cliente.objects.all().count()
    num_itens = Item.objects.all().count()
    num_pedidos = Pedido.objects.all().count()
    num_visits = request.session.get('num_visits', 0)
    context = {
        'num_clientes': num_clientes,
        'num_itens': num_itens,
        'num_pedidos': num_pedidos,
        'num_visits': num_visits,
    }
    template_name = 'home.html'
    return render(request, template_name, context) 

# Cliente

class listaCliente(ListView):
    template_name = 'listaCliente.html'
    context_object_name = 'cliente_list'

    def get_queryset(self):
        return Cliente.objects.all()    

# Item

class listaItem(ListView):
    template_name = 'listaItem.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        return Item.objects.all()   

#Pedido

class listaPedido(ListView):
    template_name = 'listaPedido.html'
    context_object_name = 'pedido_list'

    def get_queryset(self):
        return Pedido.objects.all()                   