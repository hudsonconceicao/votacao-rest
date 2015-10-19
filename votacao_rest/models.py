import sys, os
from django.db import models


class Enquete(models.Model):
    texto_pergunta = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField('Data publicacao')

    def __unicode__(self):
    	return self.texto_pergunta


class Resposta(models.Model):
    enquete = models.ForeignKey(Enquete)
    texto_resposta = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __unicode__(self):
    	return self.texto_resposta
