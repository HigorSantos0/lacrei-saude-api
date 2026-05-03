from django.db import models
from profissionais.models import Profissional

class Consulta(models.Model):
    profissional = models.ForeignKey(
        Profissional,
        on_delete=models.CASCADE,
        related_name='consultas'
    )
    data = models.DateTimeField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Consulta com {self.profissional.nome_social} em {self.data}"

    class Meta:
        ordering = ['data']