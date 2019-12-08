from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Count, Q
from .models import Squirrels
from .forms import SightingForm


def map(request):
    """
    Return a map that displays the location of the squirrel sightings
    """
    sightings = Squirrels.objects.all()
    return render(request, 'track/map.html', locals())


def home(request):
    """
    Return a home page listing all squirrel sightings 
    with a single link to add sighting view 
    and with links to edit each sighting
    """
    sighting_list = Squirrels.objects.all()
    return render(request, 'track/home.html', locals())


def add_sightings(request):
    """
    Return a page to create a new sighting
    """
    if request.method == 'POST':
        form = SightingForm(request.POST)
        if form.is_valid():
            Squirrels.objects.create(**form.cleaned_data)
            return redirect('/track/sightings/')
        return HttpResponse(form.errors)
    else:
        form = SightingForm()
    return render(request, 'track/add.html', {'form':form})


def sighting_detail(request, unique_squirrel_id):
    """
    Return a page showing details for a particular sighting
    with a link to update the sighting,
    a link to delete the sighitng,
    a link to cancel the operation and return to home page
    """
    sighting = get_object_or_404(Squirrels, unique_squirrel_id=unique_squirrel_id)
    return render(request, 'track/detail.html', {'sighting':sighting})


def update_sightings(request, unique_squirrel_id):
    """
    Return a page to update a particular sighting
    """
    sighting = get_object_or_404(Squirrels, unique_squirrel_id=unique_squirrel_id)
    if request.method == 'POST':
        form = SightingForm(request.POST,instance=sighting)
        if form.is_valid():
            sighting = form.save()
            sighting.save()
            return redirect('sighting_detail', unique_squirrel_id=sighting.unique_squirrel_id)
    else:
        form = SightingForm(instance=sighting)
    return render(request, 'track/update.html', {'form':form})


def delete_sightings(request, unique_squirrel_id):
    """
    Delete a particular sighting from the database,
    and return a message for successfully deleting it
    """
    Squirrels.objects.filter(unique_squirrel_id=unique_squirrel_id).delete()
    return HttpResponse(f'You have successfully deleted sighting {unique_squirrel_id}!')

def stat(request):
    """
    Return a page showing several general stats of the Squirrel data
    """
    age = Squirrels.objects.values('age').annotate(count=Count('unique_squirrel_id'))
    color = Squirrels.objects.values('primary_fur_color').annotate(count=Count('unique_squirrel_id'))
    location = Squirrels.objects.values('location').annotate(count=Count('unique_squirrel_id'))
    flag_twitch = Squirrels.objects.filter(Q(tail_flags=True) & Q(tail_twitches=True)).aggregate(count=Count('unique_squirrel_id'))
    flag_notwitch = Squirrels.objects.filter(Q(tail_flags=True) & Q(tail_twitches=False)).aggregate(count=Count('unique_squirrel_id'))
    noflag_twitch = Squirrels.objects.filter(Q(tail_flags=False) & Q(tail_twitches=True)).aggregate(count=Count('unique_squirrel_id'))
    noflag_notwitch = Squirrels.objects.filter(Q(tail_flags=False) & Q(tail_twitches=False)).aggregate(count=Count('unique_squirrel_id'))
    eating = Squirrels.objects.filter(eating=True).values('primary_fur_color').annotate(count=Count('eating'))
    other = Squirrels.objects.values('other_activities').annotate(count=Count('unique_squirrel_id'))
    return render(request, 'track/stat.html', locals())
