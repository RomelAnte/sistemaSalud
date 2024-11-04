from django.shortcuts import render
import json
import subprocess
from django.http import JsonResponse
from Aplicacion.ConsultaSintomas.sistema_experto import obtener_diagnostico

# Create your views here.

def home(request):
    return render(request, 'consultaSintomas.html')

def diagnostico(request):
    if request.method == 'POST':
        # Procesar datos del formulario
        hechos = {
            "tiene_fiebre": request.POST.get("tiene_fiebre") == "on",
            "tiene_tos": request.POST.get("tiene_tos") == "on",
            "tiene_congestion_nasal": request.POST.get("tiene_congestion_nasal") == "on",
            "tiene_dolor_de_garganta": request.POST.get("tiene_dolor_de_garganta") == "on",
            "tiene_erupciones": request.POST.get("tiene_erupciones") == "on",
            "tiene_dolor_de_cabeza": request.POST.get("tiene_dolor_de_cabeza") == "on"
        }
        command = ["python", "path_to_clips_script.py", str(hechos)]
        result = subprocess.run(command, capture_output=True, text=True)
        # Ejecuta el diagnóstico
        resultado = result.stdout.strip() if result.returncode == 0 else "Error en el diagnóstico"
        diagnostico = ", ".join(resultado)

        return JsonResponse({"diagnostico": diagnostico})  # Enviar respuesta JSON

    return render(request, "diagnostico.html")