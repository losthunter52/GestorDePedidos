from django.shortcuts import render
from core.models import *

# Create your views here.
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