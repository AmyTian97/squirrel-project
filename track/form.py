from django.forms import ModelForm
from .models import Squirrels

class SightingForm(ModelForm):
    class Meta:
        model = Squirrels
        fields = '__all__'
