from django.test import TestCase
from django.http import HttpResponse

# Create your tests here.

def hola(request):
    return HttpResponse("Que onda Pa")