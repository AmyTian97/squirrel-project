from django.urls import path
from . import views

urlpatterns = [
        path('map/',views.map),
        path('sightings/',views.home,name='home'),
        path('sightings/stat/',views.stat,name='stat'),
        path('sightings/add/',views.add_sightings,name='add-sightings'),
        path('sightings/<str:unique_squirrel_id>/',views.sighting_detail,name='sighting_detail'),
        path('sightings/<str:unique_squirrel_id>/update/',views.update_sightings,name='update_sightings'),
        path('sightings/<str:unique_squirrel_id>/delete/',views.delete_sightings,name='delete_sightings'),
        ]
