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
    st.components.v1.iframe("https://app.fabric.microsoft.com/view?r=eyJrIjoiOWMxZWIyZmUtYTI5NS00MjJjLWI0N2UtMzZlOWIyMjZkMjc5IiwidCI6Ijk2NGJhZWMxLWQyM2ItNGQyZC1iZmE5LTEzNDQwNTRlYTY1NCIsImMiOjR9", height=600)
elif opcion == 'Tablero 2':
    st.components.v1.iframe("https://app.fabric.microsoft.com/view?r=eyJrIjoiZDY0YWEwNGUtYzgxYS00YTg5LWI1MWUtMzRmMDQzODVmYjI1IiwidCI6Ijk2NGJhZWMxLWQyM2ItNGQyZC1iZmE5LTEzNDQwNTRlYTY1NCIsImMiOjR9", height=600)
elif opcion == 'Tablero 3':
    st.components.v1.iframe("https://app.fabric.microsoft.com/view?r=eyJrIjoiZDY0YWEwNGUtYzgxYS00YTg5LWI1MWUtMzRmMDQzODVmYjI1IiwidCI6Ijk2NGJhZWMxLWQyM2ItNGQyZC1iZmE5LTEzNDQwNTRlYTY1NCIsImMiOjR9", height=600)
