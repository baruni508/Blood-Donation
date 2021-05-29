from django.db import models

# Create your models here.
class Donor(models.Model):
  donor_name=models.CharField(max_lenght=60)
  donor_age=models.IntegerField()
  donor_address=models.FloatField()
  donor_number=models.IntergerField(max_lenght=50)
