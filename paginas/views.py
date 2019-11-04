from django.shortcuts import render
from django.http import HttpResponse
from listados.opciones import opciones_precios, opciones_cuartos, opciones_depart

from listados.models import Listado
from vendedores.models import Vendedor

# Create your views here.
def index(request):
    listados = Listado.objects.order_by('-fecha').filter(publicado=True)[:4]
    context = {
        'listados': listados,
        'op_pre': opciones_precios,
        'op_cuar': opciones_cuartos,
        'op_dep': opciones_depart
    }
    return render(request, 'paginas/index.html', context)

def about(request):
    vendedores = Vendedor.objects.order_by('-fecha_cont')
    
    mvp_vendedores = Vendedor.objects.all().filter(is_mvp=True)

    context = {
        'vendedores': vendedores,
        'mvp': mvp_vendedores
    }
    return render(request, 'paginas/about.html', context)