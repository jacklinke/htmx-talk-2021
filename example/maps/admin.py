from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin

from . import models as maps_models


admin.site.register(maps_models.MushroomSpot, LeafletGeoAdmin)