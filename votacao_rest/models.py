import sys, os
from django.db import models

# Create your models here.
class Pergunta(models.Model):
    texto_pergunta = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField('Data publicacao')

    def __unicode__(self):
    	return self.texto_pergunta


class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta)
    texto_resposta = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __unicode__(self):
    	return self.texto_resposta
