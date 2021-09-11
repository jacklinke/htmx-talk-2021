from django.urls import path
from tabs.views import (
    tabs_view, tabs_htmx_view,
    form_one_htmx_view,
    form_two_htmx_view,
    form_three_htmx_view,
    form_four_htmx_view,
    form_five_htmx_view
)

app_name = "tabs"

urlpatterns = [
    path("tabs/", tabs_view, name="tabs_view"),
    path("tabs_htmx/", tabs_htmx_view, name="tabs_htmx_view"),
    path("form_one/", form_one_htmx_view, name="form_one"),
    path("form_two/", form_two_htmx_view, name="form_two"),
    path("form_three/", form_three_htmx_view, name="form_three"),
    path("form_four/", form_four_htmx_view, name="form_four"),
    path("form_five/", form_five_htmx_view, name="form_five"),   
]