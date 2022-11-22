from django.db import models
from produtoservico.models import ProdutoServico

class Servico(models.Model):
    nome = models.CharField('Nome', max_length=50, help_text='Nome completo')
    preco = models.DecimalField('Preco', max_digits=5, decimal_places=2, help_text='Preço do serviço')
    descricao = models.TextField('Descrição', max_length=300, help_text='Descrição e observações do serviço')
    produto = models.ManyToManyField('produto.Produto', through='produtoservico.ProdutoServico')

    @property
    def produtos(self):
        return ProdutoServico.objects.filter(servico=self)


    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

        def __str__(self):
            return self.nome

# Create your models here.
