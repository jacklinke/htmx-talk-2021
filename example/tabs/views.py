from django.shortcuts import render
from django.template.response import TemplateResponse

from tabs.forms import FormOne, FormTwo, FormThree, FormFour, FormFive


def tabs_view(request):
    template = "tabs/tabs.html"
    context = {}

    post_data = request.POST or None

    # Set defaults
    form_one = FormOne(
        prefix="form_one",
        initial={
            "username": request.user.username,
            "email": request.user.email
        }
    )
    form_two = FormTwo(
        prefix="form_two",
        initial={
            "username": request.user.username,
            "email": request.user.email
        }
    )
    form_three = FormThree(
        prefix="form_three",
        initial={
            "username": request.user.username,
            "email": request.user.email
        }
    )
    form_four = FormFour(
        prefix="form_four",
        initial={
            "username": request.user.username,
            "email": request.user.email
        }
    )
    form_five = FormFive(
        prefix="form_five",
        initial={
            "username": request.user.username,
            "email": request.user.email
        }
    )

    if request.method == 'POST':
        # For each form, if the submit button name is in the POST, process and save that form
        if "submit_one" in request.POST:
            form_one = FormOne(
                post_data, prefix="form_one"
            )
            if form_one.is_valid():
                context["success"] = "Success!"

        if "submit_two" in request.POST:
            form_two = FormTwo(
                post_data, prefix="form_two"
            )
            if form_two.is_valid():
                context["success"] = "Success!"

        if "submit_three" in request.POST:
            form_three = FormThree(
                post_data, prefix="form_three"
            )
            if form_three.is_valid():
                context["success"] = "Success!"

        if "submit_four" in request.POST:
            form_four = FormFour(
                post_data, prefix="form_four"
            )
            if form_four.is_valid():
                context["success"] = "Success!"

        if "submit_five" in request.POST:
            form_five = FormFive(
                post_data, prefix="form_five"
            )
            if form_five.is_valid():
                context["success"] = "Success!"

    context["form_one"] = form_one
    context["form_two"] = form_two
    context["form_three"] = form_three
    context["form_four"] = form_four
    context["form_five"] = form_five
    

    return TemplateResponse(request, template, context)


def tabs_htmx_view(request):
    template = "tabs/tabs_htmx.html"

    context = {}

    return TemplateResponse(request, template, context)


def form_one_htmx_view(request):
    template = "tabs/fragments/form_one.html"
    context = {}
    form_one = FormOne(
        initial={
            "username": request.user.username,
            "email": request.user.email
        }
    )

    if request.method == 'POST':
        form_one = FormOne(request.POST)
        if form_one.is_valid():
            context["success"] = "Success!"

    context["form_one"] = form_one

    return TemplateResponse(request, template, context)


def form_two_htmx_view(request):
    template = "tabs/fragments/form_two.html"
    context = {}
    form_two = FormTwo(
        initial={
            "username": request.user.username,
            "email": request.user.email
        }
    )

    if request.method == 'POST':
        form_two = FormTwo(request.POST)
        if form_two.is_valid():
            context["success"] = "Success!"

    context["form_two"] = form_two

    return TemplateResponse(request, template, context)


def form_three_htmx_view(request):
    template = "tabs/fragments/form_three.html"
    context = {}
    form_three = FormThree(
        initial={
            "username": request.user.username,
            "email": request.user.email
        }
    )

    if request.method == 'POST':
        form_three = FormThree(request.POST)
        if form_three.is_valid():
            context["success"] = "Success!"

    context["form_three"] = form_three

    return TemplateResponse(request, template, context)


def form_four_htmx_view(request):
    template = "tabs/fragments/form_four.html"
    context = {}
    form_four = FormFour(
        initial={
            "username": request.user.username,
            "email": request.user.email
        }
    )

    if request.method == 'POST':
        form_four = FormFour(request.POST)
        if form_four.is_valid():
            context["success"] = "Success!"

    context["form_four"] = form_four

    return TemplateResponse(request, template, context)


def form_five_htmx_view(request):
    template = "tabs/fragments/form_five.html"
    context = {}
    form_five = FormFive(
        initial={
            "username": request.user.username,
            "email": request.user.email
        }
    )

    if request.method == 'POST':
        form_five = FormFive(request.POST)
        if form_five.is_valid():
            context["success"] = "Success!"

    context["form_five"] = form_five

    return TemplateResponse(request, template, context)
