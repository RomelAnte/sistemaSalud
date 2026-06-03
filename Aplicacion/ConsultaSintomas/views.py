from django.shortcuts import render
import json
from django.http import JsonResponse
from Aplicacion.ConsultaSintomas.sistema_experto import obtener_diagnostico


def home(request):
    return render(request, 'consultaSintomas.html')


def diagnostico(request):
    if request.method == 'POST':
        # Procesar datos del formulario
        # Los checkboxes que no están marcados no aparecen en POST
        hechos = {
            "tiene_fiebre": "tiene_fiebre" in request.POST,
            "tiene_tos": "tiene_tos" in request.POST,
            "tiene_congestion_nasal": "tiene_congestion_nasal" in request.POST,
            "tiene_dolor_de_garganta": "tiene_dolor_de_garganta" in request.POST,
            "tiene_erupciones": "tiene_erupciones" in request.POST,
            "tiene_dolor_de_cabeza": "tiene_dolor_de_cabeza" in request.POST
        }
        
        print("DEBUG - Hechos recibidos:", hechos)
        
        # Ejecutar el diagnóstico
        resultado = obtener_diagnostico(hechos)
        
        print("DEBUG - Resultado diagnóstico:", resultado)
        
        return JsonResponse({
            "diagnosticos": resultado,
            "exito": True
        })
    
    return render(request, "diagnostico.html")