from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
from django.forms.models import model_to_dict
import requests
from django.core import serializers


def objeto(request):
    lista_json=[]
    cliente = Cliente(nome='maria')
    cliente.save()
    clientes =Cliente.objects.all().values()
    return clientes
    # for cli in clientes:
    #     lista_json.append({})
    # cliente_list = list(clientes)
    # cliente_json = JsonResponse(cliente_list,safe=False)
    # return HttpResponse(clientes, content_type="application/json")
