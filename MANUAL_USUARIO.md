# 📖 Manual de Usuario — PyLearn

Bienvenida a PyLearn, la plataforma para aprender Python jugando. Esta guía te muestra cómo aprovechar la app al máximo, aunque nunca hayas programado antes.

---

## 📑 Contenido

1. Qué es PyLearn
2. Cómo empezar
3. La pantalla de bienvenida
4. Elegir un ejercicio
5. La pantalla de ejercicio
6. Escribir tu solución
7. Enviar y ver resultados
8. El sistema de puntos (XP y racha)
9. Los tres niveles de dificultad
10. El linter: tu ayudante mientras escribes
11. Consejos para no atascarte
12. Preguntas frecuentes

---

## 1. Qué es PyLearn

PyLearn es una plataforma web para practicar programación en **Python**, uno de los lenguajes de programación más populares del mundo. Está pensada para principiantes: empiezas con ejercicios muy fáciles y vas subiendo de dificultad a tu ritmo.

**Cómo funciona en pocas palabras:**

- Eliges un ejercicio de una lista.
- Lees el enunciado (te dice qué tienes que hacer).
- Escribes tu solución en el editor.
- Haces clic en el botón "Enviar" y el sistema te dice si está bien o mal, con detalle.
- Ganas puntos (XP) por cada ejercicio resuelto.

**Es gratis, sin registro, y tu progreso se guarda automáticamente en tu navegador.**

---

## 2. Cómo empezar

### Requisitos

Necesitas:

- Una computadora o tablet (funciona mejor que en celular).
- Un navegador web moderno (Chrome, Edge, Firefox, Safari).
- Conexión a internet.
- Conocimientos básicos de Python (o ganas de aprenderlos sobre la marcha).

### Abrir la app

Simplemente entra a la URL de la plataforma en tu navegador. **No hay que registrarse ni crear cuenta.** La primera vez que entres puede tardar unos 30 a 60 segundos en cargar (el servidor está despertando). Después funciona normal.

---

## 3. La pantalla de bienvenida

Al entrar por primera vez ves:

- **Banner grande verde** con el título "Aprende Python jugando" y la mascota 🐍.
- **Tres tarjetas** que explican los pasos: Lee el enunciado, Escribe tu código, Recibe feedback.
- **Sección con estadísticas** (15 ejercicios, 3 niveles, hasta 350 XP).
- **Botón grande verde "Empezar 🚀"** que te lleva al primer ejercicio.
- **Sidebar izquierda** con la lista de todos los ejercicios organizados por nivel.

Si entras desde el celular, verás también un aviso amarillo recomendándote usar computadora o tablet para una mejor experiencia con el editor.

---

## 4. Elegir un ejercicio

Tienes dos formas de empezar:

### Opción A: usar el botón "Empezar 🚀"

Te lleva automáticamente al primer ejercicio que no hayas completado. Ideal si estás empezando o quieres continuar donde te quedaste.

### Opción B: elegir de la sidebar

La barra lateral izquierda muestra todos los ejercicios agrupados por nivel:

- 🌱 **Fácil** — los primeros, ideales si nunca programaste.
- 🔥 **Medio** — requieren más lógica.
- 💎 **Difícil** — retos serios que ponen a prueba tu creatividad.

Haz clic en el ejercicio que quieras. Los ejercicios que ya completaste tienen una estrella ⭐ al lado.

---

## 5. La pantalla de ejercicio

Cuando abres un ejercicio ves:

### Arriba: enlace "Volver al inicio"

Si quieres volver a la pantalla de bienvenida, haz clic en el "← Volver al inicio" arriba de todo, o en el logo 🐍 PyLearn del header.

### Card del enunciado

- **Etiqueta de nivel** (🌱 Fácil, 🔥 Medio, o 💎 Difícil) y cuánto XP vale.
- **Título del ejercicio.**
- **Enunciado completo** que te explica qué función tienes que escribir y qué debe hacer.

### Editor de código

Un cuadro oscuro con estilo VSCode donde escribes tu código Python. Ya viene con un "esqueleto" para que empieces:

- El nombre de la función.
- Los parámetros que recibe.
- Un comentario "# Tu código aquí".
- La palabra `pass` (Python la usa como placeholder vacío).

Tienes que **borrar el `pass` y escribir tu solución**.

### Botón "Enviar solución"

Verde grande. Al hacer clic, el sistema evalúa tu código y te muestra el resultado.

---

## 6. Escribir tu solución

### Reglas básicas para no fallar

Python es un lenguaje **muy estricto con los espacios**. Ten en cuenta:

**1. Indentación (los espacios al principio de cada línea):**

- Todo lo que va **dentro** de una función tiene que estar indentado con **4 espacios** al principio.
- No mezcles espacios con Tab. Usa siempre espacios.

Ejemplo correcto:

    def sumar(a, b):
        return a + b

Ejemplo incorrecto (falta indentación):

    def sumar(a, b):
    return a + b

**2. Los dos puntos:**

Después de `def`, `if`, `for`, `while`, `else`, siempre va un `:` al final. Es fácil olvidarse.

**3. Los paréntesis, corchetes y llaves siempre en pares:**

Si abres `(` cierras `)`. Si abres `[` cierras `]`. Si abres `{` cierras `}`.

**4. Los strings van entre comillas:**

Puede ser simples `'hola'` o dobles `"hola"`, pero tienen que empezar y terminar con la misma.

### Atajos útiles del editor

- **Ctrl + Z** — deshacer.
- **Ctrl + Y** o **Ctrl + Shift + Z** — rehacer.
- **Ctrl + F** — buscar en el código.
- **Ctrl + A** — seleccionar todo.
- **Tab** — indenta (agrega 4 espacios).
- **Shift + Tab** — desindenta (quita 4 espacios).

---

## 7. Enviar y ver resultados

Cuando hagas clic en "Enviar solución", el sistema:

1. Toma tu código.
2. Le agrega automáticamente pruebas ocultas (los "tests").
3. Ejecuta todo en un ambiente seguro.
4. Compara los resultados con lo que se esperaba.

Después de 1 o 2 segundos, ves el resultado.

### Si todos los tests pasan (¡bien!)

Aparece una celebración con:

- Un emoji grande 🎉.
- Mensaje verde "¡Perfecto! Pasaste los X tests".
- **XP ganado** en amarillo.
- Detalle de cada test con ✅ verde.

La barra de progreso arriba a la izquierda se llena un poco más. El ejercicio se marca como completado con estrella ⭐ en la sidebar.

### Si algunos tests fallan

Aparece:

- Mensaje "Casi lo tienes" con el score (por ejemplo 2/4).
- Barra de progreso mostrando cuántos pasaste.
- Detalle test por test.
- Los tests que fallaron se ven en rojo con ❌ y te dicen:
  - **Esperado:** lo que tenía que dar tu función.
  - **Obtenido:** lo que dio en realidad.

**No te frustres si fallan**, es totalmente normal. Ajusta tu código y vuelve a enviar. Puedes intentar todas las veces que quieras.

---

## 8. El sistema de puntos (XP y racha)

En la esquina superior derecha ves dos indicadores:

### 🔥 Racha

Cuenta cuántos ejercicios seguidos resolviste sin fallar en el primer intento. Si envías una solución mal, la racha se resetea a 0.

Es un desafío extra para motivarte a pensar bien antes de enviar.

### ⭐ XP (puntos de experiencia)

Cada ejercicio resuelto te da XP:

- **Fácil:** 10 XP
- **Medio:** 20 XP
- **Difícil:** 40 XP

El XP se acumula y **no baja nunca**. Si completas todos los ejercicios, llegas a 350 XP.

### Persistencia

Tanto la racha, el XP como los ejercicios completados **se guardan en tu navegador**. Si cierras la pestaña y vuelves mañana, todo sigue ahí.

**Ojo:** si limpias el historial del navegador o entras desde una computadora distinta, empiezas desde cero. No hay cuenta ni cloud.

---

## 9. Los tres niveles de dificultad

### 🌱 Fácil

Ejercicios de una o dos líneas. Cubren:

- Operaciones matemáticas básicas (par/impar, máximo).
- Manipulación simple de strings (contar vocales, invertir).
- Trabajar con listas (sumar todos los elementos).

Ideales para dar los primeros pasos.

### 🔥 Medio

Requieren pensar un poco más. Cubren:

- Condicionales combinadas (FizzBuzz).
- Bucles con lógica (números primos, palíndromos).
- Diccionarios (contar palabras).
- Ordenamiento con criterio (por longitud).

Ya son "programación de verdad".

### 💎 Difícil

Son retos que combinan varios conceptos:

- Recursión (Fibonacci, aplanar listas anidadas).
- Estructuras de datos (pilas para balancear paréntesis).
- Comparación compleja (anagramas).
- Algoritmos con reglas específicas (números romanos).

Muchos de estos aparecen en entrevistas técnicas reales.

---

## 10. El linter: tu ayudante mientras escribes

Encima del editor, verás un pequeño indicador que dice:

- ✓ **"Sin errores detectados"** (verde) — todo se ve bien.
- ⚠ **"X problemas detectados"** (amarillo) — hay algo raro.

Este es el **linter**: analiza tu código en tiempo real y te avisa de problemas comunes:

- Indentación mixta (mezcla de tabs y espacios).
- Indentación con número raro de espacios (no múltiplo de 4).
- Falta de `:` en líneas de def, if, for, while, else.

Si hay problemas, aparece un cartel amarillo debajo del editor con el detalle. Y el botón "Enviar" cambia a amarillo para llamar tu atención.

**Importante:** el linter no te bloquea. Si estás segura de que tu código está bien, puedes enviar igual. Los avisos son orientativos.

---

## 11. Consejos para no atascarte

### Antes de escribir código

Lee el enunciado **dos veces**. Asegúrate de entender exactamente qué te piden. Muchos errores vienen de responder a una pregunta que no era la que pedían.

### Piensa el caso más simple primero

Si te piden una función que suma números de una lista, piensa primero: "¿cómo sumaría los números `[1, 2, 3]` a mano?". Traduce ese proceso a Python.

### Prueba con lápiz y papel

Si te atascas, agarra papel y anota qué debería hacer tu función paso a paso con un ejemplo concreto. La solución muchas veces aparece cuando lo escribes.

### Los tests fallan pero "parece igual"

Muy común. Revisa:

- **Mayúsculas y minúsculas:** `True` no es lo mismo que `true`.
- **Espacios extra:** un espacio de más en un string cambia todo.
- **Tipos de dato:** el número `3` no es lo mismo que el string `"3"`.
- **Formato de listas:** `[1,2]` es distinto a `[1, 2]` en algunos casos.

### No copies soluciones de internet

Aunque te tiente, buscar la solución en internet arruina el aprendizaje. Es mejor equivocarse muchas veces y entender, que copiar algo que no vas a recordar mañana.

### Usa el modo oscuro de tu navegador

Como el editor es oscuro, va mejor con el modo oscuro del sistema. Menos cansancio visual.

### Descansa entre ejercicios difíciles

Si estás con Fibonacci hace 30 minutos, cambia a algo más fácil o cierra y vuelve mañana. La programación cansa el cerebro y a veces la solución aparece cuando descansas.

---

## 12. Preguntas frecuentes

### ¿Tengo que instalar algo?

No. Todo funciona en el navegador. No necesitas instalar Python ni ningún editor.

### ¿Puedo usar la app sin internet?

No. Necesitas conexión para que el sistema pueda ejecutar y corregir tu código.

### ¿Se guarda mi progreso?

Sí, en el navegador. Si limpias el historial o cambias de navegador, empiezas de cero.

### ¿Puedo usar la app en el celular?

Sí, pero **no es la mejor experiencia**. El editor de código funciona mucho mejor en computadora o tablet. En celular es difícil seleccionar texto, moverte, etc.

### ¿Los ejercicios son míos si los resuelvo?

Sí, el código que escribes es tuyo. Puedes copiarlo a un archivo aparte para tener respaldo.

### ¿Puedo compartir mi progreso con alguien?

Por ahora no directamente, porque se guarda solo en tu navegador. Pero puedes hacer capturas de pantalla.

### La app carga muy lento la primera vez

Es normal si nadie la usó en la última media hora. Como está en un servidor gratuito, se "duerme" por inactividad. La primera visita tarda 30 a 60 segundos en despertarla. Después va rápido.

### ¿Puedo usar librerías externas (como numpy)?

Por ahora no, el motor solo tiene Python estándar. Los ejercicios están pensados para resolverse sin librerías externas.

### ¿Puedo sugerir nuevos ejercicios?

Sí, escribe a la autora a través de GitHub: github.com/andreaholmesy

### El código me da un error extraño que no entiendo

Copia el mensaje de error completo y pégalo en Google. La mayoría de los errores comunes tienen respuestas en Stack Overflow.

### ¿Puedo ver el código de la app?

Sí, es open source. Está todo en: github.com/andreaholmesy/pylearn

---

## Cierre

Recuerda: programar es una habilidad que se construye con práctica. Nadie nace sabiendo. Cada error que te frustra hoy es un aprendizaje para mañana.

**¡Éxitos con Python!** 🐍✨

---

**Autora:** Andrea Reyes  
**Proyecto:** PyLearn  
**Repositorio:** github.com/andreaholmesy/pylearn
