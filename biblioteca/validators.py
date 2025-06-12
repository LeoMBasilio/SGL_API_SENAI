from validate_docbr import CPF
import re

def validate_cpf(data):
    cpf = CPF()
    return cpf.validate(data)

def validate_email(data):
    regex = r'^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$'
    return re.match(regex, data) is not None

def validate_celular(data):
    regex = r'^\(\d{2}\)\s\d{4,5}-\d{4}$'
    return re.match(regex, data) is not None

def validate_nome(data):
    regex = r'^[a-zA-z\s]+$'
    return re.match(regex, data) is not None