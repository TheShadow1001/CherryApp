import streamlit as st

st.title("Bienvenido a CherryApp🍒")
st.subheader("CherryCorporation🍒")
st.image("https://dynamic.design.com/preview/logodraft/010ada47-fa29-4cfe-8c74-58ac48f80d6e/image/large.png")
st.write("Sirve para registrar clientes a una empresa")
st.write("La app está en desarrollo y puede tener errores.")
st.write("La app requiere una subscripción para poder usarla.")
st.write("Pero hay una versión BETA que es esta, así que podrás usarla gratis por ahora.")
st.write("Esta appWeb ayuda a la empresas a registrar los datos de un cliente a una lista.")
st.write("La página web no es recomendable usarla como uso diario en una empresa, porque puede tener errores")
st.write("pero dentro de muy poco tiempo la página ya no tendra errores a menudo.")

st.title("Registrarse")
st.write("Registrarse a CherryApp🍒, no es OBLIGATORIO, pero si quieres ser el primero es obtener las ")
st.write("Actualizaciones de la página es recomendable registrarse, además podrás evitar fúturos pagos.")
st.write("Ya que la página con el tiempo tendrá pagos, y sí creas una cuenta ahora podrás evitarlos a largo plazo.")

nombre = st.text_input("Ingrese su usuario")
correo = st.text_input("Ingrese su correo electrónico")
empresa = st.text_input("Ingrese el nombre de su empresa")

if st.button("Registrarme a CherryApp🍒"):
   if nombre and correo and empresa:
        st.success("¡Gracias por registrarse a CherryApp🍒!")
   else:
        st.info("Ok, gracias por su atención.")

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
st.title("Registrarme CherryApp🍒")
st.image("https://dynamic.design.com/preview/logodraft/90dca979-d816-4e92-8cbd-e37b79f63f33/image/large.png")
st.text("No es obligatorio registrarse!")
st.text("Pero si te registras tendrás muchas ventajas en CherryApp🍒")
st.text("¡Mucha suerte!")

Usuario = st.text_input("Usuario")
Nombre = st.text_input("Nombre de empresa")
cédula = st.text_input("Cédula")

if st.button("Registrarme a CherryApp🍒", key="boton1"):
    if Usuario and Nombre and cédula:
        st.success("Registrado con éxito a CherryApp🍒")
    else:
        st.info("Gracias por su tiempo.")
        
st.sidebar.title("Registros del cliente")
st.sidebar.subheader("Aquí sería el apartado de registro")

nombre = st.sidebar.text_input("Nombre del cliente")
venta = st.sidebar.text_input("Registro de venta")  
cédula = st.sidebar.text_input("Cédula del cliente")

if st.sidebar.button("Crear registro", key="boton2"):
    if nombre and venta and cédula:
        st.sidebar.success("¡Registro creado con éxito!")
    else:
        st.sidebar.warning("¡Es obligatorio poner un registro del cliente!")

st.title("")

st.text("Copyright© 2025 CherryApp.streamlit.app  |  All Rights Reserved  ")
