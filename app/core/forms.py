from django import forms
from .models import *

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"

class ItensPedidoForm(forms.ModelForm):
    class Meta:
        model = ItensPedido
        exclude = ['pedidos']

class PedidosForm(forms.ModelForm):
    class Meta:
        model = Pedido
        exclude = ['idCliente', 'data']