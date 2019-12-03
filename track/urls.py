from django.urls import path
from . import views

urlpatterns = [
        path('sightings/',views.home,name='home'),
        path('sightings/add',views.add_sightings,name='add-sightings'),
        path('sightings/<str:unique_squirrel_id>',views.sighting_detail,name='sighting_detail'),
        ]
