import json
import sys


def obtener_diagnostico(hechos):
    diagnostico = []

    # Definición de reglas
    if hechos.get("tiene_fiebre") and hechos.get("tiene_tos") and hechos.get("tiene_congestion_nasal"):
        diagnostico.append("gripe")
    if hechos.get("tiene_fiebre") and hechos.get("tiene_dolor_de_garganta"):
        diagnostico.append("amigdalitis")
    if hechos.get("tiene_fiebre") and hechos.get("tiene_erupciones"):
        diagnostico.append("sarampion")
    if hechos.get("tiene_dolor_de_cabeza") and hechos.get("tiene_fiebre"):
        diagnostico.append("migraña")
    if hechos.get("tiene_congestion_nasal") and hechos.get("tiene_tos"):
        diagnostico.append("resfriado común")

    # Si no hay diagnóstico
    if not diagnostico:
        diagnostico.append("No se encontró un diagnóstico")

    return diagnostico

if __name__ == "__main__":
    # Leer argumentos
    hechos = json.loads(sys.argv[1])
    resultado = obtener_diagnostico(hechos)
    print(", ".join(resultado))