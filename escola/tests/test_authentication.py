from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Estudantes-list')
    
    def test_user_auth_right(self):
        """Teste que verifica a autenticação do usuário com as credenciais corretas"""
        usuario = authenticate(username='admin',password='admin')
        self.assertTrue((usuario is not None) and (usuario.is_authenticated))

    def test_user_auth_username(self):
        """Teste que verifica a autenticação do usuário com o username incorreto"""
        usuario = authenticate(username='errado',password='admin')
        self.assertFalse((usuario is not None) and (usuario.is_authenticated))
    
    def test_user_auth_password(self):
        """Teste que verifica a autenticação do usuário com a senha incorreta"""
        usuario = authenticate(username='admin',password='errado')
        self.assertFalse((usuario is not None) and (usuario.is_authenticated))
    
    def test_get_request(self):
        """Teste que verifica uma requisição GET autorizada"""        
        self.client.force_authenticate(self.usuario)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)