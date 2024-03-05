from django.db import models
from datetime import datetime

from django.forms import model_to_dict
from core.erp.choices import clasificacion,tipoDocumento,tiposDeSangre


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    desc = models.CharField(max_length=150, null=True, blank=True, verbose_name='Descripción')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

class Regional(models.Model):
    name = models.CharField(max_length=150, verbose_name='Regional', unique=True)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regional'
        ordering = ['id']

class Centro(models.Model):
    name = models.CharField(max_length=150, verbose_name='Centro')
    codigo = models.CharField( max_length=50, null=True, blank=True)
    region = models.ForeignKey(Regional, on_delete=models.CASCADE, null=False, blank=False, default=1)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Centro'
        verbose_name_plural = 'Centros'
        ordering = ['id']

class Cargo(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
        ordering = ['id']


class persona(models.Model):
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, null=False, blank=False, default=1)
    names = models.CharField(max_length=30, verbose_name='Nombres')
    surnames = models.CharField(max_length=30, verbose_name='Apellidos')
    tipoDocumento= models.CharField(max_length=50, choices=tipoDocumento, default='C.C', verbose_name='TipoDocumento')
    numeroDocumento = models.CharField(max_length=10, verbose_name='numeroDocumento', null=True, blank=True)   
    tipoSangre= models.CharField(max_length=50, choices=tiposDeSangre, default='0-', verbose_name='TipoDocumento')


    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['id']