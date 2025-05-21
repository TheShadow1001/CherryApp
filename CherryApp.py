import streamlit as st

col1, col2, col3 = st.columns(3)

st.title("Bienvenido a CherryApp🍒")
st.text("CherryCorporation🍒")
st.image("https://dynamic.design.com/preview/logodraft/010ada47-fa29-4cfe-8c74-58ac48f80d6e/image/large.png")
st.text("Sirve para registrar clientes a una empresa")
st.text("La app está en desarrollo y puede tener errores.")
st.text("La app requiere una subscripción para poder usarla.")
st.text("Pero hay una versión BETA que es esta, asíq ue podrás usarla gratis por ahora.")

st.title("Descripción")
st.text("Descripción del cliente es cuando un cliente")
st.text("Hace una compra o una venta, y quieres tener lugar dónde guardar los registros.")

st.info("Escriba registro del cliente.")
cliente = st.text_input("")

registro = st.button("Crear Registro")

if registro:
    st.success(cliente)
    st.info("Resgitro exitoso!")

st.title("Sobre nosotros🤔")
st.image("https://imgs.search.brave.com/mIT3cPFH1knQmMFLf4IFRn_z_YpXqJZdlp6xJAiw670/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvNjY5/ODg3MzUwL2VzL2Zv/dG8vZ2VudGUtZGUt/bmVnb2Npb3MtdHJh/YmFqYW5kby1lbi1l/c2NyaXRvcmlvLWRl/LXdpbmRvd3MuanBn/P3M9NjEyeDYxMiZ3/PTAmaz0yMCZjPVZi/a2VtS1JGWUJuY1df/SDd0ZEJIakw2eS1u/aUxuYXd0TzhzTTYt/U2Z5UzA9")
st.text("Nosotros somos una corporación que se encarga de la producción de cosas que sean útiles para empresas")
st.text("Siempre cualquier error con la página la resolverémos, pero la página puede presentar muchos de estos.")
st.text("Pero cualquier errores puedes escribirnos por email:WikiDeveloper1@gmail.com")
st.text("Esta página está en desarrollo, cualquier error critico puedes decirnos!")
st.text("Si quieres ayudar en la página puedes contactarnos!")
st.text("Y muchas gracias por visitar nuestro proyecto!")
st.text("CherryCorporation es vida, CherryCorporation es amor.")
st.title("")
st.title("")
st.title("Registrarse")
st.image("https://dynamic.design.com/preview/logodraft/010ada47-fa29-4cfe-8c74-58ac48f80d6e/image/large.png")
st.text("No es obligatorio registrarse!")
st.text("Pero si te registrar tendras muchas ventajas en CherryApp🍒")
st.text("¡Mucha suerte!")

entrada1 = st.text_input("Ingrese Su Nombre De Usuario")

entrada2 = st.text_input("Ingrese Su Correo Eléctronico")

registrarse = st.button("Registrarme a CherryApp🍒")

if registrarse:
    st.success("Gracias por registrarse a CherryApp!🍒")
