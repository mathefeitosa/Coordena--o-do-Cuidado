import uuid
from django.db import models
from django.contrib.auth.models import User

STATE_CHOICES = (
  ("AC", "Acre"),
  ("AL", "Alagoas"),
  ("AP", "Amapá"),
  ("AM", "Amazonas"),
  ("BA", "Bahia"),
  ("CE", "Ceará"),
  ("DF", "Distrito Federal"),
  ("ES", "Espírito Santo"),
  ("GO", "Goiás"),
  ("MA", "Maranhão"),
  ("MT", "Mato Grosso"),
  ("MS", "Mato Grosso do Sul"),
  ("MG", "Minas Gerais"),
  ("PA", "Pará"),
  ("PB", "Paraíba"),
  ("PR", "Paraná"),
  ("PE", "Pernambuco"),
  ("PI", "Piauí"),
  ("RJ", "Rio de Janeiro"),
  ("RN", "Rio Grande do Norte"),
  ("RS", "Rio Grande do Sul"),
  ("RO", "Rondônia"),
  ("RR", "Roraima"),
  ("SC", "Santa Catarina"),
  ("SP", "São Paulo"),
  ("SE", "Sergipe"),
  ("TO", "Tocantins"),
)

class Profile(models.Model):
  id = models.UUIDField(
    default=uuid.uuid4,
    primary_key=True,
    unique=True,
    editable=False,
    )
  user = models.OneToOneField(
      User, on_delete=models.CASCADE,
      null=True,
      blank=True,
      verbose_name='Usuário',
  )
  full_name = models.CharField(
      max_length=200,
      verbose_name='Nome completo',
  )
  full_name = models.CharField(
      max_length=200,
      verbose_name='Email',
  )
  cpf = models.CharField(
      max_length=11,
      editable=False,
      verbose_name='CPF',
  )
  cns = models.CharField(
      max_length=15,
      editable=True,
      verbose_name='CNS',
  )
  crm_number = models.CharField(
      max_length=20,
      verbose_name='Número do CRM',
      blank=True,
  )
  crm_state = models.CharField(
      max_length=2,
      choices=STATE_CHOICES,
      verbose_name='Estado do CRM',
      blank=True,
  )
  created = models.DateTimeField(
      auto_now_add=True,
      editable=False,
      verbose_name='Data de criação',
  )
  updated = models.DateTimeField(
    auto_now=True, 
    editable=False,
    verbose_name='Data de edição'
  )