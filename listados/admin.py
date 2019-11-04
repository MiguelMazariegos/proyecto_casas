from django.contrib import admin

from .models import Listado

class ListadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'publicado', 'precio', 'fecha', 'vendedor')
    list_display_links = ('id', 'titulo')
    list_filter = ('vendedor',)
    search_fields = ('titulo', 'descripcion', 'direccion', 'departamento', 'municipio', 'precio')
    list_per_page = 25
admin.site.register(Listado, ListadoAdmin)
