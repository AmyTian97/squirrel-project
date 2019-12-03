from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Squirrels
from .forms import SightingForm




def home(request):
    sighting_list = Squirrels.objects.all()
    return render(request, 'track/home.html', locals())

# Create your views here.
