from django.test import TestCase
from escola.models import Estudante, Curso, Matricula

class ModelEstudanteTestCase(TestCase):
    # def test_falha(self):
    #     self.fail('Teste falhou.')
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'Teste de Modelo',
            email = 'testedemodelo@site.net',
            cpf = '68195899056',
            data_nascimento = '2000-03-03',
            celular = '21 99999-9999'
        )
    
    def test_attr_estudante(self):
        """Teste que verifica os atributos do modelo de Estudante"""
        self.assertEqual(self.estudante.nome, 'Teste de Modelo')
        self.assertEqual(self.estudante.email, 'testedemodelo@site.net')
        self.assertEqual(self.estudante.cpf, '68195899056')
        self.assertEqual(self.estudante.data_nascimento, '2000-03-03')
        self.assertEqual(self.estudante.celular, '21 99999-9999')

class ModelCursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(
            codigo = 'CTEST',
            descricao = 'Descrição do Teste de Curso',
            nivel = 'B'
        )
    
    def test_attr_curso(self):
        """Teste que verifica os atributos do modelo de Curso"""
        self.assertEqual(self.curso.codigo, 'CTEST')
        self.assertEqual(self.curso.descricao, 'Descrição do Teste de Curso')
        self.assertEqual(self.curso.nivel, 'B')

class ModelMatriculaTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'Teste de Modelo',
            email = 'testedemodelo@site.net',
            cpf = '68195899056',
            data_nascimento = '2000-03-03',
            celular = '21 99999-9999'
        )
        self.curso = Curso.objects.create(
            codigo = 'CTEST',
            descricao = 'Descrição do Teste de Curso',
            nivel = 'B'
        )

        self.matricula = Matricula.objects.create(
            estudante = self.estudante,
            curso = self.curso,
            periodo = 'T'
        )
    
    def test_attr_matricula(self):
        """Teste que verifica os atributos do modelo de Matrícula"""
        self.assertEqual(self.matricula.estudante.nome, 'Teste de Modelo')
        self.assertEqual(self.matricula.curso.codigo, 'CTEST')
        self.assertEqual(self.matricula.periodo, 'T')
