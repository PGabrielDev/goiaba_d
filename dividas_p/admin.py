from django.contrib import admin
from .models import PessoaF, Divida
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.

@admin.register(PessoaF)
class PessoaFAdmin(ImportExportActionModelAdmin):
    list_display = [
        'nome',
        'idade',
        'cpf',
        'ativa',
        
    ]

@admin.register(Divida)
class DividadeAdmin(ImportExportActionModelAdmin):
    list_display = [
        'nome',
        'local',
        'data',
        'valor',
        'status',
        'pessoas'
    ]
    list_filter = ['pessoas']
