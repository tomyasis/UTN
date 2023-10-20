from django.db import models

class Tipodocumento(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

class Usuario(models.Model):
    nombre_completo = models.CharField(max_length=255)
    domicilio = models.CharField(max_length=255)
    mail = models.EmailField()
    telefono = models.CharField(max_length=20)
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
    listaHorarios = models.TextField()

class Correlatividad(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    estado_curso = models.ForeignKey('EstadoCurso', on_delete=models.CASCADE)

class EstadoCurso(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

class Historial(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    estado_curso = models.ForeignKey(EstadoCurso, on_delete=models.CASCADE)

class NotaEvaluacion(models.Model):
    nombre = models.CharField(max_length=255)
    tipoEvaluacion = models.CharField(max_length=255)
    valor = models.IntegerField()
    fecha = models.DateField()
    profesor = models.ForeignKey('Profesor', on_delete=models.CASCADE)

class Profesor(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

class Inscripcion(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    condicionFinal = models.ForeignKey(EstadoCurso, on_delete=models.CASCADE)
    fechaInicio = models.DateTimeField()
    fechaFinal = models.DateTimeField()

class Alumno(Usuario):
    listaCarrera = models.ManyToManyField(Carrera)
    listaInscripciones = models.ManyToManyField(Inscripcion)