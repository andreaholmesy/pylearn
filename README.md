# 🐍 PyLearn

> Plataforma web de ejercicios de Python con corrección automática, inspirada en el diseño de Duolingo.

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi&logoColor=white)
![Tailwind](https://img.shields.io/badge/Tailwind_CSS-3.4-38B2AC?logo=tailwindcss&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## ✨ Características

- **15 ejercicios** en tres niveles de dificultad: 🌱 Fácil, 🔥 Medio, 💎 Difícil.
- **Editor de código profesional** con Monaco Editor (el mismo de VSCode) y resaltado de sintaxis.
- **Corrección automática** con feedback detallado por cada test (esperado vs obtenido).
- **Ejecución segura** con timeout configurable para prevenir bucles infinitos.
- **Gamificación completa:** sistema de XP, racha, y progreso persistente en localStorage.
- **API REST** documentada automáticamente con Swagger UI.
- **Interfaz moderna** estilo Duolingo con Tailwind CSS y animaciones sutiles.

## 🎯 Demo

_Próximamente: link al deploy en vivo_

## 🛠️ Stack técnico

**Backend:**
- Python 3.12
- FastAPI (framework de API)
- Uvicorn (servidor ASGI)
- subprocess + tempfile (ejecución segura de código)

**Frontend:**
- HTML5 + JavaScript vanilla
- Tailwind CSS (vía CDN)
- Monaco Editor (vía CDN)
- Google Fonts (Nunito)

**Sin dependencias de npm** — decisión consciente para minimizar la superficie de ataque de supply chain.

## 🚀 Cómo correrlo localmente

### Requisitos previos

- Python 3.10 o superior
- pip

### Instalación

    git clone https://github.com/andreaholmesy/pylearn.git
    cd pylearn
    pip install fastapi uvicorn[standard]
    uvicorn api:app --reload

### Uso

1. Abrí el navegador en `http://localhost:8000/app` para la interfaz web.
2. También podés explorar la API en `http://localhost:8000/docs` (Swagger UI).

## 📁 Estructura del proyecto

    pylearn/
    ├── motor.py            # Motor de ejecución segura de código Python
    ├── corrector.py        # Sistema de corrección automática con tests
    ├── api.py              # API REST con FastAPI
    ├── ejercicios.json     # Base de datos de ejercicios
    └── static/
        └── index.html      # Interfaz web (HTML + Tailwind + Monaco)

## 🎓 Ejercicios incluidos

### 🌱 Nivel Fácil (10 XP c/u)

1. Función es_par
2. Suma de lista
3. Cadena al revés
4. Contar vocales
5. Máximo de una lista

### 🔥 Nivel Medio (20 XP c/u)

6. FizzBuzz
7. Palíndromo
8. Contador de palabras
9. Números primos hasta N
10. Ordenar por longitud

### 💎 Nivel Difícil (40 XP c/u)

11. Fibonacci
12. Anagramas
13. Aplanar lista
14. Balancear paréntesis
15. Números romanos

## 🔒 Seguridad

- El código de los usuarios se ejecuta en un proceso separado con **timeout de 5 segundos** para prevenir bucles infinitos.
- Los archivos temporales se eliminan siempre después de la ejecución.
- CORS configurado para permitir integración con frontends externos en desarrollo.

**Nota:** Para uso en producción con usuarios no confiables, se recomienda migrar el motor a un sandbox más robusto (Docker efímero, gVisor, o servicios como Judge0).

## 🗺️ Roadmap

- [ ] Deploy en producción con dominio propio
- [ ] Sistema de login de usuarios
- [ ] Base de datos persistente (SQLite → PostgreSQL)
- [ ] Panel de profesor con seguimiento de progreso
- [ ] Editor de ejercicios sin editar JSON manualmente
- [ ] Sistema de pistas después de X intentos fallidos
- [ ] Soporte para más lenguajes (JavaScript, Java)

## 📝 Licencia

MIT — Podés usar este código libremente, modificarlo y distribuirlo.

## 👩‍💻 Autora

**Andrea Reyes**

- GitHub: [@andreaholmesy](https://github.com/andreaholmesy)

---

<p align="center">Hecho con ❤️ y ☕</p>
