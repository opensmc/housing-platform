from django.db import models

# Create your models here.
class Applicant(models.Model):
  name = models.CharField(max_length=200)
  county = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')