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


st.title('COMITEE_ARRIVAL')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiYTA4YWU4MWQtYWJmMS00ZDMyLWJhOTMtMTVjZDY2ODU5YWUxIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=400)
st.title('CLAIMS_PROJECT')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiYTliMWY1ZjctNDI1Yy00YWU1LTkxYjktZTdlMDYwMTYxODY5IiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=400)
st.title('UMBRALES ARRIBOS')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiNTQ0Y2I4MDItZmE4ZS00YjdhLWFkOTMtM2YzYWU4MWI2N2NjIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=400)
st.title('BUDGET')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiYTI0NDc5NmYtZWQzNy00MWFjLWJhZjItY2M1ZTIzM2MyYzhlIiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=400)
st.title('ORIGEN_CHAO')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiODg2MzljYmYtMmYxMC00NTQ1LThmMTYtZWNhNDIyYWMzMmE1IiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=400)
st.title('ORIGEN_PIURA')
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiZmY4NDlkM2YtYmMxZS00Njk4LTlkYTQtYTMxYTZjZGE0Nzk2IiwidCI6ImM4ODRjYzQyLTViMjEtNDA3Mi04YjdhLWE2M2QwYTZmNWQ3OSIsImMiOjR9", height=400)
