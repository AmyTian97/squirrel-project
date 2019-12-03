from django.urls import path
from . import views

urlpatterns = [
        path('sightings/',views.home,name='home'),
        path('sightings/<str:unique_squirrel_id>',views.sighting_detail,name='sighting_detail'),
        ]
