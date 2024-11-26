from django.shortcuts import render
from .models import Usuarios
# Create your views here.

def inicio_vista(request):
    lista_usuarios=Usuarios.objects.all()
    return render(request,"index.html",{"losusuarios":lista_usuarios})