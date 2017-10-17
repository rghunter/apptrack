from django.shortcuts import render
from models import ApplicationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from django import forms

def application(request):
    template = loader.get_template('apptrack/form.html')
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        app = ApplicationForm(request.POST)
        # check whether it's valid:
        if app.is_valid():
            f = app.save()
            return HttpResponse(loader.get_template('apptrack/finish.html').render())
        return HttpResponse(template.render({ "form" : ApplicationForm(request.POST) }, request))
    return HttpResponse(template.render({ "form" : ApplicationForm() }, request))

