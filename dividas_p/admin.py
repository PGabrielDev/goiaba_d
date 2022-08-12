from django.contrib import admin
from .models import PessoaF, Divida
# Register your models here.

@admin.register(PessoaF)
class PessoaFAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
        'idade',
        'cpf',
        'ativa',
        
    ]

@admin.register(Divida)
class DividadeAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
        'local',
        'data',
        'valor',
        'status',
        'pessoas'
    ]
