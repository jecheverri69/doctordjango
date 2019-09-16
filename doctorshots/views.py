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
        return HttpResponseRedirect(reverse ('doctorshots:formlogin',args=(e,)))

def logout(request):
    del request.session['logueado']
    return render(request, 'doctorshots/index.html')

def formularioLogin(request ,mensaje):
    contexto = {'mensaje': mensaje}
    return render(request, 'doctorshots/login.html',contexto)

def formularioEmpleado(request ,mensaje):
    q= Usuarios.objects.all()
    contexto = {'datos': q, 'mensaje': mensaje }
    return render(request,'doctorshots/form-crear-empleado.html',contexto)

def guardarEmpleado(request):
    try:
        empleado = Usuarios(
            cedula = request.POST['cedula'],
            nombres= request.POST['nombres'],
            usuario = request.POST['usuario'],
            clave = request.POST['clave'],
            Rol = request.POST['Rol']
        )
        empleado.save()
        
        q = Usuarios.objects.all()
        contexto = {'datos': q}
        
        return HttpResponseRedirect(reverse ('doctorshots:formempleado' ,args=('GuardadoCorrectamente',))) 
    except Exception as e:
        return HttpResponseRedirect(reverse('doctorshots:formempleado',args=(e,)))

def eliminarEmpleado(request,id):
    try:
        q = Usuarios.objects.get(pk=id)
        print(q)
        q.delete()
        return HttpResponseRedirect(reverse('doctorshots:formempleado', args=('Eliminado Correctamente',)))
    except Exception as e:
        return HttpResponseRedirect(reverse('doctorshots:formempleado', args=(e,)))
    
def editarEmpleado(request, id):
    try:
        q= Usuarios.objects.get(pk=id)
        contexto = {'empleado':q}
        return render(request,'doctorshots/form-editar-empleado.html',contexto)
    except Exception as e:
        return HttpResponseRedirect(reverse('doctorshots:formempleado', args=(e,)))

def actualizarEmpleado(request):
    try:
        id= request.POST['id']
        q = Usuarios.objects.get(pk=id)
        q.cedula= request.POST['cedula']
        q.nombres= request.POST['nombres']
        q.usuario= request.POST['usuario']
        q.clave= request.POST['clave']
        q.Rol= request.POST['Rol']
        q.save()
        return HttpResponseRedirect(reverse('doctorshots:formempleado' ,args=('actualizado correctamente',)))
    except Exception as e:
        return HttpResponse(e)

def carta(request):
    return render(request, 'doctorshots/carta.html')  

def ventas(request):
    return render(request, 'doctorshots/ventas.html')      

    # inventario

    
def formularioinventario(request ,mensaje):
    q= Usuarios.objects.all()
    contexto = {'datos': q, 'mensaje': mensaje }
    return render(request,'doctorshots/form-crear-producto.html',contexto)

def guardarEmpleado(request):
    try:
        empleado = Usuarios(
            cedula = request.POST['cedula'],
            nombres= request.POST['nombres'],
            usuario = request.POST['usuario'],
            clave = request.POST['clave'],
            Rol = request.POST['Rol']
        )
        empleado.save()
        
        q = Usuarios.objects.all()
        contexto = {'datos': q}
        
        return HttpResponseRedirect(reverse ('doctorshots:formempleado' ,args=('GuardadoCorrectamente',))) 
    except Exception as e:
        return HttpResponseRedirect(reverse('doctorshots:formempleado',args=(e,)))

def eliminarEmpleado(request,id):
    try:
        q = Usuarios.objects.get(pk=id)
        print(q)
        q.delete()
        return HttpResponseRedirect(reverse('doctorshots:formempleado', args=('Eliminado Correctamente',)))
    except Exception as e:
        return HttpResponseRedirect(reverse('doctorshots:formempleado', args=(e,)))
    
def editarEmpleado(request, id):
    try:
        q= Usuarios.objects.get(pk=id)
        contexto = {'empleado':q}
        return render(request,'doctorshots/form-editar-empleado.html',contexto)
    except Exception as e:
        return HttpResponseRedirect(reverse('doctorshots:formempleado', args=(e,)))

def actualizarEmpleado(request):
    try:
        id= request.POST['id']
        q = Usuarios.objects.get(pk=id)
        q.cedula= request.POST['cedula']
        q.nombres= request.POST['nombres']
        q.usuario= request.POST['usuario']
        q.clave= request.POST['clave']
        q.Rol= request.POST['Rol']
        q.save()
        return HttpResponseRedirect(reverse('doctorshots:formempleado' ,args=('actualizado correctamente',)))
    except Exception as e:
        return HttpResponse(e)
