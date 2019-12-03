from django.core.management.base import BaseCommand, CommandError
from track.models import Squirrels
import csv

class Command(BaseCommand):
    help = 'Export data in database to a csv file'
    
    def add_arguments(self,parser):
        parser.add_argument('filepath',nargs=1,type=str)

    def handle(self,*args,**options):
        columns = [c.name for c in Squirrels._meta.fields]
        with open(options['filepath'][0],'w+') as f:
            f_writer = csv.writer(f,delimiter=',')
            f_writer.writerow(columns)
            for s in Squirrels.objects.all():
                row = [getattr(s,col) for col in columns]
                f_writer.writerow(row)
        print('Data written to %s'% options['filepath'][0])
