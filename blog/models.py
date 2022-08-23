from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    entrada = models.TextField()
    fecha_creacion = models.DateTimeField(blank=True, default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, default=timezone.now)
    categoria = models.CharField(max_length=255, default='Noticias')

    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    #permite regresar a pagina principal una vez realizado el post
    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return f'{self.titulo}'

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nombre}'

    def get_absolute_url(self):
        return reverse('blog/entry/<int:pk>')
