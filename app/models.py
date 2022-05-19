"""
Definition of models.
"""

from django.db import models
from cpf_field.models import CPFField
from django.db.models import (
    AutoField,
    Model,
    UUIDField,
    SlugField,
    CharField,
    DateField,
    PositiveIntegerField,
    ImageField,
    FileField,
    DateTimeField,
    IntegerField,
    FloatField,
    TextField,
    EmailField,
    ForeignKey,
    CASCADE,
    ManyToManyField
)
# Create your models here.

CONTRATACAO_CHOICES = (
    ('EST', 'Estagio'),
    ('CLT', 'Empregado registrado pela CLT'),
    ('PJ', 'Pessoa Jurídica'),
)
MODALIDADE = (
    ('PRESENCIAL', 'presencial'),
    ('REMOTO', 'home-office')
)
class Tecnologia(Model):
    nome = CharField(max_length=255, null=False, blank=False)


class Vacancies(Model):
    __tablename__ = 'vagas'
    vaga_id = AutoField(primary_key=True)
    titulo = CharField(max_length=50)
    descricao = TextField()
    salario = FloatField()
    empresa = CharField(max_length=50)
    modalidade = CharField(max_length=20, choices = MODALIDADE)
    local = CharField(max_length=20, null=False, blank=False)
    tecnologias = ManyToManyField(Tecnologia)
    tipo_contratacao = CharField(max_length=3, null=False, blank=False, choices = CONTRATACAO_CHOICES)
    created_at = DateField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

class UserClient(Model):
    __tablename__ = 'usuario'
    user_id = AutoField(primary_key=True)
    full_name = CharField(max_length=200)
    birthday = CharField(max_length=8)
    scholarity = CharField(max_length=50)
    cpf = CPFField('cpf')
    telephone_number = CharField(max_length=15)
    city = CharField(max_length=100)
    district = CharField(max_length=100) # bairro
    street = CharField(max_length=100)
    numero_usuario = CharField(max_length=10)
    email = EmailField()
    password = CharField(max_length=10)
    document = FileField(upload_to='pdfs', null=True)
    created_at = DateField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    

class Candidato(Model):
    empresa = ForeignKey(Vacancies, on_delete=CASCADE, verbose_name="Empresa")  
    usuario = ForeignKey(UserClient, on_delete=CASCADE, verbose_name="Usuario") 

class Recrutador(Model):
    pass