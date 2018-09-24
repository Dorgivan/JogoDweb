from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Pergunta(models.Model):

    texto = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
    	return self.texto

class Relaciona(models.Model):

    ir_para = models.ForeignKey(Pergunta, on_delete=models.CASCADE,
        help_text='Esse campo serve para direcionar para qual pergunta deve ter as opções'
    )
    relaciona = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name='relacionas',
        help_text='Esse campo serve para mostrar em qual pergunta o botão deve aparecer para\
        se relacionar com a pergunta de cima'
    )

    def __str__(self):
    	return str(self.ir_para)
