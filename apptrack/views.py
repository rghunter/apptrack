from django.shortcuts import render
from apptrack.models import ApplicationForm, RecommendationLetterForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from templated_email import send_templated_mail
from django.conf import settings
from django.urls import reverse


from django import forms

def application(request):
    template = loader.get_template('apptrack/form.html')
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        app = ApplicationForm(request.POST)
        # check whether it's valid:
        if app.is_valid():
            application_instance = app.save()
            lor_url = request.build_absolute_uri(reverse('letters-of-rec',args=[application_instance.id]))
            ## Send an email to the scholarship recipient with instructions regarding letters of recomendations
            send_templated_mail(
                    template_name='submit_app',
                    from_email=settings.DEFAULT_FROM_EMAIL,  # We should set this to scholarships@bts.org
                    recipient_list=[application_instance.email],
                    context={
                        'first_name': application_instance.first_name,
                        "scholarship_name": application_instance.scholarship,
                        "lor_url": lor_url
                        }
                    )            
            return HttpResponse(loader.get_template('apptrack/submit_app.html').render({"lor_url": lor_url}))
        return HttpResponse(template.render({ "form" : ApplicationForm(request.POST) }, request))
    return HttpResponse(template.render({ "form" : ApplicationForm() }, request))

def recommend(request, application_id):
    template = loader.get_template('apptrack/form.html')
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        app = RecommendationLetterForm(request.POST)
        # check whether it's valid:
        if app.is_valid():
            f = app.save(commit=False)
            f.application_id = application_id
            f.save()
            return HttpResponse(loader.get_template('apptrack/submit_lor.html').render())
        return HttpResponse(template.render({ "form" : RecommendationLetterForm(request.POST) }, request))
    return HttpResponse(template.render({ "form" : RecommendationLetterForm() }, request))

