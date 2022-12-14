from functools import reduce
from xmlrpc.server import list_public_methods
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_d
from django.contrib.auth.decorators import login_required

from dividas_p.models import PessoaF, Divida
# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return dividas(request)
    if request.method == "GET":
        return render(request, 'login.html')
    user_login = request.POST.get('user_login')
    senha = request.POST.get('senha')
    user = authenticate(username=user_login, password=senha)
    if user:
        login_d(request, user)
        return dividas(request)

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    cpf = request.POST.get('cpf')
    pessoaF = PessoaF.objects.filter(cpf=cpf)

    if not pessoaF:
        return redirect('cadastro')

    user_login = request.POST.get('user_login')
    first_name = request.POST.get('first_name')
    senha = request.POST.get('senha')
    user = User.objects.create_user(first_name=first_name, username=user_login, password=senha)
    user = user.save()
    user = authenticate(username=user_login, password=senha)
    if user:
        login_d(request, user)
        return dividas(request)
        
    else:
        return render(request, 'login.html')

    
@login_required
def dividas(request):
    print('entrei em dividas')
    pessoas = PessoaF.objects.all()
    dividas  = [set_to_dict(query_set) for  query_set in pessoas]
    context = {
        'pessoas': dividas
    }

    return render(request, 'dividas.html', context)


def set_to_dict(query_set):
    lista_dividas = {}
    lista_dividas['nome'] = query_set.nome
    lista_dividas['cpf'] = query_set.cpf
    lista_dividas['dividas'] = [divida for divida in query_set.dividas.values()]
    lista_dividas['total'] = sum([valor['valor'] for valor in lista_dividas['dividas']])
    return lista_dividas
