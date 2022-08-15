from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class PessoaF(models.Model):
    nome = models.TextField('Nome')
    idade = models.IntegerField("IDADE")
    cpf = models.TextField("CPF")
    ativa = models.BooleanField('ativa')

    def __str__(self) -> str:
        return f'Pessoa Fisica: {self.nome}'

class Divida(models.Model):
    nome = models.TextField('Nome')
    local = models.TextField('Local')
    data = models.DateField('Data')
    valor = models.FloatField('Valor')
    status = models.BooleanField('Status')
    pessoas = models.ForeignKey(PessoaF, on_delete=models.PROTECT, related_name='dividas')


class PessoaFUser(models.Model):
    pessoaF = models.ForeignKey(PessoaF, on_delete=models.PROTECT, related_name='pessoa_user')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_pessoa')
    cpf = models.TextField('CPF')
