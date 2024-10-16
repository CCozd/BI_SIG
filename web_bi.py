import streamlit as st

# Ocultar el menú de GitHub y otras opciones
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# Ocultar el pie de página "Hosted with Streamlit"
hide_footer_style = """
    <style>
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_footer_style, unsafe_allow_html=True)


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
