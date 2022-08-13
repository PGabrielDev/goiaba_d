from django.urls import path

from .views import login, dividas, cadastro

urlpatterns = [
    path('login', login, name='login'),
    path('dividas', dividas, name='dividas'),
    path('cadastro', cadastro, name='cadastro' )
]