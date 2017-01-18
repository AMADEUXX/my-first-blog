from __future__ import unicode_literals
from django.shortcuts import render


from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.

from django.db import models
from django.template.defaultfilters import slugify
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Entrada(models.Model):

    Nombre = models.CharField(max_length=30)
    Telefono = PhoneNumberField()
    Titulo = models.CharField(max_length=50)
    Publicacion = models.TextField()
    Slug = models.SlugField(editable=False)
    fecha = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.Titulo

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.Titulo)
        super(Entrada, self).save(*args,**kwargs)
