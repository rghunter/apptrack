from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.application),
    url(r'^application/([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/recommend', views.recommend, name='letters-of-rec')
]
