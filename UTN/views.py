from django.shortcuts import render
from UTN.models import *

# Create your views here.
def inicio(request):
    return render(request, 'index.html')        

def login (request):
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
    else:
        return render(request, 'login.html')        

def singin(request):
    return render(request, 'singin.html')        
