import streamlit as st

# Título de la aplicación
st.title('Filtro de Tableros Power BI')

# Opciones de filtro
opcion = st.selectbox(
    'Selecciona un tablero para visualizar:',
    ('Tablero 1', 'Tablero 2', 'Tablero 3')
)

# Mostrar el tablero correspondiente según la opción seleccionada
if opcion == 'Tablero 1':
    st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiOWNlODdmMmYtNGM3Ny00ZmM3LWIyNzQtM2JjNDc2NjIzMzZkIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=600)
elif opcion == 'Tablero 2':
    st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiMTI4MDhmMzAtZjJjYy00YzgzLWFkODAtYjA5MDYxZjllYjEzIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=600)
elif opcion == 'Tablero 3':
    st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiMDY5YjhlOGYtMzhkMC00ZWZlLTllYmMtNDFhZTg5ODU3NTFmIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=600)
