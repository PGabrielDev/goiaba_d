from django.urls import path

from .views import login, dividas, cadastro

urlpatterns = [
    
    path('dividas', dividas, name='dividas'),
    path('cadastro', cadastro, name='cadastro' )
]