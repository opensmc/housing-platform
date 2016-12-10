import json
from django.shortcuts import render
from django.http import Http404, HttpResponse
from housing_app.models import Applicant
from django.utils import timezone


def save_applicant(request, applicant_id=None):
  new_applicant_info = json.loads(request.body.decode('utf-8'))
  if request.method == 'POST':
    name = new_applicant_info['name']
    county = new_applicant_info['county']
    address = new_applicant_info['address']
    applicant = Applicant.objects.create(name = name, county = county, address = address, pub_date = timezone.now())
    return HttpResponse(json.dumps({'id': applicant.id}), content_type='application/json')
  elif request.method == 'PUT':
    applicant_id = new_applicant_info['id']
    applicant = Applicant.objects.get(pk=applicant_id)
    applicant.name = new_applicant_info['name']
    applicant.county = new_applicant_info['county']
    applicant.address = new_applicant_info['address']
    applicant.pub_date = timezone.now()
    applicant.save()
    return HttpResponse()    
  else:
    return Http404
  



def get_applicants(request):
  applicants = Applicant.objects.order_by("pub_date")
  data =[{'name': applicant.name, 'county': applicant.county, 'address': applicant.address, 'id': applicant.id} for applicant in applicants]
  return HttpResponse(json.dumps(data))
