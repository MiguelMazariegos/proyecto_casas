from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'nombre', 'listado', 'email', 'fecha')
  list_display_links = ('id', 'nombre')
  search_fields = ('nombre', 'email', 'listado')
  list_per_page = 25

admin.site.register(Contact, ContactAdmin)
