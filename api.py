from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from corrector import cargar_ejercicios, obtener_ejercicio, corregir
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse


# Crear la aplicación FastAPI
app = FastAPI(
    title="Plataforma Python API",
    description="API para plataforma de ejercicios de Python con corrección automática",
    version="1.0.0"
)


# Permitir que el frontend (que va a correr en otro puerto) se comunique con la API.
# Esto se llama CORS. Sin esto, el navegador bloquea la comunicación por seguridad.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción esto sería solo tu dominio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================================================================
# MODELOS: definen la "forma" de los datos que entran y salen
# ==========================================================================

class SolucionRequest(BaseModel):
    """Lo que el frontend envía cuando el estudiante da 'Enviar'"""
    codigo: str
    ejercicio_id: int


# ==========================================================================
# ENDPOINTS: las "URLs" que ofrece la API
# ==========================================================================

@app.get("/")
def raiz():
    """Endpoint de prueba. Si esto responde, la API está viva."""
    return {
        "mensaje": "Plataforma Python API funcionando 🐍",
        "docs": "Visitá /docs para ver la documentación interactiva"
    }


@app.get("/ejercicios")
def listar_ejercicios():
    """Devuelve la lista de todos los ejercicios disponibles (sin los tests ocultos)."""
    ejercicios = cargar_ejercicios()
    # Devolvemos solo lo necesario para el listado (título, id, cantidad de tests)
    return [
        {
            "id": ej["id"],
            "titulo": ej["titulo"],
            "nivel": ej.get("nivel", "facil"),
            "cantidad_tests": len(ej["tests"])
        }
        for ej in ejercicios
    ]

@app.get("/ejercicios/{ejercicio_id}")
def obtener_ejercicio_detalle(ejercicio_id: int):
    """Devuelve el detalle de un ejercicio específico (enunciado, código inicial, tests visibles)."""
    ejercicio = obtener_ejercicio(ejercicio_id)
    if ejercicio is None:
        raise HTTPException(status_code=404, detail=f"Ejercicio {ejercicio_id} no encontrado")
    
    return {
        "id": ejercicio["id"],
        "titulo": ejercicio["titulo"],
        "nivel": ejercicio.get("nivel", "facil"),
        "enunciado": ejercicio["enunciado"],
        "codigo_inicial": ejercicio["codigo_inicial"],
        "tests_visibles": ejercicio["tests"]
    }


@app.post("/corregir")
def corregir_solucion(datos: SolucionRequest):
    """Recibe el código del estudiante y devuelve el resultado de los tests."""
    ejercicio = obtener_ejercicio(datos.ejercicio_id)
    if ejercicio is None:
        raise HTTPException(status_code=404, detail=f"Ejercicio {datos.ejercicio_id} no encontrado")
    
    resultado = corregir(datos.codigo, ejercicio)
    return resultado
# Servir archivos estáticos (CSS, JS, imágenes) desde la carpeta static/
app.mount("/static", StaticFiles(directory="static"), name="static")


# La página principal sirve el index.html
@app.get("/app", include_in_schema=False)
def servir_app():
    return FileResponse("static/index.html")