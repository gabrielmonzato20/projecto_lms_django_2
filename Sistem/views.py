from django.shortcuts import render,redirect
from Cliente.views import objeto
import json
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, get_user_model,login as auth
from django.contrib.auth.models import User,Permission
# def index(request):
#     return render('templates/index.html')
from django.http import HttpResponse,JsonResponse
def reset(request):
    return render(request,'registration/reset.html',)
def login(request):
    erro = False
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        nome = request.POST['username']
        senha = request.POST['password']
        user = authenticate(username=nome, password=senha)
        if user is not None:
            if user.is_active:
                auth(request, user)
                request.session['admin_permissao'] = True if user.has_perm('change_user') else False
                return redirect('index')
        else:
                erro = True
                return render(request, 'registration/login.html', {'form': formulario,'erro':erro})
    else:
        erro = False
        formulario = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': formulario,'erro':erro})
def deleta_tudo(request):
    usuario = User.objects.all().delete()
    return HttpResponse("delete")
def cadastra_funcionario(request):

    nome = request.GET["nome_func"]
    senha = request.GET['password']
    admin = 1 if 'admin' in request.GET else 0
    print(admin)
    print(len(User.objects.filter(username=nome).values())== 0)
    if(len(User.objects.filter(username=nome).values())== 0):
        print('01924849')

        if admin == 1:
            usuario = User.objects.create_superuser(username=nome, email='', password=senha)
            permissao = Permission.objects.get(codename='change_user')
            usuario.user_permissions.add(permissao)
        else:
            usuario = User.objects.create_user(username=nome, email='', password=senha)

        usuario.save()
        return HttpResponse(User.objects.all())
    response = HttpResponse({"error": "there was an error"})
    response.status_code = 403 # To announce that the user isn't allowed to publish
    return response
def index(request,admin=False):
    clientes = objeto(request)
    return render(request,"front\index.html",{'clientes':clientes,'admin':request.session['admin_permissao']})
