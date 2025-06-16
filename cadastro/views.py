from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
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

def excluir_usuario(request, id):
    usuario_obj = get_object_or_404(usuario, id=id)
    usuario_obj.delete()
    return redirect('entrou') 

def editar_usuario(request, id):
    usuario_obj = get_object_or_404(usuario, id=id)
    
    if request.method == 'POST':
        form = usuarioForm(request.POST, instance=usuario_obj)
        if form.is_valid():
            form.save()
            return redirect('entrou')
    else:
        form = usuarioForm(instance=usuario_obj)

    return render(request, 'editar.html', {'form': form, 'usuario': usuario_obj})

