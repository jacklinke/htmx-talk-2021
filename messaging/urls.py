from django.urls import path
from messaging.views import inbox, inbox_htmx

app_name = "messaging"

urlpatterns = [
    path("inbox/", inbox, name="inbox"),
    path("inbox_htmx/", inbox_htmx, name="inbox_htmx"),
]