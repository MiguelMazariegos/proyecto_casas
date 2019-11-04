from django.shortcuts import get_object_or_404, render
from .models import Listado
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listados.opciones import opciones_precios, opciones_cuartos, opciones_depart

def index(request):
    listados = Listado.objects.order_by('-fecha').filter(publicado=True)
    paginator = Paginator(listados, 6)
    page = request.GET.get('page')
    paged_listados = paginator.get_page(page)
    context = {
        'listados': paged_listados
    }
    return render(request, 'listados/listados.html', context)

def listing(request, listing_id):
    listado = get_object_or_404(Listado, pk=listing_id)
    context = {
        'listado': listado
    }
    return render(request, 'listados/listado.html', context)

def buscar(request):
    queryset_list = Listado.objects.order_by('-fecha')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(descripcion__icontains=keywords)
    
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(municipio__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(departamento__iexact=state)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(dormitorios__lte=bedrooms)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(precio__lte=price)

    context = {
        'op_pre': opciones_precios,
        'op_cuar': opciones_cuartos,
        'op_dep': opciones_depart,
        'listados': queryset_list
    }
    return render(request, 'listados/busqueda.html', context)
