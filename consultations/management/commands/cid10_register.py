import csv
import os
from django.core.management.base import BaseCommand
from django.conf import settings

from consultations.models import Cid10

class Command(BaseCommand):
  help = 'Insere os códigos CID-10 no banco de dados.'
  
  def handle(self, *args, **options):
    file_path = os.path.join(
      settings.BASE_DIR,
      'consultations/management/commands/cid10_subcategories.csv'
      )
    with open(file_path, 'r', encoding='utf-8') as file:
      reader = csv.reader(file)
      next(reader)
      for raw_row in reader:
        row = raw_row[0].split(';')
        
        letter = row[0][0:1]
        number = row[0][1:4]
        description = row[4]
        sex = ''
        if row[2] == 'M':
          sex = 'M'
        if row[2] == 'F':
          sex = 'W'
        cause_death = False
        if row[3] == 'N':
          cause_death = False
        else:
          cause_death = True
        cid = Cid10(
          number=number,
          letter=letter,
          description=description,
          sex=sex,
          cause_death=cause_death
          )
        cid.save()
        print(cid)