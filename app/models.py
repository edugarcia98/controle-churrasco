from django.db import models

# Create your models here.
class Pessoa(models.Model):
    TP_PESSOA = (
        (1, 'Funcionário'),
        (2, 'Convidado')
    )

    nome = models.CharField(max_length=100, verbose_name="Nome")
    bebe = models.BooleanField(verbose_name="Bebe?")
    tipo = models.IntegerField(choices=TP_PESSOA, verbose_name="Tipo de pessoa")
    convidado = models.OneToOneField('app.Pessoa', null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Convidado")
    valor_pagar = models.FloatField(verbose_name="Valor a pagar")

    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ('nome',)
        verbose_name = ("Pessoa")
        verbose_name_plural = ("Pessoas")

class Compra(models.Model):
    TP_COMPRA = (
        (1, 'Comida'),
        (2, 'Bebida')
    )

    desc = models.CharField(max_length=150, verbose_name="Descrição")
    tipo = models.IntegerField(choices=TP_COMPRA, verbose_name="Tipo de compra")
    preco_unitario = models.FloatField(verbose_name="Preço unitário")
    qtd = models.IntegerField(verbose_name="Quantidade")
    preco_total = models.FloatField(verbose_name="Preço total")

    def __str__(self):
        return self.desc
    
    class Meta:
        ordering = ('desc',)
        verbose_name = ("Compra")
        verbose_name_plural = ("Compras")