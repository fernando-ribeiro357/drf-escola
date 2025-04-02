from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Curso
from escola.serializers import CursoSerializer

class CursosTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Cursos-list')
        self.client.force_authenticate(user=self.usuario)        
        self.curso01 = Curso.objects.create(
            codigo = 'CTEST1',
            descricao = 'Descrição do Curso 01',
            nivel = 'B'
        )
        self.curso02 = Curso.objects.create(
            codigo = 'CTEST2',
            descricao = 'Descrição do Curso 02',
            nivel = 'I'
        )
    
    def test_get_cursos(self):
        """Teste de requisição GET"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_curso(self):
        """Teste de requisição GET para um curso"""
        response = self.client.get(self.url+'1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_curso = Curso.objects.get(pk=1)
        dados_curso_serial = CursoSerializer(instance=dados_curso).data
        self.assertEqual(response.data,dados_curso_serial)
    
    def test_post_curso(self):
        """Teste de requisição POST para um curso"""
        dados = {
            'codigo': 'CT01',
            'descricao': 'Curso para teste',
            'nivel': 'B'
        }
        response = self.client.post(self.url,data=dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_delete_curso(self):
        """Teste de requisição DELETE um curso"""
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

    def test_put_curso(self):
        """Teste de requisição PUT para atualizar um curso"""
        dados = {
            'codigo': 'CTST1',
            'descricao': 'Descrição do Curso 01 atualizado',
            'nivel': 'I'
        }
        response = self.client.put(f'{self.url}1/',data=dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)