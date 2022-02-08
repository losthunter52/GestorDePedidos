from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView

# Generico

def index(request):
    num_clientes = Cliente.objects.all().count()
    num_itens = Item.objects.all().count()
    num_pedidos = Pedido.objects.all().count()
    context = {
        'num_clientes': num_clientes,
        'num_itens': num_itens,
        'num_pedidos': num_pedidos,
    }
    template_name = 'home.html'
    return render(request, template_name, context) 

# Cliente

class listaCliente(ListView):
    template_name = 'listaCliente.html'
    context_object_name = 'cliente_list'

    def get_queryset(self):
        return Cliente.objects.all()    

class detalhesCliente(DetailView):
    model = Cliente
    template_name ='detalhesCliente.html'

def cadastroCliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Cliente')
    form = ClienteForm()

    return render(request,'cadastro.html',{'form': form})

def editarCliente(request, pk, template_name='cadastro.html'):
    clientes = get_object_or_404(Cliente, pk=pk)
    form = ClienteForm(request.POST or None, instance=clientes)
    if form.is_valid():
        form.save()
        return redirect('Cliente')
    return render(request, template_name, {'form':form})    

def excluirCliente(request, pk, template_name='confirm_delete.html'):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method=='POST':
        cliente.delete()
        return redirect('Cliente')
    return render(request, template_name, {'object':cliente})

# Item

class listaItem(ListView):
    template_name = 'listaItem.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        return Item.objects.all()  

def cadastroItem(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Item')
    form = ItemForm()

    return render(request,'cadastro.html',{'form': form})

def editarItem(request, pk, template_name='cadastro.html'):
    itens = get_object_or_404(Item, pk=pk)
    form = ItemForm(request.POST or None, instance=itens)
    if form.is_valid():
        form.save()
        return redirect('Item')
    return render(request, template_name, {'form':form})     

def excluirItem(request, pk, template_name='confirm_delete.html'):
    item = get_object_or_404(Item, pk=pk)
    if request.method=='POST':
        item.delete()
        return redirect('Item')
    return render(request, template_name, {'object':item})    

#Pedido

class listaPedido(ListView):
    template_name = 'listaPedido.html'
    context_object_name = 'pedido_list'

    def get_queryset(self):
        return Pedido.objects.all()   

def checkCliente(nome):
    clientes = Cliente.objects.all()

    for x in clientes:
        if x.nome == nome:
            return x.pk

    return "DONT_EXIST"

def buscaCliente(request):
    if request.method == 'POST':
        nome = request.POST["nome"]
        id_cliente = checkCliente(nome)
        if id_cliente != "DONT_EXIST":
            url = "add/" + str(id_cliente)
            return redirect(url)
        else:
            return render(request, 'clienteErro.html')
    return render(request, 'clienteBusca.html')

def cadastroPedido(request, pk):
    movimento_forms = Pedido()
    item_movimento_formset = inlineformset_factory(Pedido, ItensPedido, form=ItensPedidoForm, extra=0, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        forms = PedidosForm(request.POST, request.FILES, instance=movimento_forms, prefix='main')
        formset = item_movimento_formset(request.POST, request.FILES, instance=movimento_forms, prefix='item')

        if forms.is_valid() and formset.is_valid():
            forms = forms.save(commit=False)
            forms.idCliente = Cliente.objects.get(pk=pk)
            forms.save()
            formset.save()
            url = "../../pedido/" + str(forms.pk)
            return redirect(url)

    else:
        forms = PedidosForm(instance=movimento_forms, prefix='main')
        formset = item_movimento_formset(instance=movimento_forms, prefix='item')

    context = {
        'forms': forms,
        'formset': formset,
    }

    return render(request, 'cadastroPedido.html', context)

def detalhesPedido(request, pk):
    template_name = 'detalhesPedido.html'
    pedido = Pedido.objects.get(pk=pk)
    itensPedido = ItensPedido.objects.get_queryset().filter(pedidos=pk)
    context = {
        'movimento': pedido,
        'movimentosItens': itensPedido,
    }
    return render(request, template_name, context)                             

def excluirPedido(request, pk, template_name='confirm_delete.html'):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method=='POST':
        pedido.delete()
        return redirect('Pedido')
    return render(request, template_name, {'object':pedido})