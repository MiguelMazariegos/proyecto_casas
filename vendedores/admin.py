from django.contrib import admin

from .models import Vendedor

class VendedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email', 'telefono')
    list_display_links = ('id', 'nombre')
    search_fields = ('nombre',)

admin.site.register(Vendedor, VendedorAdmin)
