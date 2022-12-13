from django.shortcuts import render
from django.views.generic import ListView
from .models import Servico
from django.db.models import Q

class ServicosView (ListView):
    model = Servicotemplate_name = 'servicos.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(ServicosView,self).get_queryset(*args,**kwargs)
        if buscar:
            qs = qs.filter(Q(nome__icontains=buscar)|Q(descricao__icontains=buscar))
        return qs

# Create your views here.
