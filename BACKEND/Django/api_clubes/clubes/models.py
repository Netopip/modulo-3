from django.db import models
import datetime

# Create your models here.

class Clube(models.Model):
    #vem id por padrão
    nome = models.CharField()
    uf = models.CharField(max_length=2,null=True)
    data_fundacao = models.DateField(default=datetime.datetime.today)
    tem_estadio = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = 'Clubes'
        
    def __str__(self):
        return self.nome
    
class Jogador(models.Model):
    nome = models.CharField()
    numero = models.IntegerField()
    
    class Meta:
        verbose_name_plural = 'Jogadores'
        
    '''def __str__(self):#lista display substitui
        return f'{self.nome} {self.numero}'''