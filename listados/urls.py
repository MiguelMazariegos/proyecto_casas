from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listados'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.buscar, name='buscar'),
]
