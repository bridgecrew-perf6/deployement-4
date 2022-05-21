from django.contrib.gis.db import models
from datetime import date
from datetime import datetime
from django.utils.timezone import now
from numpy import delete


class tbl_Secteur(models.Model):
    id_secteur=models.AutoField(primary_key=True)
    sec_name = models.CharField(max_length=15,blank=True)
    wilaya_secteur=models.CharField(max_length=15,blank=True)
    sec_color=models.CharField(max_length=15,blank=True)
    poly = models.PolygonField(blank=True)
    sec_creator=models.CharField(max_length=15,blank=True)
    created_date = models.DateTimeField(default=now, editable=False)
    is_deleted=models.IntegerField(default=0)
    def __str__(self):
        return str(self.sec_name)


class tbl_Wilaya(models.Model):
    id_city=models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=35,blank=True)
    city_code=models.CharField(max_length=15,blank=True)
    city_poly=models.PolygonField(blank=True)
    def __str__(self):
        return str(self.city_name)