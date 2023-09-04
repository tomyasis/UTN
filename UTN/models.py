from django.db import models

# Clase para representar Categorías
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Clase para representar Autores
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    biografia = models.TextField()

    def __str__(self):
        return self.nombre

# Clase para representar Posts del Blog
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)  # Relación con Autor
    categorias = models.ManyToManyField(Categoria)              # Relación con Categoría

    def __str__(self):
        return self.titulo

# Clase para representar Comentarios en los Posts
class Comentario(models.Model):
    autor = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # Relación con Post

    def __str__(self):
        return self.contenido
