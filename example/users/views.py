from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse
from django.urls import reverse


def settings(request):
    template = "users/settings.html"
    context = {}

    if request.method == "POST":
        user = request.user

        setting_value = request.POST.get('settings')

        # Set/un-set settings booleans
        if setting_value == "setting_one":
            request.user.toggle_setting_one()
        
        if setting_value == "setting_two":
            request.user.toggle_setting_two()

        if setting_value == "setting_three":
            request.user.toggle_setting_three()
        
        if setting_value == "setting_four":
            request.user.toggle_setting_four()

    return TemplateResponse(request, template, context)


def settings_htmx(request):
    template = "users/settings_htmx.html"
    context = {}

    if request.method == "POST":
        user = request.user
        successful_toggle = False

        setting_value = request.POST.get('settings')

        # Set/un-set settings booleans
        if setting_value == "setting_one":
            request.user.toggle_setting_one()
            successful_toggle = True
        
        if setting_value == "setting_two":
            request.user.toggle_setting_two()
            successful_toggle = True

        if setting_value == "setting_three":
            request.user.toggle_setting_three()
            successful_toggle = True
        
        if setting_value == "setting_four":
            request.user.toggle_setting_four()
            successful_toggle = True
        
        if successful_toggle:
            return HttpResponse(
                (
                    '<div _="on load wait 2s then remove me" '
                    'class="alert alert-success alert-dismissible fade show" '
                    'role="alert">'
                    '<i class="icon-like menu-icon text-success"></i>'
                    '</div>'
                ),
                status=200,
                content_type="text/html",
            )

    return TemplateResponse(request, template, context)
