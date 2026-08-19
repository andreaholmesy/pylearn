# 📘 Manual Técnico — PyLearn

Documentación técnica completa del proyecto PyLearn: plataforma de ejercicios de Python con corrección automática.

---

## 📑 Tabla de contenidos

1. Visión general
2. Arquitectura
3. Stack tecnológico
4. Estructura del proyecto
5. Instalación desde cero
6. Cómo funciona cada componente
7. Endpoints de la API
8. Formato de ejercicios
9. Cómo agregar un nuevo ejercicio
10. Deploy en Render
11. Consideraciones de seguridad
12. Solución de problemas

---

## 1. Visión general

**PyLearn** es una plataforma web para practicar Python. Un estudiante entra, elige un ejercicio, escribe código en un editor, y el sistema ejecuta ese código contra una batería de tests automáticos, dando feedback inmediato sobre qué funcionó y qué no.

El proyecto está compuesto por:

- **Motor de ejecución** de código Python con sandbox básico (timeout, aislamiento).
- **Sistema de corrección** que compara la salida del código contra resultados esperados.
- **API REST** con FastAPI que expone el motor por HTTP.
- **Frontend web** con HTML, Tailwind CSS y Monaco Editor (el editor de VSCode).
- **Deploy** en Render (plan gratuito).

---

## 2. Arquitectura

**Flujo de comunicación:**

El navegador carga la interfaz desde el servidor FastAPI. Cuando el usuario interactúa (elige ejercicio o envía solución), el JavaScript del navegador hace peticiones HTTP a la API. FastAPI recibe esas peticiones, llama a las funciones del corrector, que a su vez usan el motor de ejecución. El motor crea un archivo temporal con el código, lo ejecuta con timeout, y devuelve el resultado hasta que llega de vuelta al navegador.

**Flujo típico paso a paso:**

1. El navegador carga index.html desde la ruta /app.
2. JavaScript hace un GET a /ejercicios para llenar la lista de la sidebar.
3. Al elegir un ejercicio, hace GET a /ejercicios/{id} para traer el enunciado.
4. Cuando el usuario da "Enviar solución", hace POST a /corregir con el código.
5. FastAPI recibe el pedido y llama a corregir() en corrector.py.
6. corrector.py construye un script con el código del usuario más los tests, y llama a ejecutar_codigo() en motor.py.
7. motor.py crea un archivo temporal, lo ejecuta con subprocess con timeout, y captura la salida.
8. El resultado sube por la cadena hasta el navegador, que muestra el feedback visual.

---

## 3. Stack tecnológico

### Backend

- **Python 3.10+** — lenguaje base.
- **FastAPI 0.115** — framework para la API REST.
- **Uvicorn 0.32** — servidor ASGI que corre FastAPI.
- **subprocess** (librería estándar) — ejecución del código de usuarios.
- **tempfile** (librería estándar) — creación de archivos temporales.
- **json** (librería estándar) — lectura del archivo de ejercicios.

### Frontend

- **HTML5** — estructura.
- **Tailwind CSS** (vía CDN) — estilos.
- **Monaco Editor** (vía CDN) — editor de código con resaltado de sintaxis.
- **Google Fonts (Nunito)** — tipografía.
- **JavaScript vanilla** — lógica del cliente.
- **localStorage** — persistencia local del progreso.

### Infraestructura

- **Git + GitHub** — control de versiones y hosting del código.
- **Render** — deploy en producción (plan free).

### Por qué NO usamos npm

Se tomó la decisión consciente de no usar el ecosistema npm para minimizar la superficie de ataque de supply chain attacks. En vez de eso, todas las librerías frontend (Tailwind, Monaco) se cargan desde CDN oficial en el navegador.

---

## 4. Estructura del proyecto

La carpeta raíz del proyecto contiene:

- **motor.py** — motor de ejecución segura de código Python.
- **corrector.py** — sistema de corrección con tests.
- **api.py** — API REST con FastAPI.
- **ejercicios.json** — base de datos de ejercicios.
- **requirements.txt** — dependencias de Python.
- **.gitignore** — archivos ignorados por Git.
- **README.md** — portada del proyecto.
- **MANUAL_TECNICO.md** — este documento.
- **MANUAL_USUARIO.md** — manual para el usuario final.
- **static/index.html** — interfaz web completa (dentro de la subcarpeta static).

Cada archivo tiene una responsabilidad única y bien delimitada.

---

## 5. Instalación desde cero

### Requisitos previos

- **Python 3.10 o superior.** Verificar con: python --version.
- **Git.** Verificar con: git --version.
- **Un editor de código** (recomendado VSCode).

### Pasos de instalación

1. Clonar el repositorio: git clone https://github.com/andreaholmesy/pylearn.git
2. Entrar a la carpeta: cd pylearn
3. Instalar dependencias: pip install -r requirements.txt
4. Arrancar el servidor: uvicorn api:app --reload

Una vez arrancado, se tiene disponible:

- **API** en http://localhost:8000
- **Documentación interactiva** en http://localhost:8000/docs
- **App web** en http://localhost:8000/app

Se detiene con Ctrl + C en la terminal.

---

## 6. Cómo funciona cada componente

### motor.py — Ejecutor de código

Recibe código Python como string, lo escribe en un archivo temporal, lo ejecuta con subprocess.run() con timeout configurable, y captura la salida y errores.

Función principal: **ejecutar_codigo(codigo, timeout=5)**.

Devuelve un diccionario con:

- **stdout** — lo que imprimió el código.
- **stderr** — errores de ejecución.
- **exit_code** — 0 si todo salió bien, otro número si falló.
- **timeout** — True si el código tardó más del límite.

Este es el componente más crítico en cuanto a seguridad, ya que aísla la ejecución del código de terceros.

### corrector.py — Sistema de tests

Lee ejercicios.json, y para cada solución enviada:

1. Toma el código del usuario.
2. Agrega automáticamente el print de cada test.
3. Ejecuta el script combinado con motor.py.
4. Compara la salida obtenida con el resultado esperado.
5. Devuelve un diccionario con detalles por test y estadísticas.

Funciones principales:

- **cargar_ejercicios()** — carga todos los ejercicios desde el JSON.
- **obtener_ejercicio(id)** — devuelve uno específico.
- **corregir(codigo, ejercicio)** — ejecuta la corrección completa.

### api.py — API REST

Wrapper de FastAPI sobre las funciones anteriores. Expone endpoints HTTP que el frontend puede consumir. También sirve los archivos estáticos (el HTML).

### ejercicios.json — Base de datos

Archivo JSON con la lista completa de ejercicios. El formato se detalla en la sección 8.

### static/index.html — Frontend

Un único archivo HTML que contiene la estructura de la página, estilos con Tailwind CSS cargado desde CDN, editor Monaco cargado desde CDN, y toda la lógica JavaScript del cliente.

Se decidió mantenerlo como un solo archivo para simplificar el despliegue y no depender de npm.

---

## 7. Endpoints de la API

FastAPI genera automáticamente documentación interactiva en /docs (Swagger UI).

### GET /

Endpoint de verificación. Si responde, la API está viva. Devuelve un mensaje de bienvenida.

### GET /ejercicios

Devuelve la lista de todos los ejercicios (sin exponer los tests, solo metadatos: id, título, nivel y cantidad de tests).

### GET /ejercicios/{id}

Devuelve el detalle de un ejercicio específico, incluyendo el enunciado, el código inicial y los tests visibles. Devuelve error 404 si el ejercicio no existe.

### POST /corregir

Recibe el código del estudiante junto con el ID del ejercicio, corrige contra los tests y devuelve el resultado detallado (tests pasados, totales, y detalle por cada test).

### GET /app

Sirve la interfaz web (el HTML principal).

---

## 8. Formato de ejercicios

Cada ejercicio en ejercicios.json tiene los siguientes campos:

- **id** (int) — identificador único, debe ser único en todo el archivo.
- **titulo** (string) — nombre corto que aparece en la sidebar.
- **nivel** (string) — uno de: facil, medio, dificil. Determina el color y el XP.
- **enunciado** (string) — descripción completa del problema.
- **codigo_inicial** (string) — plantilla que ve el estudiante al empezar.
- **tests** (array) — lista de objetos con entrada y esperado.

### Formato de tests

Cada test es un diccionario con dos campos string:

- **entrada** — expresión Python que se va a evaluar. Típicamente una llamada a la función que el estudiante debe implementar.
- **esperado** — representación string exacta del resultado esperado, tal como Python lo mostraría con repr().

**Importante:** los strings esperados deben coincidir exactamente con la salida.

Ejemplos de formato de valores esperados:

- Para True o False: "True" o "False" (con mayúscula).
- Para números: "42" o "3.14".
- Para strings: incluir las comillas simples. Ejemplo: "'hola'".
- Para listas: "[1, 2, 3]" (con espacios después de las comas).
- Para diccionarios: "{'clave': 'valor'}".

Si hay dudas del formato exacto, en un Python interactivo se hace print(repr(tu_resultado)) y ese es el string que va en esperado.

---

## 9. Cómo agregar un nuevo ejercicio

### Paso 1: elegir un id

Abrir ejercicios.json y elegir el siguiente id disponible.

### Paso 2: escribir la solución primero

Antes de armar el ejercicio, escribir la solución correcta en un editor aparte y probar que funcione con los inputs que se van a usar como tests. Esto evita crear ejercicios con tests imposibles o incorrectos.

### Paso 3: agregar la entrada al JSON

Agregar un nuevo objeto al array, siguiendo el formato de la sección 8. Cuidar:

- La coma después del ejercicio anterior.
- El id único.
- Comillas dobles siempre (JSON no acepta comillas simples).
- Escapar comillas dentro de strings con backslash.

### Paso 4: probar la corrección

Reiniciar el servidor si no está corriendo con --reload. Abrir la app, verificar que el nuevo ejercicio aparezca en la sidebar. Probarlo con la solución correcta y verificar que pase todos los tests. También probar con una solución incorrecta a propósito para asegurar que los tests fallen cuando deben.

### Paso 5: commit y push

Guardar los cambios en Git con git add, git commit y git push. Render redeployará automáticamente.

---

## 10. Deploy en Render

### Configuración inicial

El proyecto está configurado para deploy en Render con estos parámetros:

- **Runtime:** Python 3
- **Build Command:** pip install -r requirements.txt
- **Start Command:** uvicorn api:app --host 0.0.0.0 --port $PORT
- **Instance Type:** Free

### Deploy automático

Render está conectado al repositorio GitHub del proyecto. Cada push a la rama main dispara automáticamente un nuevo deploy. El proceso tarda entre 3 y 5 minutos.

### Verificar el estado

En el dashboard de Render, la pestaña Events muestra el historial de deploys. Los logs en vivo se ven en Logs.

### Limitaciones del plan Free

- **Sleep tras 15 minutos de inactividad.** La primera visita después de dormir tarda 30 a 60 segundos en despertar el servidor. Después funciona normal.
- **512 MB de RAM, 0.1 CPU.** Suficiente para tráfico bajo.
- **No hay SSH ni acceso directo al servidor.**

---

## 11. Consideraciones de seguridad

### Ejecución de código de usuarios

El motor ejecuta código arbitrario proporcionado por los usuarios. Se han tomado las siguientes precauciones:

- **Timeout obligatorio de 5 segundos** para prevenir bucles infinitos.
- **Proceso separado** usando subprocess.run() en vez de exec() directo.
- **Archivos temporales eliminados** siempre después de la ejecución (uso de try/finally).

### Limitaciones actuales

Para uso en producción con usuarios completamente no confiables, se recomienda migrar a un sandbox más robusto:

- **Docker efímero** — un contenedor descartable por cada ejecución.
- **gVisor** — sandbox a nivel de kernel.
- **Servicios especializados** — Judge0 o Piston con self-hosting apropiado.

### CORS

Actualmente el CORS está configurado como allow_origins con asterisco, aceptando cualquier origen. Para producción con usuarios reales, se recomienda restringirlo al dominio propio.

### Datos de usuarios

El proyecto no tiene backend de usuarios ni base de datos de personas. Toda la información de progreso (XP, racha, ejercicios completados) se guarda en localStorage del navegador y no viaja al servidor. Esto significa:

- Cero recolección de datos personales.
- Cumplimiento trivial de leyes de privacidad.
- Si el usuario limpia el navegador, pierde su progreso.

---

## 12. Solución de problemas

### La API arranca pero /app no muestra nada

- Verificar que la carpeta static existe y contiene index.html.
- Verificar en la consola del navegador (F12) si hay errores de recursos no encontrados o problemas de CORS.

### El linter marca errores donde no los hay

- El linter solo detecta problemas de indentación y dos puntos faltantes. Es orientativo.
- Se pueden ignorar sus avisos si el código funciona: el botón "Enviar" sigue activo.

### El deploy en Render falla

- Revisar los logs en la pestaña Logs del servicio.
- Errores comunes:
  - **ModuleNotFoundError** — falta agregar la librería a requirements.txt.
  - **Address already in use** — el Start Command tiene un puerto hardcodeado en vez de la variable de entorno PORT.

### Cambios locales no se ven en el navegador

- Probar Ctrl + F5 para forzar recarga sin caché.
- Verificar que uvicorn esté corriendo con --reload.

### Un ejercicio da "obtenido" distinto al "esperado" siendo aparentemente iguales

- Es un problema de formato exacto. True y true son distintos. Revisar mayúsculas, espacios, comillas.
- En repr(), los strings incluyen sus comillas: "hola" en un test se representa como "'hola'" (con comillas dentro).

---

## Créditos

**Proyecto:** PyLearn

**Autora:** Andrea Reyes

**Repositorio:** github.com/andreaholmesy/pylearn

**Licencia:** MIT
