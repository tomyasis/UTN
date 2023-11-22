from django.db import models
from django.contrib.auth.models import AbstractUser


class Tipodocumento(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

class Usuario(AbstractUser):
    tipodocumento = models.ForeignKey(Tipodocumento, on_delete=models.CASCADE)
    documento = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()

class Turno(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

class Carrera(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

class Materia(models.Model):
    nombre = models.CharField(max_length=255)
    siglas = models.CharField(max_length=10)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    materia_correlativa = models.OneToOneField('self', null=True, blank=True, on_delete=models.SET_NULL)
    
class Curso(models.Model):
    nombreCurso = models.CharField(max_length=255)
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE)
    nivel = models.IntegerField()
    listaHorarios = models.CharField(max_length=255)

class EstadoCurso(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()


class Correlatividad(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    estado_curso = models.ForeignKey(EstadoCurso, on_delete=models.CASCADE)


class Profesor(models.Model):
    nombre = models.CharField(max_length=255, default='')
    apellido = models.CharField(max_length=255, default='')
    correo = models.EmailField(default='')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

class CondicionFinal(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

class Inscripcion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default='')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    condicionFinal = models.ForeignKey(CondicionFinal, on_delete=models.CASCADE)
    fechaInicio = models.DateTimeField()
    fechaFinal = models.DateTimeField()

class NotaEvaluacion(models.Model):
    nombre = models.CharField(max_length=255)
    tipoEvaluacion = models.CharField(max_length=255)
    valor = models.IntegerField()
    fecha = models.DateField()
    Inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE, default='')
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

class Historial(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    Inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE, default='')
    estado_curso = models.ForeignKey(EstadoCurso, on_delete=models.CASCADE)