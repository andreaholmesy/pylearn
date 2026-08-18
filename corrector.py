import json
from motor import ejecutar_codigo


def cargar_ejercicios(archivo="ejercicios.json"):
    """Lee el archivo JSON y devuelve la lista de ejercicios."""
    with open(archivo, encoding='utf-8') as f:
        return json.load(f)


def obtener_ejercicio(id_ejercicio, archivo="ejercicios.json"):
    """Devuelve un ejercicio específico por su id."""
    ejercicios = cargar_ejercicios(archivo)
    for ej in ejercicios:
        if ej["id"] == id_ejercicio:
            return ej
    return None


def corregir(codigo_estudiante, ejercicio):
    """
    Corrige la solución del estudiante contra los tests del ejercicio.
    
    Devuelve un diccionario con:
        - tests_pasados: cuántos tests pasaron
        - tests_totales: cuántos tests había
        - detalles: lista con el resultado de cada test
        - todo_ok: True si pasaron todos
    """
    resultados = []
    pasados = 0
    
    for test in ejercicio["tests"]:
        # Armamos un script: el código del estudiante + el print del test
        script = f"{codigo_estudiante}\n\nprint(repr({test['entrada']}))"
        
        # Lo ejecutamos con el motor
        r = ejecutar_codigo(script, timeout=5)
        
        # Comparamos la salida con lo esperado
        salida = r["stdout"].strip()
        esperado = test["esperado"].strip()
        
        # Normalizamos: repr de True es 'True', repr de 'aloh' es "'aloh'"
        paso = (salida == esperado) and r["exit_code"] == 0
        
        if paso:
            pasados += 1
        
        resultados.append({
            "entrada": test["entrada"],
            "esperado": esperado,
            "obtenido": salida if not r["stderr"] else f"ERROR: {r['stderr'].strip().splitlines()[-1]}",
            "paso": paso
        })
    
    return {
        "tests_pasados": pasados,
        "tests_totales": len(ejercicio["tests"]),
        "detalles": resultados,
        "todo_ok": pasados == len(ejercicio["tests"])
    }


def mostrar_resultado(resultado):
    """Imprime el resultado de la corrección de forma amigable."""
    print(f"\n{'='*50}")
    print(f"Tests pasados: {resultado['tests_pasados']} / {resultado['tests_totales']}")
    print(f"{'='*50}")
    
    for i, det in enumerate(resultado["detalles"], 1):
        emoji = "✅" if det["paso"] else "❌"
        print(f"\n{emoji} Test {i}: {det['entrada']}")
        print(f"   Esperado: {det['esperado']}")
        print(f"   Obtenido: {det['obtenido']}")
    
    print(f"\n{'='*50}")
    if resultado["todo_ok"]:
        print("🎉 ¡Perfecto! Pasaron todos los tests.")
    else:
        print(f"Faltan {resultado['tests_totales'] - resultado['tests_pasados']} tests por resolver.")
    print(f"{'='*50}\n")


# Zona de prueba
if __name__ == "__main__":
    # Cargamos el ejercicio 1 (es_par)
    ejercicio = obtener_ejercicio(1)
    print(f"Ejercicio: {ejercicio['titulo']}")
    print(f"Enunciado: {ejercicio['enunciado']}\n")
    
    # Prueba 1: solución CORRECTA
    print(">>> Probando una solución CORRECTA:")
    solucion_buena = """
def es_par(n):
    return n % 2 == 0
"""
    resultado = corregir(solucion_buena, ejercicio)
    mostrar_resultado(resultado)
    
    # Prueba 2: solución INCORRECTA (solo funciona para positivos)
    print("\n>>> Probando una solución INCORRECTA:")
    solucion_mala = """
def es_par(n):
    if n == 2 or n == 0:
        return True
    return False
"""
    resultado = corregir(solucion_mala, ejercicio)
    mostrar_resultado(resultado)