from django.db import models
from fornecedores.models import Fornecedor
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(verbose_name='Categoria de Produto', blank='False', null='False', max_length=200)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'categoria'

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(verbose_name='nome do produto', max_length=50, blank=False, null=False)
    descricao = models.CharField(verbose_name='Descrição do Produto', max_length=200)
    preco = models.DecimalField(verbose_name='Preço', decimal_places=2, max_digits=10, blank=False, null=False)
    quantidadeEstoque=models.PositiveIntegerField(verbose_name='Quantidade em Estoque', default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT  )
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    imagem = models.ImageField(null=True, blank=True, default='/images/placeholder.png')
    marca = models.CharField(max_length=200, null=True, blank=True)
    avaliacao = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    criadores = models.DateTimeField(auto_now_add=True)
    
    class Meta:
         verbose_name = 'Produto'
         verbose_name_plural = 'Produtos'
         db_table = 'produto'

    def __str__(self):
        return (f'{self.nome} | {self.marca} | {str(self.preco)}')
       

