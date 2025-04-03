from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante, Curso, Matricula

class MatriculassTestCase(APITestCase):
    fixtures = ['prototipo_database.json']
    def setUp(self):        
        self.usuario = User.objects.get(username='fernando')
        self.url = reverse('Matriculas-list')
        self.client.force_authenticate(user=self.usuario)
        self.estudante = Estudante.objects.get(pk=1)
        self.curso = Curso.objects.get(pk=1)
        self.matricula = Matricula.objects.get(pk=1)
    
    def test_get_matriculas(self):
        """Teste de requisição GET"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_post_matricula(self):
        """Teste de requisição POST para uma matrícula"""        
        dados = {
            'estudante': self.estudante.pk,
            'curso': self.curso.pk,
            'periodo': 'M'
        }
        response = self.client.post(self.url,data=dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_delete_matricula(self):
        """Teste de requisição DELETE para uma matricula"""
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code,status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def test_put_matricula(self):
        """Teste de requisição PUT para uma matricula"""
        dados = {
            'estudante': self.estudante.pk,
            'curso': self.curso.pk,
            'periodo': 'T'
        }
        response = self.client.put(f'{self.url}1/')
        self.assertEqual(response.status_code,status.HTTP_405_METHOD_NOT_ALLOWED)