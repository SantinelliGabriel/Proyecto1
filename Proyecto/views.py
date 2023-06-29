from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo (request):
    return HttpResponse("Hola Django - Coder")

def segundavista(request):
    return HttpResponse("<br><br> <h1>Ya entendimos esto, es muy simple :)<h1>")

def diahoy(request):

    dia = datetime.datetime.now()
    documentoDeTexto =f"Hoy es dia: {dia}"
    return HttpResponse(documentoDeTexto)


def miNombreEs(self, nombre):
    documentoDeTexto = f"Mi nombre es <br><br> {nombre}"
    return HttpResponse(documentoDeTexto)

def probandoTemplate(self):
    miHtml = open("C:/Users/gabi_/Documents/Python/PythonProyecto1/Proyecto1/Proyecto1/plantillas/template1.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContext = Context()
    documento = plantilla.render(miContext)
    nombre = "Gabriel"
    apellido = "Santinelli"
    diccionario = {

        "nombre" :  nombre,
        "apellido" : apellido

    }

    miHtml = open ("C:/Users/gabi_/Documents/Python/PythonProyecto1/Proyecto1/Proyecto1/plantillas/template1.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContext = Context(diccionario)
    documento = plantilla.render (miContext)
    return HttpResponse(documento)




