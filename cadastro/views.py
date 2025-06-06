from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.hashers import make_password
from .forms import usuarioForm
from .models import usuario
# Create your views here.
def home(request):
    return render(request, 'index.html')
def entrou(request):
    usuarios = usuario.objects.all()
    return render(request, 'entrou.html', {'usuarios': usuarios})


def cadastra_usuario(request):
    if request.method == 'POST':
        form = usuarioForm(request.POST)
        if form.is_valid():
            form.save()
            #print("Formulário válido, redirecionando...")
            return redirect('entrou')
    else:
        form = usuarioForm()
    return render(request, 'index.html', {'form': form})

'''def cadastra_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')
        setor = request.POST.get('setor')
        usuario.objects.create(
            nome=nome,
            email=email,
            cpf=cpf,
            senha=senha,
            cargo=setor
        )
        return redirect('entrou')
    return render(request, 'index.html')

def entrou(request):
    return render(request, 'entrou.html')'''
