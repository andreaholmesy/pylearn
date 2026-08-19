\# 📘 Manual Técnico — PyLearn



Documentación técnica completa del proyecto PyLearn: plataforma de ejercicios de Python con corrección automática.



\---



\## 📑 Tabla de contenidos



1\. \[Visión general](#1-visión-general)

2\. \[Arquitectura](#2-arquitectura)

3\. \[Stack tecnológico](#3-stack-tecnológico)

4\. \[Estructura del proyecto](#4-estructura-del-proyecto)

5\. \[Instalación desde cero](#5-instalación-desde-cero)

6\. \[Cómo funciona cada componente](#6-cómo-funciona-cada-componente)

7\. \[Endpoints de la API](#7-endpoints-de-la-api)

8\. \[Formato de ejercicios](#8-formato-de-ejercicios)

9\. \[Cómo agregar un nuevo ejercicio](#9-cómo-agregar-un-nuevo-ejercicio)

10\. \[Deploy en Render](#10-deploy-en-render)

11\. \[Consideraciones de seguridad](#11-consideraciones-de-seguridad)

12\. \[Solución de problemas](#12-solución-de-problemas)



\---



\## 1. Visión general



\*\*PyLearn\*\* es una plataforma web para practicar Python. Un estudiante entra, elige un ejercicio, escribe código en un editor, y el sistema ejecuta ese código contra una batería de tests automáticos, dando feedback inmediato sobre qué funcionó y qué no.



El proyecto está compuesto por:



\- \*\*Motor de ejecución\*\* de código Python con sandbox básico (timeout, aislamiento).

\- \*\*Sistema de corrección\*\* que compara la salida del código contra resultados esperados.

\- \*\*API REST\*\* con FastAPI que expone el motor por HTTP.

\- \*\*Frontend web\*\* con HTML + Tailwind CSS + Monaco Editor (el editor de VSCode).

\- \*\*Deploy\*\* en Render (plan gratuito).



\---



\## 2. Arquitectura



Diagrama simplificado del flujo:

┌─────────────────┐ ┌──────────────────┐ ┌─────────────────┐

│ │ HTTP │ │ │ │

│ Navegador │────────▶│ FastAPI │────────▶│ corrector.py │

│ (index.html) │◀────────│ (api.py) │◀────────│ motor.py │

│ │ JSON │ │ │ │

└─────────────────┘ └──────────────────┘ └─────────────────┘

│

▼

┌──────────────────┐

│ ejercicios.json │

└──────────────────┘



\*\*Flujo típico:\*\*



1\. El navegador carga `index.html` desde `/app`.

2\. JavaScript hace un `GET /ejercicios` para llenar la lista de la sidebar.

3\. Al elegir un ejercicio, hace `GET /ejercicios/{id}` para traer el enunciado.

4\. Cuando el usuario da "Enviar solución", hace `POST /corregir` con el código.

5\. FastAPI recibe el pedido, llama a `corregir()` en `corrector.py`.

6\. `corrector.py` construye un script con el código del usuario + los tests, y llama a `ejecutar\_codigo()` en `motor.py`.

7\. `motor.py` crea un archivo temporal, lo ejecuta con `subprocess` con timeout, y captura la salida.

8\. El resultado sube por la cadena hasta el navegador, que muestra el feedback visual.



\---



\## 3. Stack tecnológico



\### Backend



| Tecnología | Versión | Uso |

|------------|---------|-----|

| Python | 3.10+ | Lenguaje base |

| FastAPI | 0.115 | Framework para la API REST |

| Uvicorn | 0.32 | Servidor ASGI que corre FastAPI |

| subprocess | (stdlib) | Ejecución del código de usuarios |

| tempfile | (stdlib) | Creación de archivos temporales |

| json | (stdlib) | Lectura del archivo de ejercicios |



\### Frontend



| Tecnología | Uso |

|------------|-----|

| HTML5 | Estructura |

| Tailwind CSS (CDN) | Estilos |

| Monaco Editor (CDN) | Editor de código con resaltado |

| Google Fonts (Nunito) | Tipografía |

| JavaScript vanilla | Lógica del cliente |

| localStorage | Persistencia local del progreso |



\### Infraestructura



| Tecnología | Uso |

|------------|-----|

| Git + GitHub | Control de versiones y hosting del código |

| Render | Deploy en producción (plan free) |



\### Por qué NO usamos npm



Se tomó la decisión consciente de no usar el ecosistema npm para minimizar la superficie de ataque de supply chain attacks (compromisos como Shai-Hulud, chalk/debug, axios). En vez de eso, todas las librerías frontend (Tailwind, Monaco) se cargan desde CDN oficial en el navegador.



\---



\## 4. Estructura del proyecto

pylearn/

├── motor.py # Motor de ejecución segura de código Python

├── corrector.py # Sistema de corrección con tests

├── api.py # API REST con FastAPI

├── ejercicios.json # Base de datos de ejercicios

├── requirements.txt # Dependencias de Python

├── .gitignore # Archivos ignorados por Git

├── README.md # Portada del proyecto

├── MANUAL\_TECNICO.md # Este documento

├── MANUAL\_USUARIO.md # Manual para el usuario final

└── static/

└── index.html # Interfaz web completa (HTML + JS + CSS)



Cada archivo tiene una responsabilidad única y bien delimitada.



\---



\## 5. Instalación desde cero



\### Requisitos previos



\- \*\*Python 3.10 o superior\*\*  

&#x20; Verificar con `python --version`. Si no lo tienes, descárgalo de \[python.org](https://python.org).

\- \*\*Git\*\*  

&#x20; Verificar con `git --version`. Si no, descárgalo de \[git-scm.com](https://git-scm.com).

\- \*\*Un editor de código\*\* (recomendado VSCode, pero no obligatorio).



\### Instalación



```bash

\# 1. Clonar el repositorio

git clone https://github.com/andreaholmesy/pylearn.git

cd pylearn



\# 2. Instalar dependencias

pip install -r requirements.txt



\# 3. Arrancar el servidor

uvicorn api:app --reload

```



Una vez arrancado, tendrás:



\- \*\*La API\*\* en `http://localhost:8000`

\- \*\*La documentación interactiva\*\* en `http://localhost:8000/docs`

\- \*\*La app web\*\* en `http://localhost:8000/app`



Ctrl + C en la terminal para detener el servidor.



\---



\## 6. Cómo funciona cada componente



\### `motor.py` — Ejecutor de código



Recibe código Python como string, lo escribe en un archivo temporal, lo ejecuta con `subprocess.run()` con un timeout configurable, y captura la salida y errores.



\*\*Función principal:\*\*



```python

ejecutar\_codigo(codigo: str, timeout: int = 5) -> dict

```



Devuelve un diccionario con:



\- `stdout`: lo que imprimió el código.

\- `stderr`: errores de ejecución.

\- `exit\_code`: 0 si todo salió bien, otro número si falló.

\- `timeout`: True si el código tardó más del límite.



Este es el componente más crítico en cuanto a seguridad: aísla la ejecución del código de terceros del servidor principal.



\### `corrector.py` — Sistema de tests



Lee `ejercicios.json`, y para cada solución enviada:



1\. Toma el código del usuario.

2\. Agrega automáticamente el print de cada test (`print(repr(nombre\_funcion(argumentos)))`).

3\. Ejecuta ese script combinado con `motor.py`.

4\. Compara la salida obtenida con el resultado esperado del test.

5\. Devuelve un diccionario con detalles por test y estadísticas.



\*\*Funciones principales:\*\*



\- `cargar\_ejercicios()` — carga todos los ejercicios desde el JSON.

\- `obtener\_ejercicio(id)` — devuelve uno específico.

\- `corregir(codigo, ejercicio)` — ejecuta la corrección completa.



\### `api.py` — API REST



Wrapper de FastAPI sobre las funciones anteriores. Expone endpoints HTTP que el frontend puede consumir. También sirve los archivos estáticos (el HTML).



Ver la sección \[Endpoints de la API](#7-endpoints-de-la-api) para el detalle.



\### `ejercicios.json` — Base de datos



Archivo JSON con la lista completa de ejercicios. Cada uno tiene id, título, nivel, enunciado, código inicial y tests.



Ver \[Formato de ejercicios](#8-formato-de-ejercicios).



\### `static/index.html` — Frontend



Un único archivo HTML que contiene:



\- La estructura de la página (header, sidebar, contenido principal).

\- Estilos con Tailwind CSS cargado desde CDN.

\- Editor Monaco cargado desde CDN.

\- JavaScript vanilla con toda la lógica del cliente (fetch de la API, renderizado, gamificación, linter).



Se decidió mantenerlo como un solo archivo para simplificar el despliegue y no depender de npm.



\---



\## 7. Endpoints de la API



FastAPI genera automáticamente documentación interactiva en `/docs` (Swagger UI).



\### `GET /`



Endpoint de verificación. Si responde, la API está viva.



\*\*Respuesta:\*\*

```json

{

&#x20; "mensaje": "Plataforma Python API funcionando 🐍",

&#x20; "docs": "Visitá /docs para ver la documentación interactiva"

}

```



\### `GET /ejercicios`



Devuelve la lista de todos los ejercicios (sin exponer los tests, solo metadatos).



\*\*Respuesta:\*\*

```json

\[

&#x20; {

&#x20;   "id": 1,

&#x20;   "titulo": "Función es\_par",

&#x20;   "nivel": "facil",

&#x20;   "cantidad\_tests": 4

&#x20; },

&#x20; ...

]

```



\### `GET /ejercicios/{id}`



Devuelve el detalle de un ejercicio específico, incluyendo los tests.



\*\*Respuesta:\*\*

```json

{

&#x20; "id": 1,

&#x20; "titulo": "Función es\_par",

&#x20; "nivel": "facil",

&#x20; "enunciado": "Escribe una función llamada 'es\_par'...",

&#x20; "codigo\_inicial": "def es\_par(n):\\n    pass\\n",

&#x20; "tests\_visibles": \[

&#x20;   {"entrada": "es\_par(2)", "esperado": "True"},

&#x20;   ...

&#x20; ]

}

```



Devuelve \*\*404\*\* si el ejercicio no existe.



\### `POST /corregir`



Recibe el código del estudiante, lo corrige contra los tests, y devuelve el resultado.



\*\*Body:\*\*

```json

{

&#x20; "codigo": "def es\_par(n):\\n    return n % 2 == 0",

&#x20; "ejercicio\_id": 1

}

```



\*\*Respuesta:\*\*

```json

{

&#x20; "tests\_pasados": 4,

&#x20; "tests\_totales": 4,

&#x20; "detalles": \[

&#x20;   {

&#x20;     "entrada": "es\_par(2)",

&#x20;     "esperado": "True",

&#x20;     "obtenido": "True",

&#x20;     "paso": true

&#x20;   },

&#x20;   ...

&#x20; ],

&#x20; "todo\_ok": true

}

```



\### `GET /app`



Sirve la interfaz web (el HTML principal).



\---



\## 8. Formato de ejercicios



Cada ejercicio en `ejercicios.json` tiene esta estructura:



```json

{

&#x20; "id": 1,

&#x20; "titulo": "Nombre corto del ejercicio",

&#x20; "nivel": "facil",

&#x20; "enunciado": "Descripción de qué debe hacer la función.",

&#x20; "codigo\_inicial": "def nombre\_funcion(param):\\n    # Tu código aquí\\n    pass\\n",

&#x20; "tests": \[

&#x20;   {"entrada": "nombre\_funcion(argumento)", "esperado": "resultado\_esperado"},

&#x20;   ...

&#x20; ]

}

```



\### Campos



| Campo | Tipo | Descripción |

|-------|------|-------------|

| `id` | int | Identificador único. Debe ser único en todo el archivo. |

| `titulo` | string | Nombre corto que aparece en la sidebar. |

| `nivel` | string | Uno de: `"facil"`, `"medio"`, `"dificil"`. Determina el color y XP. |

| `enunciado` | string | Descripción completa del problema. |

| `codigo\_inicial` | string | Plantilla que ve el estudiante al empezar. |

| `tests` | array | Lista de objetos con `entrada` y `esperado`. |



\### Formato de tests



Cada test es un diccionario con dos strings:



\- \*\*`entrada`\*\*: expresión Python que se va a evaluar. Típicamente una llamada a la función.

\- \*\*`esperado`\*\*: la representación string exacta del resultado esperado, tal como Python lo mostraría con `repr()`.



\*\*Importante:\*\* los strings esperados deben coincidir \*\*exactamente\*\* con la salida. Ejemplos:



\- Para `True` o `False`: `"True"` / `"False"` (con mayúscula).

\- Para números: `"42"`, `"3.14"`.

\- Para strings: incluir las comillas simples, ejemplo `"'hola'"`.

\- Para listas: `"\[1, 2, 3]"` (con espacios después de las comas).

\- Para diccionarios: `"{'clave': 'valor'}"`.



Si dudas del formato exacto, en un Python interactivo hacé `print(repr(tu\_resultado))` y ese es el string que va en `esperado`.



\---



\## 9. Cómo agregar un nuevo ejercicio



\### Paso 1: elegir un id



Abre `ejercicios.json` y elige el siguiente id disponible (si el último es 15, usa 16).



\### Paso 2: escribir la solución primero



Antes de armar el ejercicio, escribe \*\*tu solución correcta\*\* en un editor aparte y probá que funcione con los inputs que quieres usar como tests. Esto evita que crees ejercicios con tests imposibles o incorrectos.



\### Paso 3: agregar la entrada al JSON



Agrega un nuevo objeto al array, siguiendo el formato de la sección anterior. Cuida:



\- La coma después del ejercicio anterior.

\- El id único.

\- Comillas dobles siempre (JSON no acepta comillas simples).

\- Escapar comillas dentro de strings con `\\"`.



\### Paso 4: probar la corrección



Reinicia el servidor si estabas corriendo con `uvicorn` (o si tiene `--reload` se hace solo). Abre la app, el nuevo ejercicio debe aparecer en la sidebar. Pruébalo con tu solución correcta y verifica que pase todos los tests. También prueba con una solución incorrecta a propósito para asegurarte de que los tests \*\*fallen\*\* cuando deben.



\### Paso 5: commit y push



```bash

git add ejercicios.json

git commit -m "Agregar ejercicio: \[nombre del ejercicio]"

git push

```



Render redeployará automáticamente.



\---



\## 10. Deploy en Render



\### Configuración inicial



El proyecto ya está configurado para deploy en Render con estos parámetros:



\- \*\*Runtime:\*\* Python 3

\- \*\*Build Command:\*\* `pip install -r requirements.txt`

\- \*\*Start Command:\*\* `uvicorn api:app --host 0.0.0.0 --port $PORT`

\- \*\*Instance Type:\*\* Free



\### Deploy automático



Render está conectado al repositorio GitHub del proyecto. Cada `git push` a la rama `main` dispara automáticamente un nuevo deploy. El proceso tarda entre 3 y 5 minutos.



\### Verificar el estado



En el dashboard de Render, la pestaña \*\*Events\*\* muestra el historial de deploys. Los logs en vivo se ven en \*\*Logs\*\*.



Cuando un deploy termina con éxito, aparece el mensaje:

==> Your service is live 🎉

==> Available at your primary URL https://\[tu-servicio].onrender.com



\### Limitaciones del plan Free



\- \*\*Sleep tras 15 minutos de inactividad.\*\* La primera visita después de dormir tarda 30-60 segundos en despertar el servidor. Después funciona normal.

\- \*\*512 MB de RAM, 0.1 CPU.\*\* Suficiente para tráfico bajo.

\- \*\*No hay SSH ni acceso directo al servidor.\*\*



\### Variables de entorno



En el estado actual del proyecto no se requieren variables de entorno. Todo funciona con la configuración por defecto.



\---



\## 11. Consideraciones de seguridad



\### Ejecución de código de usuarios



El motor ejecuta código arbitrario proporcionado por los usuarios. Se han tomado las siguientes precauciones:



\- \*\*Timeout obligatorio de 5 segundos\*\* para prevenir bucles infinitos.

\- \*\*Proceso separado\*\* con `subprocess.run()` (no `exec()` directo).

\- \*\*Archivos temporales eliminados\*\* siempre después de la ejecución (uso de `try/finally`).



\### Limitaciones actuales



Para uso en producción con usuarios completamente no confiables, se recomienda migrar a un sandbox más robusto:



\- \*\*Docker efímero:\*\* un contenedor descartable por cada ejecución.

\- \*\*gVisor:\*\* sandbox a nivel de kernel.

\- \*\*Servicios especializados:\*\* Judge0, Piston (con self-hosting apropiado).



\### CORS



Actualmente el CORS está configurado como `allow\_origins=\["\*"]`, que acepta cualquier origen. Para producción con usuarios reales, se recomienda restringirlo al dominio propio.



\### Datos de usuarios



El proyecto no tiene backend de usuarios ni base de datos de personas. Toda la información de progreso (XP, racha, ejercicios completados) se guarda en `localStorage` del navegador y \*\*no viaja al servidor\*\*. Esto significa:



\- Cero recolección de datos personales.

\- Cumplimiento trivial de GDPR/leyes de privacidad.

\- Si el usuario limpia el navegador, pierde su progreso.



\---



\## 12. Solución de problemas



\### La API arranca pero `/app` no muestra nada



\- Verifica que la carpeta `static/` existe y contiene `index.html`.

\- Verifica en la consola del navegador (F12) si hay errores 404 o de CORS.



\### El linter marca errores donde no los hay



\- El linter solo detecta problemas de indentación y dos puntos faltantes. Es orientativo.

\- Puedes ignorar sus avisos si tu código funciona: el botón "Enviar" sigue activo.



\### El deploy en Render falla



\- Revisa los logs en la pestaña "Logs" del servicio.

\- Errores comunes:

&#x20; - `ModuleNotFoundError`: falta agregar la librería a `requirements.txt`.

&#x20; - `Address already in use`: el Start Command tiene un puerto hardcodeado en vez de `$PORT`.



\### Cambios locales no se ven en el navegador



\- Prueba \*\*Ctrl + F5\*\* para forzar recarga sin caché.

\- Verifica que `uvicorn` esté corriendo con `--reload`.



\### Un ejercicio da "obtenido" distinto al "esperado" siendo aparentemente iguales



\- Es un problema de formato exacto. `True` y `true` son distintos. Revisar mayúsculas, espacios, comillas.

\- En `repr()` los strings incluyen sus comillas. `"hola"` en un test se representa como `"'hola'"` (con comillas dentro).



\---



\## Créditos



\*\*Proyecto:\*\* PyLearn  

\*\*Autora:\*\* Andrea Reyes  

\*\*Repositorio:\*\* \[github.com/andreaholmesy/pylearn](https://github.com/andreaholmesy/pylearn)  

\*\*Licencia:\*\* MIT



\---

