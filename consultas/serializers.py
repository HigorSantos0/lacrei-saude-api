from rest_framework import serializers
from .models import Consulta

class ConsultaSerializer(serializers.ModelSerializer):
    profissional_nome = serializers.CharField(
        source='profissional.nome_social',
        read_only=True
    )

    class Meta:
        model = Consulta
        fields = '__all__'
        read_only_fields = ['criado_em', 'atualizado_em']