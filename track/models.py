from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Squirrels(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
    unique_squirrel_id = models.CharField(
            max_length=100,
            help_text=_("'Hectare ID'+'Shift'+'Date'+'Hectare Squirrel Number'"),
            )

    AM = 'AM'
    PM = 'PM'
    SHIFT_CHOICES = (
            (AM,'AM'),
            (PM,'PM'),
            )
    shift = models.CharField(
            max_length=2,
            choices=SHIFT_CHOICES,
            )

    date = models.DateField()

    ADULT = 'AD'
    JUVENILE = 'JU'
    AGE_CHOICES = (
            (ADULT,'Adult'),
            (JUVENILE,'Juvenile'),
            )
    age = models.CharField(
            max_length=10,
            choices=AGE_CHOICES,
            blank=True,
            )

    GRAY = 'GR'
    CINNAMON = 'CI'
    BLACK = 'BL'
    PRIMARY_FUR_COLOR_CHOICES = (
            (GRAY,'Gray'),
            (CINNAMON,'Cinnamon'),
            (BLACK,'Black'),
            )
    primary_fur_color = models.CharField(
            max_length=10,
            choices=PRIMARY_FUR_COLOR_CHOICES,
            blank=True,
            )

    GROUND_PLANE = 'GP'
    ABOVE_GROUND = 'AG'
    LOCATION_CHOICES = (
            (GROUND_PLANE,'Ground Plane'),
            (ABOVE_GROUND,'Above Ground'),
            )
    location = models.CharField(
            max_length=20,
            choices=LOCATION_CHOICES,
            blank=True,
            )

    specific_location = models.CharField(max_length=100,blank=True,)
    running = models.BooleanField()
    chasing = models.BooleanField()
    climbing = models.BooleanField()
    eating = models.BooleanField()
    foraging = models.BooleanField()
    other_activities = models.CharField(max_length=100,blank=True)
    kuks = models.BooleanField()
    quaas = models.BooleanField()
    moans = models.BooleanField()
    tail_flags = models.BooleanField()
    tail_twitches = models.BooleanField()
    approaches = models.BooleanField()
    indifferent = models.BooleanField()
    runs_from = models.BooleanField()

    def __str__(self):
        return self.unique_squirrel_id
