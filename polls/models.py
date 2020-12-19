from django.db import models

# Create your models here.
class covid19(models.Model):
#    Date = models.DateTimeField(auto_now_add=True,auto_now=False)
    Index = models.BigIntegerField()
    Date = models.DateTimeField()
    NewConfirmed = models.BigIntegerField()
    TotalConfirmed = models.BigIntegerField()
    NewDeaths = models.BigIntegerField()
    TotalDeaths = models.BigIntegerField()
    NewRecovered = models.BigIntegerField()
    TotalRecovered = models.BigIntegerField()
    Country = models.CharField(max_length=30)
    CountryCode = models.CharField(max_length=30)
    Slug = models.CharField(max_length=30)
    NewConfirmed = models.BigIntegerField()
    TotalConfirmed = models.BigIntegerField()
    NewDeaths = models.BigIntegerField()
    TotalDeaths = models.BigIntegerField()



