import re
from validate_docbr import CPF

def cpf_invalido(num_cpf):
    cpf = CPF()
    cpf_valido = cpf.validate(num_cpf)
    return not cpf_valido
                
def celular_invalido(celular):
    # 21 99999-9999
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo,celular)
    return not resposta

def nome_invalido(nome):
    return not nome.replace(' ','').isalpha()