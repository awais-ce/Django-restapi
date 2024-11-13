from django.db import models

# Create your models here.


class Company(models.Model):
    Company_Type = (('Software House','Software House') , ('PVT LTD','PVT LTD') ,('Solar Panal','Solar Panal') ,('Partnership','Partnership'))
    name = models.CharField(max_length=122)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=140)
    state = models.CharField(max_length=160)
    country = models.CharField(max_length=200)
    companytype = models.CharField(choices=Company_Type , max_length=300)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=180)
    phone = models.CharField(max_length=40 , null=True)
    email = models.EmailField(unique=True)
    company = models.ForeignKey(Company , on_delete=models.CASCADE , related_name="employess")
    position = models.CharField(max_length=155)
    salary = models.IntegerField()
    joinning_date = models.DateField()

    def __str__(self):
        return self.first_name





