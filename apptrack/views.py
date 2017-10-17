from django.shortcuts import render
from models import ApplicationForm, RecommendationLetterForm
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
            return HttpResponse(loader.get_template('apptrack/submit_app.html').render({"app_id": str(f.id)}))
        return HttpResponse(template.render({ "form" : ApplicationForm(request.POST) }, request))
    return HttpResponse(template.render({ "form" : ApplicationForm() }, request))

def letterofrec(request, application_id):
    template = loader.get_template('apptrack/form.html')
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        app = RecommendationLetterForm(request.POST)
        # check whether it's valid:
        if app.is_valid():
            f = app.save(commit=False)
            f.application_id = application_id
            f.save()
            return HttpResponse(loader.get_template('apptrack/finish.html').render())
        return HttpResponse(template.render({ "form" : RecommendationLetterForm(request.POST) }, request))
    return HttpResponse(template.render({ "form" : RecommendationLetterForm() }, request))

