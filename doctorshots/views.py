from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.forms.models import model_to_dict

from doctorshots.models import Usuarios


def index(request):
    return render(request, 'doctorshots/login.html')

def login(request):
    try:
        user = request.POST['txtuser']
        passw = request.POST['txtpass']
        #verificar si hay un registro con ese usuario y clave
        q = Usuarios.objects.get(usuario = user, contraseña = passw)
       
        #en caso afirmativo, creo la variable de sesión
        request.session['logueado'] = [q.cedula, q.usuario, q.contraseña, q.Rol]
        return HttpResponse("logueado")
    except Exception as e:
        return HttpResponse(e)
        