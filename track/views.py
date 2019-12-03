from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Squirrels
from .forms import SightingForm




def home(request):
    sighting_list = Squirrels.objects.all()
    return render(request, 'track/home.html', locals())


def sighting_detail(request,unique_squirrel_id):
    sighting = get_object_or_404(Squirrels, unique_squirrel_id=unique_squirrel_id)
    return render(request, 'track/detail.html', {'sighting':sighting})
