from django.urls import path
from users.views import settings, settings_htmx

app_name = "users"

urlpatterns = [
    path("settings/", settings, name="settings"),
    path("settings_htmx/", settings_htmx, name="settings_htmx"),
]
