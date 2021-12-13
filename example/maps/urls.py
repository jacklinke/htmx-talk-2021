from django.shortcuts import render
from django.urls import path
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView

from maps.models import MushroomSpot
from maps.views import mushroom_data

app_name = "maps"

urlpatterns = [
    path('', TemplateView.as_view(template_name='maps/map.html'), name='map'),
    path('htmx', TemplateView.as_view(template_name='maps/map_htmx.html'), name='map_htmx'),
    path('data.geojson', GeoJSONLayerView.as_view(model=MushroomSpot, properties=('title', 'description', 'picture_url', 'id')), name='data'),
    path("<mushroom_id>/", mushroom_data, name="mushroom_data"),
]