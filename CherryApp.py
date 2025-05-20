import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<h1>Bienvenido a CherryApp</h1>", unsafe_allow_html=True)
    
with col2:
    st.text("CherryApp,")
    st.image("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjRjbWumUSdjVdz0uRQNh8a48d7Dt203j8mK1fxhtLhJdZfyxxAtzYvpF9rzTom81e4zDa08y8LGf39A6O8YMAYJTwm0qVODsoa_oY2sagdVNXLzTHC1M5FdMd6AbwSAUGTxb8rTOBXnl33BEG7k9XfaLqHfU7NiCbVHIBaKQjdn1egMQ0t-RBu7LcyzYc/s600/AppCherry2.png")
    st.text("Sirve para registrar clientes a una empresa")
    st.text("La app está en desarrollo y puede tener errores.")
    st.text("La app requiere una subscripción para poder usarla.")
    st.text("Pero hay una versión BETA que es esta, asíq ue podrás usarla gratis por ahora.")

st.title("Descripción")
st.text("Descripción del cliente es cuando un cliente")
st.text("Hace una compra o una venta, y quieres tener lugar dónde guardar los registros.")

st.info("Escriba registro del cliente.")
cliente = st.text_input("")

registro = st.button("CrearRegistro")

if registro:
    st.success(cliente)
    st.info("Resgitro exitoso!")

