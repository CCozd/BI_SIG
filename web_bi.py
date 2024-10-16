import streamlit as st
st.set_page_config(menu_items={
    'Get help': None,
    'Report a bug': None,
    'About': None
# Título de la aplicación
st.title('Filtro de Tableros Power BI')

# Opciones de filtro
opcion = st.selectbox(
    'Selecciona un tablero para visualizar:',
    ('Comitee_Arrival', 'SIG_ARRIBO', 'PITAHAYA')
)

# Mostrar el tablero correspondiente según la opción seleccionada
if opcion == 'Comitee_Arrival':
    st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiOWNlODdmMmYtNGM3Ny00ZmM3LWIyNzQtM2JjNDc2NjIzMzZkIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=600)
elif opcion == 'SIG_ARRIBO':
    st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiMTI4MDhmMzAtZjJjYy00YzgzLWFkODAtYjA5MDYxZjllYjEzIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=600)
elif opcion == 'PITAHAYA':
    st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiMDY5YjhlOGYtMzhkMC00ZWZlLTllYmMtNDFhZTg5ODU3NTFmIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=600)
