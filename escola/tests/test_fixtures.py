from django.test import TestCase
from escola.models import Estudante, Curso

class FixturesTestCase(TestCase):
    fixtures = ['prototipo_database.json']

    def test_fixtures(self):
        """Teste de carregamento da fixture"""
        estudante = Estudante.objects.get(cpf='29698838562')
        curso = Curso.objects.get(codigo='CPOO1')
        self.assertEqual(estudante.email,'dr.joaoguilhermemendes@uol.com.br')
        self.assertEqual(curso.descricao,'Curso de Python Orientação à Objetos 01')