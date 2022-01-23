from django.db import models

# Create your models here.

CATEGORIA_CHOICES = (
    ('Alimento Não Perecível', 'Alimento Não Perecível'),
    ('Remédio', 'Remédio'),
    ('Protetor Solar', 'Protetor Solar')
)

class Cliente(models.Model):
    nome = models.CharField(max_length=96, blank = True, null = True)
    cpf = models.CharField(max_length=24, blank = True, null = True)
    email = models.EmailField(blank = True, null = True)

    def __str__(self):
        return self.nome

class Item(models.Model):
    descricao = models.CharField(max_length=100, blank = True, null = True)
    categoria = models.CharField(choices=CATEGORIA_CHOICES, max_length=50, blank = True, null = True)

    def __str__(self):
        return self.descricao

class Pedido(models.Model):
    idCliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, blank = True, null = True)
    data = models.DateTimeField(auto_now_add=True, blank = True, null = True)
    observacao = models.TextField(max_length=96, blank = True, null = True)

    def __str__(self):
        return str("Pedido " + str({self.pk}))

class ItensPedido(models.Model):
    pedidos = models.ForeignKey(Pedido, on_delete=models.CASCADE, blank = True, null = True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank = True, null = True)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.item.descricao