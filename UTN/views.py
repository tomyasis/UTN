from django.shortcuts import render, redirect
from UTN.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse


# Create your views here.
def inicio(request):
    return render(request, 'index.html')        

def login_view (request):
    if request.method == 'GET':    
        return render(request, 'login.html')   
     
    elif request.method == 'POST':
        usuario = request.POST['usuario']
        contrasena = request.POST['contrasena']

        user = authenticate(request, username=usuario, password=contrasena)
        if user is not None:
            
            login(request, user)    
            
            #request.session["user"] = usuario
            #request.session["password"] = contrasena

            return redirect('home')  
        else:
            error_message = ''
            return render(request, {'error_message': error_message} )
    

def signup(request):
    
    if request.method == 'GET':
        tiposdocumento = Tipodocumento.objects.all()
        return render(request, 'signup.html', { 'tipos_documentos' : tiposdocumento})
    
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']


        if User.objects.filter(username=username).exists():
            error_message = "El nombre de usuario ya está en uso."
        
        elif User.objects.filter(email=email).exists():
            error_message = "El correo electrónico ya está en uso."

        elif User.objects.filter(password=password).exists():
            error_message = "La contasenia ya esta en uso"
             
        else:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name,
                is_active = 'True'
            )
            return render(request, 'home.html')

        return render(request, 'signup.html', {'error_message': error_message})
        

def home(request):
    return render(request, 'home.html')



def inscribir(request):

    return render(request, 'inscribir.html')


def horario(request):

    return render(request, 'horario.html')


def historial(request):

    return render(request, 'historial.html')


def notas(request):
    
    return render(request, 'notas.html')
