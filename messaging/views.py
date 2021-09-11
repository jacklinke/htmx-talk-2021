from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse
from django.urls import reverse

from messaging.models import Message

def inbox(request):
    template = "messaging/inbox.html"

    if request.method == "POST":
        message_id = request.POST.get('item')
        message = get_object_or_404(Message, id=message_id)
        if message.to_user == request.user:
            message.mark_read()

    messages = Message.objects.filter(to_user=request.user)
    context = {'messages': messages}


    return TemplateResponse(request, template, context)


def inbox_htmx(request):
    template = "messaging/inbox_htmx.html"

    if request.method == "POST":
        message_id = request.POST.get('item')
        message = get_object_or_404(Message, id=message_id)
        if message.to_user == request.user:
            message.mark_read()

        template = "messaging/fragments/message_fragment.html"
        context = {'message': message}
        return TemplateResponse(request, template, context)

    messages = Message.objects.filter(to_user=request.user)
    context = {'messages': messages}


    return TemplateResponse(request, template, context)
