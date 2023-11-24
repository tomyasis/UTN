from django.shortcuts import render, redirect
from UTN.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import HorarioClase
from .forms import HorarioClaseForm



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


        if Usuario.objects.filter(username=username).exists():
            error_message = "El nombre de usuario ya está en uso."
        
        elif Usuario.objects.filter(email=email).exists():
            error_message = "El correo electrónico ya está en uso."

        elif Usuario.objects.filter(password=password).exists():
            error_message = "La contasenia ya esta en uso"
             
        else:
            user = Usuario.objects.create_user(
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
    if request.method == 'GET':    
        return render(request, 'inscribir.html')
    elif request.method == 'POST':
        pass

def horario(request):

    return render(request, 'horario.html')
    


def historial(request):

    return render(request, 'historial.html')


def notas(request):

    return render(request, 'notas.html')



def horarios_clases(request):
    if request.method == 'POST':
        form = HorarioClaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('horarios_clases')
    else:
        form = HorarioClaseForm()
        
    horarios = HorarioClase.objects.all()
    return render(request, 'horarios.html', {'horarios': horarios, 'form': form})