from django.db import models

class Profissional(models.Model):
    nome_social = models.CharField(max_length=255)
    profissao = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    contato = models.CharField(max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome_social} - {self.profissao}"

    class Meta:
        ordering = ['nome_social']