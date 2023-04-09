from tabnanny import verbose
import uuid
from django.db import models

from users.models import Profile
from utils.constants import SEX_CHOICE


# Create your models here.
class Cid10(models.Model):
  id = models.UUIDField(
    default=uuid.uuid4,
    unique=True,
    primary_key=True,
    editable=False,
  )
  letter = models.CharField(
    max_length=1,
    editable=False,
    verbose_name='Letra',
  )
  number = models.CharField(
    max_length=3,
    editable=False,
    verbose_name='Número',
  )
  description = models.CharField(
    max_length=200,
    editable=False,
    verbose_name='Descrição',
  )
  sex = models.CharField(
    max_length=1,
    choices=SEX_CHOICE,
    editable=False,
    blank=True,
    verbose_name='Sexo relacionado',
  )
  cause_death = models.BooleanField(
    max_length=1,
    editable=False,
    blank=True,
    verbose_name='Sexo relacionado',
  )
  
  def __str__(self):
    return f'{self.letter}{self.number}|{self.description}|{self.sex}|{self.cause_death}'

class consultation(models.Model):
  id = models.UUIDField(
    default=uuid.uuid4,
    unique=True,
    primary_key=True,
    editable=False,
  )
  patient = models.ForeignKey(
    Profile,
    on_delete=models.PROTECT,
    null=True,
    blank=True,
    verbose_name='Paciente',
    related_name='consultations_as_patient',
  )
  specialty = models.CharField(
    max_length=200,
    verbose_name='Especialidade'
  )
  #-------------------------------------
  requester = models.ForeignKey(
    Profile,
    on_delete=models.PROTECT,
    null=True,
    blank=True,
    verbose_name='Solicitante',
    related_name='consultations_as_requester',
  )
  requester_cid = models.ForeignKey(
    Cid10,
    on_delete=models.PROTECT,
    null=True,
    blank=False,
    verbose_name='Hipótese/diagnóstico',
    related_name='consultations_as_requester',
  )
  requester_text = models.TextField(
      verbose_name='Solicitação',
  )
  #-------------------------------------
  responder = models.ForeignKey(
    Profile,
    on_delete=models.PROTECT,
    null=True,
    blank=True,
    verbose_name='Respondente',
    related_name='consultations_as_responder',
  )
  responder_cid = models.ForeignKey(
    Cid10,
    on_delete=models.PROTECT,
    null=True,
    blank=False,
    verbose_name='Hipótese/diagnóstico',
    related_name='consultations_as_responder',
  )
  responder_text = models.TextField(
      verbose_name='Resposta',
  )
  #-------------------------------------
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
  is_answered = models.BooleanField(
    default=False,
    verbose_name='Está respondido?'
  )
  
