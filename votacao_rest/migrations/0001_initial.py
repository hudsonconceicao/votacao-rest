# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('texto_pergunta', models.CharField(max_length=200)),
                ('data_publicacao', models.DateTimeField(verbose_name=b'Data publicacao')),
            ],
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('texto_resposta', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('pergunta', models.ForeignKey(to='votacao_rest.Pergunta')),
            ],
        ),
    ]
