from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField('Cidade', max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
    

class Radio(models.Model):
    name = models.CharField(
        "Nome",
        max_length=20
    )
    dial = models.CharField(
        "Canal",
        max_length=5
    )
    cities = models.ForeignKey(
        City,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Rádio"
        verbose_name_plural = "Rádios"