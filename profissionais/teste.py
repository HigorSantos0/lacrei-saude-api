from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Profissional

class ProfissionalTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser('testuser', '', 'testpass')
        response = self.client.post('/api/token/', {
            'username': 'testuser',
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

    def test_listar_profissionais(self):
        response = self.client.get('/api/profissionais/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_criar_profissional(self):
        data = {
            'nome_social': 'Dr. Carlos',
            'profissao': 'Clínico Geral',
            'endereco': 'Av. Central, 456',
            'contato': '11988888888'
        }
        response = self.client.post('/api/profissionais/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_buscar_profissional_por_id(self):
        response = self.client.get(f'/api/profissionais/{self.profissional.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome_social'], 'Dra. Ana Silva')

    def test_atualizar_profissional(self):
        data = {'nome_social': 'Dra. Ana Santos', 'profissao': 'Psicóloga',
                'endereco': 'Rua das Flores, 123', 'contato': '11999999999'}
        response = self.client.put(f'/api/profissionais/{self.profissional.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deletar_profissional(self):
        response = self.client.delete(f'/api/profissionais/{self.profissional.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_sem_autenticacao(self):
        self.client.credentials()
        response = self.client.get('/api/profissionais/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_criar_profissional_dados_invalidos(self):
        response = self.client.post('/api/profissionais/', {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)