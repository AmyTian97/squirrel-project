from django.core.management.base import BaseCommand, CommandError
from track.models import Squirrels
import csv
from datetime import datetime

class Command(BaseCommand):
    help = 'Import 2018 census data file in csv format to database'

    def add_arguments(self,parser):
        parser.add_argument('filepath',nargs=1,type=str)

    def handle(self,*args,**options):
        str_to_bool = lambda x: True if x=='true' else False
        with open(options['filepath'][0]) as f:
            reader = csv.DictReader(f)
            for row in reader:
                s = Squirrels(
                        longitude = float(row['X']),
                        latitude = float(row['Y']),
                        unique_squirrel_id = row['Unique Squirrel ID'],
                        shift = row['Shift'],
                        date = datetime.strptime(row['Date'],'%m%d%Y'),
                        age = row['Age'].upper()[:2],
                        primary_fur_color = row['Primary Fur Color'].upper()[:2],
                        location = ''.join([w[0] for w in row['Location'].split()]),
                        specific_location = row['Specific Location'],
                        running = str_to_bool(row['Running']),
                        chasing = str_to_bool(row['Chasing']),
                        climbing = str_to_bool(row['Climbing']),
                        eating = str_to_bool(row['Eating']),
                        foraging = str_to_bool(row['Foraging']),
                        other_activities = row['Other Activities'],
                        kuks = str_to_bool(row['Kuks']),
                        quaas = str_to_bool(row['Quaas']),
                        moans = str_to_bool(row['Moans']),
                        tail_flags = str_to_bool(row['Tail flags']),
                        tail_twitches = str_to_bool(row['Tail twitches']),
                        approaches = str_to_bool(row['Approaches']),
                        indifferent = str_to_bool(row['Indifferent']),
                        runs_from = str_to_bool(row['Runs from']),
                        )
                s.save()
