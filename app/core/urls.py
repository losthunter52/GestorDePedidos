from django.urls import path
from core import views

#Generic
urlpatterns = [
    path('home/', views.index, name='home'),
]


#Cliente
urlpatterns += [
    path('cliente/', views.listaCliente.as_view(), name='Cliente'),
    path('cliente/add', views.cadastroCliente, name='ClienteCadastro'),
    path('cliente/<int:pk>', views.detalhesCliente.as_view(), name='ClienteDetalhes'),
    path('cliente/edit/<int:pk>', views.editarCliente, name='ClienteEditar'),
    path('cliente/delete<int:pk>', views.excluirCliente, name='ClienteExcluir'),
]

#Item
urlpatterns += [
    path('item/', views.listaItem.as_view(), name='Item'),
    path('item/add', views.cadastroItem, name='ItemCadastro'),
    path('item/edit/<int:pk>', views.editarItem, name='ItemEditar'),
    path('item/delete<int:pk>', views.excluirItem, name='ItemExcluir'),
]

#Pedido
urlpatterns += [
    path('pedido/', views.listaPedido.as_view(), name='Pedido'),
    path('pedido/add', views.buscaCliente, name='ProcuraCliente'),
    path('pedido/add/<int:pk>', views.cadastroPedido, name='PedidoCadastro'),
    path('pedido/<int:pk>', views.detalhesPedido, name='PedidoDetalhes'),
    path('pedido/delete<int:pk>', views.excluirPedido, name='PedidoExcluir'),
]

