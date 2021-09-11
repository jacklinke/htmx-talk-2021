from django.shortcuts import render
from django.template.response import TemplateResponse

from tabs.forms import FormOne, FormTwo, FormThree, FormFour, FormFive


def tabs_view(request):
    template = "tabs/tabs.html"

    post_data = request.POST or None

    # Set defaults
    form_one = FormOne(
        prefix="form_one", instance=request.user
    )
    form_two = FormTwo(
        prefix="form_two", instance=request.user
    )
    form_three = FormThree(
        prefix="form_three", instance=request.user
    )
    form_four = FormFour(
        prefix="form_four", instance=request.user
    )
    form_five = FormFive(
        prefix="form_five", instance=request.user
    )

    if request.method == 'POST':
        # For each form, if the submit button name is in the POST, process and save that form
        if "submit_one" in request.POST:
            form_one = FormOne(
                post_data, prefix="form_one", instance=request.user
            )
            if form_one.is_valid():
                form_one.save()

        if "submit_two" in request.POST:
            form_two = FormTwo(
                post_data, prefix="form_two", instance=request.user
            )
            if form_two.is_valid():
                form_two.save()

        if "submit_three" in request.POST:
            form_three = FormThree(
                post_data, prefix="form_three", instance=request.user
            )
            if form_three.is_valid():
                form_three.save()

        if "submit_four" in request.POST:
            form_four = FormFour(
                post_data, prefix="form_four", instance=request.user
            )
            if form_four.is_valid():
                form_four.save()

        if "submit_five" in request.POST:
            form_five = FormFive(
                post_data, prefix="form_five", instance=request.user
            )
            if form_five.is_valid():
                form_five.save()

    context = {
        "form_one": form_one,
        "form_two": form_two,
        "form_three": form_three,
        "form_four": form_four,
        "form_five": form_five,
    }

    return TemplateResponse(request, template, context)


def tabs_htmx_view(request):
    template = "tabs/tabs_htmx.html"

    context = {}

    return TemplateResponse(request, template, context)


def form_one_htmx_view(request):
    template = "tabs/fragments/form_one.html"

    form_one = FormOne(instance=request.user)

    if request.method == 'POST':
        post_data = request.POST or None

        form_one = FormOne(
            post_data, instance=request.user
        )
        if form_one.is_valid():
            form_one.save()

    context = {"form_one": form_one}

    return TemplateResponse(request, template, context)


def form_two_htmx_view(request):
    template = "tabs/fragments/form_two.html"

    form_two = FormTwo(instance=request.user)

    if request.method == 'POST':
        post_data = request.POST or None

        form_two = FormTwo(
            post_data, instance=request.user
        )
        if form_two.is_valid():
            form_two.save()

    context = {"form_two": form_two}

    return TemplateResponse(request, template, context)


def form_three_htmx_view(request):
    template = "tabs/fragments/form_three.html"

    form_three = FormThree(instance=request.user)

    if request.method == 'POST':
        post_data = request.POST or None

        form_three = FormThree(
            post_data, instance=request.user
        )
        if form_three.is_valid():
            form_three.save()

    context = {"form_three": form_three}

    return TemplateResponse(request, template, context)


def form_four_htmx_view(request):
    template = "tabs/fragments/form_four.html"

    form_four = FormFour(instance=request.user)

    if request.method == 'POST':
        post_data = request.POST or None

        form_four = FormFour(
            post_data, instance=request.user
        )
        if form_four.is_valid():
            form_four.save()

    context = {"form_four": form_four}

    return TemplateResponse(request, template, context)


def form_five_htmx_view(request):
    template = "tabs/fragments/form_five.html"

    form_five = FormFive(instance=request.user)

    if request.method == 'POST':
        post_data = request.POST or None

        form_five = FormFive(
            post_data, instance=request.user
        )
        if form_five.is_valid():
            form_five.save()

    context = {"form_five": form_five}

    return TemplateResponse(request, template, context)
