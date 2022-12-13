from django.core.paginator import Paginator
from django.views.generic import ListView

from cliente.models import Cliente
from home.utils import HtmlToPdf
from .models import Cliente


class ClientesView(ListView):
    model = Cliente
    template_name = 'clientes.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(ClientesView,self).get_queryset(*args,**kwargs)
        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        paginator = Paginator(qs,1)
        listagem = paginator = paginator.get_page(self.request.GET.get('page'))
        return listagem
    def get(self,*args,**kwargs):
        if self.request.GET.get('imprimir') == 'pdf':
            hmtl_pdf = HtmlToPdf(arquivo='clientes_pdf',qs=self.get_queryset())
            return hmtl_pdf.response
        else:
            return super (ClientesView,self).get(*args,**kwargs)

