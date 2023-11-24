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

            return redirect('home')  
        else:
            error_message = ''
            return render(request, {'error_message': error_message} )
    

def signup(request):
    
    if request.method == 'GET':
        tiposdocumento = Tipodocumento.objects.all()
        return render(request, 'signup.html', {'tipos_documento': tiposdocumento})    
   
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        tipo_documento_id = request.POST['tipodocumento']
        documento = request.POST['documento']
        fecha_nacimiento = request.POST['fecha_nacimiento']


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
                is_active = 'True',
                tipodocumento = Tipodocumento.objects.get(id = tipo_documento_id), 
                documento = documento,
                fecha_nacimiento = fecha_nacimiento

            )
            return render(request, 'home.html')

        return render(request, 'signup.html', {'error_message': error_message})
        

def home(request):
    return render(request, 'home.html')


def inscribir(request):
    if request.method == 'GET':

        usuario = request.user   
        carreras = usuario.carrera.all()
        
        materias_totales = []
        cursos_totales = []
        print(usuario.carrera.all())
        
        for c in carreras:
            materias = Materia.objects.filter(carrera = c)
            for m in materias:
                materias_totales.append(m)
                cursos = Curso.objects.filter(materia = m)
                for a in cursos:
                    cursos_totales.append(a)
                    
        return render(request, 'inscribir.html', { 'materias_totales' : materias_totales,
                                                    'carreras' : carreras,
                                                    'cursos_totales' : cursos_totales})
   
    elif request.method == 'POST':
        # Obtener los datos del formulario
        carrera_id = request.POST['carrera_id']
        materia_id = request.POST['materia_id']

        carrera = Carrera.objects.get(id=carrera_id)
        materia = Materia.objects.get(id=materia_id)

        # Crear una nueva instancia de Inscripcion
        inscripcion = Inscripcion()
        inscripcion.usuario = request.user
        inscripcion.carrera = carrera
        #inscripcion.curso = materia
        inscripcion.fechaInicio = inscribir.setFechaIncio()
        inscripcion.save()

def horario(request):

    return render(request, 'horario.html')
    


def historial(request):

    return render(request, 'historial.html')


def notas(request):

    return render(request, 'notas.html')
