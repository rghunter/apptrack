from django.contrib import admin

from apptrack.models import Application, Scholarship, RecommendationLetter

admin.site.register(Application)
admin.site.register(Scholarship)
admin.site.register(RecommendationLetter)
# Register your models here.
