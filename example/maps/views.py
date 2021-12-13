from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.utils import timezone
from djgeojson.views import GeoJSONLayerView

from maps.models import MushroomSpot


def mushroom_data(request, mushroom_id):
    template = "maps/fragments/data.html"
    context = {}

    try:
        mushroom = MushroomSpot.objects.get(id=mushroom_id)
        context["mushroom"] = mushroom

    except MushroomSpot.DoesNotExist:
        pass

    return TemplateResponse(request, template, context)
