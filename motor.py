import subprocess
import tempfile
import os

def ejecutar_codigo(codigo, timeout=5):
    """
    Ejecuta código Python en un proceso separado con timeout.
    
    Argumentos:
        codigo: string con el código Python a ejecutar.
        timeout: segundos máximos que puede tardar (default 5).
    
    Devuelve un diccionario con:
        - stdout: lo que imprimió el código
        - stderr: los errores que dio (si dio)
        - exit_code: 0 si salió bien, otro número si falló
        - timeout: True si el código tardó demasiado
    """
    # Creamos un archivo temporal con el código
    with tempfile.NamedTemporaryFile(
        mode='w',
        suffix='.py',
        delete=False,
        encoding='utf-8'
    ) as archivo:
        archivo.write(codigo)
        ruta_archivo = archivo.name
    
    resultado = {
        "stdout": "",
        "stderr": "",
        "exit_code": None,
        "timeout": False
    }
    
    try:
        # Ejecutamos el código con Python, con un tiempo máximo
        proceso = subprocess.run(
            ["python", ruta_archivo],
            capture_output=True,
            text=True,
            timeout=timeout,
            encoding='utf-8'
        )
        resultado["stdout"] = proceso.stdout
        resultado["stderr"] = proceso.stderr
        resultado["exit_code"] = proceso.returncode
    
    except subprocess.TimeoutExpired:
        resultado["timeout"] = True
        resultado["stderr"] = f"El código tardó más de {timeout} segundos."
    
    finally:
        # Borramos el archivo temporal siempre
        os.unlink(ruta_archivo)
    
    return resultado


# Zona de prueba: solo corre si ejecutamos este archivo directamente
if __name__ == "__main__":
    print("=== Prueba 1: código simple ===")
    codigo1 = 'print("Hola desde el motor")\nprint(2 + 2)'
    r = ejecutar_codigo(codigo1)
    print(f"Salida: {r['stdout']}")
    print(f"Exit code: {r['exit_code']}")
    
    print("\n=== Prueba 2: código con error ===")
    codigo2 = 'print("Antes del error")\nx = 1/0'
    r = ejecutar_codigo(codigo2)
    print(f"Salida: {r['stdout']}")
    print(f"Error: {r['stderr']}")
    print(f"Exit code: {r['exit_code']}")
    
    print("\n=== Prueba 3: bucle infinito (debería cortarse) ===")
    codigo3 = 'while True:\n    pass'
    r = ejecutar_codigo(codigo3, timeout=2)
    print(f"Timeout: {r['timeout']}")
    print(f"Error: {r['stderr']}")