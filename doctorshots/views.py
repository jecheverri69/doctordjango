from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.forms.models import model_to_dict

from doctorshots.models import Usuarios


def index(request):
    return render(request, 'doctorshots/index.html')

def login(request):
    try:
        user = request.POST['usuario']
        passw = request.POST['clave']
        #verificar si hay un registro con ese usuario y clave
        q = Usuarios.objects.get(usuario = user, clave = passw)       
        #en caso afirmativo, creo la variable de sesión
        request.session['logueado'] = [q.cedula, q.usuario, q.clave, q.Rol]
        return render(request,'doctorshots/index.html')
    except Exception as e:
        return HttpResponse(e)

def logout(request):
    del request.session['logueado']
    return render(request, 'doctorshots/index.html')


def formularioLogin(request):
    return render(request, 'doctorshots/login.html')

def formularioEmpleado(request):
    q= Usuarios.objects.all()
    contexto = {'datos': q}
    return render(request,'doctorshots/form-crear-empleado.html',contexto)

def guardarEmpleado(request):
    try:
        empleado = Usuarios(
            cedula = request.POST['cedula'],
            usuario = request.POST['usuario'],
            clave = request.POST['clave'],
            Rol = request.POST['Rol']
        )
        empleado.save()
        
        q = Usuarios.objects.all()
        contexto = {'datos': q}
        
        return HttpResponseRedirect(reverse ('doctorshots:formempleado',args=()))
    except Exception as e:
        return HttpResponse('Error entro aca')


def eliminarEmpleado(request,id):
    try:
        q = Usuarios.objects.get(pk=id)
        print(q)
        q.delete()
        return HttpResponseRedirect(reverse('doctorshots:formempleado', args=()))
    except Exception as e:
        return HttpResponse(e)