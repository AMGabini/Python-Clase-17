from django.template import Template, Context
from django.http import HttpResponse
import datetime

def bienvenida(request):
    return HttpResponse("Bienvenidos al curso de Django!!")

def bienvenida_html(request):
    hoy = datetime.datetime.now()
    response = f"""
    <html>
    <h1>Bienvenidos al curso de Django!!</h1>
    <h2>Esta es la comision 55630</h2>
    <h3>Hoy es {hoy} </h3>
    </html>
    """
    return HttpResponse(response)

def saludar(request, nombre):
    response = f"Hola! Bienvenida {nombre} al curso de Django"
    return HttpResponse(response)

def calcular_bruto(resquest, neto):
    neto = int(neto)
    response = f"<html><h1>El bruto de la factura es ${neto*1.21} </h1></html>"
    return HttpResponse(response)

def saludar2(request, nombre, apellido):
    response = f"Hola! Bienvenida {nombre} {apellido} al curso de Django"
    return HttpResponse(response)

def bienvenida_template(resquest):
    miHtml = open("C:/Users/Antito/Desktop/Python/Clase_17/proyecto/proyecto/plantillas/bienvenido.html") 
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)
    