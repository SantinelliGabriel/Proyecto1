from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    return render (request, "Appcoder/inicio.html")

def musica(request):
    return render (request, "Appcoder/musica.html")


