from django.conf.urls import url
from . import views
from . import ajax

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^ajax/applicant/(?P<applicant_id>[0-9]*)$', ajax.save_applicant), 
    url(r'^ajax/applicants/$', ajax.get_applicants)  
]