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
st.title('COMITEE_ARRIVAL')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiMTk2YjU2NDktYmViZi00N2VhLTgyYzQtZDc2Yzg5NTI1NWU0IiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=600)
st.title('CLAIMS_PROJECT')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiZjFkOGI4ZTUtZjdlMC00MWQ5LTg1NDItMWI0YjgwYjk4ZTg1IiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=600)
st.title('DESTINATION_PROJECT')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiOWNlODdmMmYtNGM3Ny00ZmM3LWIyNzQtM2JjNDc2NjIzMzZkIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=600)
