import json
import sys


def obtener_diagnostico(hechos):
    """
    Sistema experto para diagnóstico de enfermedades comunes.
    Devuelve un diccionario con diagnósticos ordenados por confianza.
    """
    diagnosticos = {}

    # Regla 1: GRIPE - Fiebre + Tos + Congestión nasal
    if hechos.get("tiene_fiebre") and hechos.get("tiene_tos") and hechos.get("tiene_congestion_nasal"):
        diagnosticos["Gripe"] = {
            "confianza": 95,
            "sintomas_detectados": 3,
            "descripcion": "Infección viral respiratoria. Se recomienda reposo y antitérmicos."
        }
    
    # Regla 2: AMIGDALITIS - Fiebre + Dolor de garganta (+ posible tos)
    if hechos.get("tiene_fiebre") and hechos.get("tiene_dolor_de_garganta"):
        confianza = 90 if hechos.get("tiene_tos") else 85
        diagnosticos["Amigdalitis"] = {
            "confianza": confianza,
            "sintomas_detectados": 2 if not hechos.get("tiene_tos") else 3,
            "descripcion": "Inflamación de las amígdalas. Consulte a un médico si persiste."
        }
    
    # Regla 3: SARAMPIÓN - Fiebre + Erupciones + Tos
    if hechos.get("tiene_fiebre") and hechos.get("tiene_erupciones"):
        confianza = 92 if hechos.get("tiene_tos") else 80
        diagnosticos["Sarampión"] = {
            "confianza": confianza,
            "sintomas_detectados": 2 if not hechos.get("tiene_tos") else 3,
            "descripcion": "Enfermedad viral grave. Requiere atención médica inmediata."
        }
    
    # Regla 4: RESFRIADO COMÚN - Congestión nasal + Tos (sin fiebre o con fiebre leve)
    if hechos.get("tiene_congestion_nasal") and hechos.get("tiene_tos"):
        confianza = 85 if not hechos.get("tiene_fiebre") else 75
        diagnosticos["Resfriado Común"] = {
            "confianza": confianza,
            "sintomas_detectados": 2,
            "descripcion": "Infección viral leve de vías respiratorias superiores."
        }
    
    # Regla 5: MIGRAÑA/CEFALEA - Dolor de cabeza + Fiebre
    if hechos.get("tiene_dolor_de_cabeza") and hechos.get("tiene_fiebre"):
        diagnosticos["Cefalea Febril"] = {
            "confianza": 70,
            "sintomas_detectados": 2,
            "descripcion": "Dolor de cabeza asociado a fiebre. Puede estar relacionado con otra infección."
        }
    
    # Regla 6: ALERGIA - Congestión nasal sin fiebre + Tos leve
    if hechos.get("tiene_congestion_nasal") and not hechos.get("tiene_fiebre") and hechos.get("tiene_tos"):
        diagnosticos["Alergia Respiratoria"] = {
            "confianza": 65,
            "sintomas_detectados": 2,
            "descripcion": "Posible reacción alérgica. Evite alérgenos comunes."
        }
    
    # Regla 7: Solo dolor de garganta sin fiebre
    if hechos.get("tiene_dolor_de_garganta") and not hechos.get("tiene_fiebre"):
        diagnosticos["Irritación Leve de Garganta"] = {
            "confianza": 60,
            "sintomas_detectados": 1,
            "descripcion": "Irritación no infecciosa. Manténgase hidratado."
        }

    # Ordenar por confianza
    diagnosticos_ordenados = sorted(
        diagnosticos.items(),
        key=lambda x: x[1]["confianza"],
        reverse=True
    )

    # Si hay diagnósticos, devolver los 3 principales
    if diagnosticos_ordenados:
        resultado = [
            {
                "nombre": nombre,
                "confianza": info["confianza"],
                "descripcion": info["descripcion"]
            }
            for nombre, info in diagnosticos_ordenados[:3]
        ]
        return resultado
    else:
        return [{
            "nombre": "Insuficientes síntomas",
            "confianza": 0,
            "descripcion": "No se puede determinar un diagnóstico. Seleccione más síntomas."
        }]


if __name__ == "__main__":
    # Leer argumentos
    hechos = json.loads(sys.argv[1])
    resultado = obtener_diagnostico(hechos)
    print(json.dumps(resultado, ensure_ascii=False))