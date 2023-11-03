from django.shortcuts import render, redirect
from UTN.models import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


# Create your views here.
def inicio(request):
    return render(request, 'index.html')        

def login (request):    
    if request.method == 'POST':
        usuario = request.POST['usuario']
        contrasena = request.POST['contrasena']

        user = authenticate(request, username=usuario, password=contrasena)
        if user is not None:
            login(request, user)
            
            #request.session["user"] = usuario
            #request.session["password"] = contrasena
            return redirect('/')  
        else:
            return render(request, HttpResponse('logiate bien boludito'))
    else:    
        return render(request, 'login.html')

def signin(request):
    if request.method == 'POST':    
        nombre_completo = request.POST['nombre_completo']
        domicilio = request.POST['domicilio']
        mail = request.POST['mail']
        telefono = request.POST['telefono']
        tipodocumento_id = request.POST['tipodocumento']
        documento = request.POST['documento']
        fecha_nacimiento = request.POST['fecha_nacimiento']

        Usuario.objects.create(
            nombre_completo=nombre_completo,
            domicilio=domicilio,
            mail=mail,
            telefono=telefono,
            tipodocumento_id=tipodocumento_id,
            documento=documento,
            fecha_nacimiento=fecha_nacimiento
        )
        return redirect('/')
    else:
        tiposdocumento = Tipodocumento.objects.all()
        return render(request, 'signin.html', { 'tipos_documentos' : tiposdocumento})