from django.db import models

# Create your models here.
class Regional(models.Model):
    nombreRegional = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreRegional
    
    class Meta:
        verbose_name = 'Regional'
        verbose_name_plural = 'Regionales'
        ordering = ['id']



class Centro(models.Model):
    nombreDelCentro = models.CharField(max_length=100)
    Regionla = models.ForeignKey(Regional, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombredelcentro
    
    class Meta:
        verbose_name = 'Centro'
        verbose_name_plural = 'Centros'
        ordering = ['id']


class PerfilUsuarioSena(models.Model):
    nombrePerfilSena = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreperfil
    
    class Meta:
        verbose_name = 'PerfilUsuarioSena'
        verbose_name_plural = 'PerfilUsuarioSena'
        ordering = ['id']
