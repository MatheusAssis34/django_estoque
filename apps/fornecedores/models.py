from django.db import models


# Create your models here.
class Fornecedor(models.Model):
    nome = models.CharField(verbose_name='Nome', blank='False', null='False', max_length=200)
    contato = models.CharField(verbose_name='Contato', blank='False', null='False', max_length=200)
    cnpj = models.CharField(verbose_name='CNPJ', blank='False', null='False', max_length=200, unique=True)
    
    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        db_table = 'fornecedor'
        ordering=['-id']

    def __str__(self):
        return (f'{self.nome} - {self.cnpj}')
    
    
    