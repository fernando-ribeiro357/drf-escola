from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante
from escola.serializers import EstudanteSerializer

class EstudantesTestCase(APITestCase):
    fixtures = ['prototipo_database.json']
    def setUp(self):
        self.usuario = User.objects.get(username='fernando')
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.usuario)
        self.estudante01 = Estudante.objects.get(pk=1)
        self.estudante02 = Estudante.objects.get(pk=2)
    
    def test_get_estudantes(self):
        """Teste de requisição GET"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_estudante(self):
        """Teste de requisição GET para um estudante"""
        response = self.client.get(f'{self.url}1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_estudante = Estudante.objects.get(pk=1)    
        dados_estudante_serial = EstudanteSerializer(instance=dados_estudante).data
        self.assertEqual(response.data,dados_estudante_serial)
    
    def test_post_estudante(self):
        """Teste de requisição POST para criar um estudante"""
        dados = {
            'nome': 'Teste',
            'email': 'teste@site.com',
            'cpf': '13218107504',
            'data_nascimento': '2000-03-03',
            'celular': '21 99999-8888'
        }
        response = self.client.post(self.url,data=dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_estudante(self):
        """Teste de requisição DELETE um estudante"""
        response = self.client.delete(f'{self.url}45/')
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

    def test_put_estudante(self):
        """Teste de requisição PUT para atualizar um estudante"""
        dados = {
            'nome': 'Teste put',
            'email': 'testeput@site.com',
            'cpf': '26321261262',
            'data_nascimento': '1999-03-03',
            'celular': '21 95555-8888'
        }
        response = self.client.put(f'{self.url}1/',data=dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)