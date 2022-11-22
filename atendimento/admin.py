from django.contrib import admin
from .models import Atendimento


@admin.register(Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    list_display = ['horario','cliente','funcionario','servico','situacao']
    search_fields = ('cliente', 'funcionario')
    list_filter = ('horario', 'servico','situacao',)
# Register your models here.
