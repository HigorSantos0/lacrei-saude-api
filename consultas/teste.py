from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from profissionais.models import Profissional
from .models import Consulta

class ConsultaTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser('testuser2', '', 'testpass')
        response = self.client.post('/api/token/', {
            'username': 'testuser2',
            'password': 'testpass'
        }, format='json')
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        self.profissional = Profissional.objects.create(
            nome_social='Dra. Ana Silva',
            profissao='Psicóloga',
            endereco='Rua das Flores, 123',
            contato='11999999999'
        )
        self.consulta = Consulta.objects.create(
            profissional=self.profissional,
            data='2026-06-01T10:00:00Z'
        )

    def test_listar_consultas(self):
        response = self.client.get('/api/consultas/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_criar_consulta(self):
        data = {'profissional': self.profissional.id, 'data': '2026-07-01T14:00:00Z'}
        response = self.client.post('/api/consultas/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_buscar_consulta_por_profissional(self):
        response = self.client.get(f'/api/consultas/?profissional_id={self.profissional.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_criar_consulta_sem_profissional(self):
        data = {'data': '2026-07-01T14:00:00Z'}
        response = self.client.post('/api/consultas/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_requisicao_sem_autenticacao(self):
        self.client.credentials()
        response = self.client.get('/api/consultas/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)