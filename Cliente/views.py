from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *


def objeto(request):
    cliente = Cliente(nome='maria')
    cliente.save()
    clientes =Cliente.objects.all()
    return HttpResponse(clientes)
