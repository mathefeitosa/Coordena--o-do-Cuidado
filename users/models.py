import uuid
from django.db import models
from django.contrib.auth.models import User

from utils.constants import STATE_CHOICES, USER_TYPES

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
  user_type = models.CharField(
      max_length=3,
      choices=USER_TYPES,
      verbose_name='Tipo de usuário',
      blank=False,
      null=False,
      editable=True,
      default='PAT'
  )
  full_name = models.CharField(
      max_length=200,
      verbose_name='Nome completo',
  )
  email = models.CharField(
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
  def __str__(self) -> str:
    text = f'{self.full_name} - CRM/{self.crm_state} {self.crm_number}'
    return text