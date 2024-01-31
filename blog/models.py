from django.db import models
from ckeditor.fields import RichTextField

from miembros.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='title', blank=True)
    content = RichTextField(verbose_name='Contenido')
    image = models.ImageField(upload_to='posts', verbose_name='Imagen', blank=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')

    def __str__(self):
        return self.title