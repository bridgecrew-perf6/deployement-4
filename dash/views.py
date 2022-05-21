from django.shortcuts import render
from django.http import HttpResponse
from dash.models import tbl_Secteur
from datetime import date
from datetime import datetime
from django.contrib.gis.geos import GEOSGeometry
import json

def index(request):
    return render(request,'index.html')

def dashboard(request):
    if 'enrg' in request.POST:
        poly = request.POST.get('js_data_input')
        sec = request.POST.get('sec_name')
        wilaya = request.POST.get('wilaya')
        current_user = request.user
        now = datetime.now()
        poly_object = json.loads(poly)
        pnt = GEOSGeometry(str(poly_object["geometry"])) # GeoJSOn
        Tbl_Secteur=tbl_Secteur(sec_name=sec,wilaya_secteur=wilaya,poly=pnt,sec_creator=current_user)
        Tbl_Secteur.save()
        context={}
        Q1=tbl_Secteur.objects.all()
        poly_list=Q1
        context['poly_list']=poly_list
        print(Q1)

        

    return render(request,'dashboard.html')

def maps(request):
    return render(request,'maps.html')

    
