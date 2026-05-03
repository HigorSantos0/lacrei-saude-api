from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import Consulta
from .serializers import ConsultaSerializer

class ConsultaViewSet(viewsets.ModelViewSet):
    serializer_class = ConsultaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Consulta.objects.all()
        profissional_id = self.request.query_params.get('profissional_id')
        if profissional_id:
            queryset = queryset.filter(profissional__id=profissional_id)
        return queryset