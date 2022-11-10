from django.shortcuts import render,redirect

from App.models import Usuario
from App.forms import UsuarioForm
# Create your views here.

def mostrarUsuarios(request):
    usuarios = Usuario.objects.all()
    
    return render(request,"usuarios.html", {"usuarios":usuarios})

def registrarUsuario(request):
    if request.method == 'POST':
        formUsuario = UsuarioForm(request.POST)
        if formUsuario.is_valid():
            formUsuario.save()
    else:    
        formUsuario = UsuarioForm()   
    return redirect('inicio')   

    
    