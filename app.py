import streamlit as st
from corrector import cargar_ejercicios, corregir


# Configuración de la página (título en la pestaña del navegador, ícono, etc.)
st.set_page_config(
    page_title="Plataforma de Python",
    page_icon="🐍",
    layout="wide"
)


# Título principal
st.title("🐍 Plataforma de Ejercicios de Python")
st.caption("Practicá Python con corrección automática")


# Cargar los ejercicios del archivo JSON
ejercicios = cargar_ejercicios()


# Barra lateral izquierda: lista de ejercicios
st.sidebar.title("📚 Ejercicios")
st.sidebar.write("Elegí un ejercicio para resolver:")

# Diccionario para el selector: {"1. Función es_par": ejercicio_completo}
opciones = {f"{ej['id']}. {ej['titulo']}": ej for ej in ejercicios}

# Selector en la barra lateral
opcion_elegida = st.sidebar.radio(
    "Ejercicios disponibles",
    list(opciones.keys()),
    label_visibility="collapsed"
)

# El ejercicio que la persona eligió
ejercicio = opciones[opcion_elegida]


# Panel principal dividido en dos columnas
col_izq, col_der = st.columns([1, 1])


# COLUMNA IZQUIERDA: enunciado del ejercicio
with col_izq:
    st.subheader(f"📖 {ejercicio['titulo']}")
    st.write(ejercicio["enunciado"])
    
    with st.expander("Ver casos de prueba (tests públicos)"):
        for i, test in enumerate(ejercicio["tests"], 1):
            st.code(f"{test['entrada']} → {test['esperado']}", language="python")


# COLUMNA DERECHA: editor de código y resultado
with col_der:
    st.subheader("✏️ Tu solución")
    
    # Editor de código. Usa el código_inicial del ejercicio como valor por defecto.
    # La key hace que cada ejercicio recuerde su propio código.
    codigo_estudiante = st.text_area(
        "Escribí tu código aquí:",
        value=ejercicio["codigo_inicial"],
        height=250,
        key=f"codigo_{ejercicio['id']}",
        label_visibility="collapsed"
    )
    
    # Botón de enviar
    if st.button("🚀 Enviar solución", type="primary", use_container_width=True):
        with st.spinner("Ejecutando tus tests..."):
            resultado = corregir(codigo_estudiante, ejercicio)
        
        # Mostrar el resumen general
        pasados = resultado["tests_pasados"]
        totales = resultado["tests_totales"]
        
        if resultado["todo_ok"]:
            st.success(f"🎉 ¡Perfecto! Pasaron los {totales} tests.")
            st.balloons()
        else:
            st.warning(f"⚠️ Pasaron {pasados} de {totales} tests. Seguí intentando.")
        
        # Barra de progreso visual
        st.progress(pasados / totales)
        
        # Detalle test por test
        st.subheader("Detalle de tests")
        for i, det in enumerate(resultado["detalles"], 1):
            if det["paso"]:
                st.success(f"✅ Test {i}: `{det['entrada']}` → esperado `{det['esperado']}`")
            else:
                st.error(
                    f"❌ Test {i}: `{det['entrada']}`\n\n"
                    f"- Esperado: `{det['esperado']}`\n"
                    f"- Obtenido: `{det['obtenido']}`"
                )


# Pie de página
st.sidebar.divider()
st.sidebar.caption("Hecho con ❤️ por Andrea")