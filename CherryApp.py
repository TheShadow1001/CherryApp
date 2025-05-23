import streamlit as st

st.set_page_config(
    page_title="CherryApp",
    page_icon="https://imgs.search.brave.com/6vTnX1yW4AjzIMsAxRvBb-LWCESSEpoxwHSwvRE-37A/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9pbWdz/LnNlYXJjaC5icmF2/ZS5jb20vS2RBX3dz/WFZNWnBXNFdhcnlm/VW9PTkhybEQwcU9w/S2dfbmQ5b1QzenhZ/dy9yczpmaXQ6NTAw/OjA6MDowL2c6Y2Uv/YUhSMGNITTZMeTl6/ZEdGMC9hV010TURB/dWFXTnZibVIxL1ky/c3VZMjl0TDJGemMy/VjAvY3k0d01DOWph/R1Z5Y25rdC9hV052/YmkweU16QjRNalUy/L0xXcGxhbWxyT1hS/M0xuQnUvWnc.jpeg",
    layout="wide"
)

st.hide_everything = """
    <style>
    {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""

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

st.title("Sobre mí🤔")
st.image("https://imgs.search.brave.com/mIT3cPFH1knQmMFLf4IFRn_z_YpXqJZdlp6xJAiw670/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvNjY5/ODg3MzUwL2VzL2Zv/dG8vZ2VudGUtZGUt/bmVnb2Npb3MtdHJh/YmFqYW5kby1lbi1l/c2NyaXRvcmlvLWRl/LXdpbmRvd3MuanBn/P3M9NjEyeDYxMiZ3/PTAmaz0yMCZjPVZi/a2VtS1JGWUJuY1df/SDd0ZEJIakw2eS1u/aUxuYXd0TzhzTTYt/U2Z5UzA9")
st.text("Soy un creador indie, de juego y de útilidades.")
st.text("Siempre cualquier error con la página la resolveré, pero la página puede presentar muchos de estos")
st.text("Pero cualquier errores puedes escribirme por email:WikiDeveloper1@gmail.com")
st.text("Esta página está en desarrollo, cualquier error critico puedes decirnos!")
st.text("Si quieres ayudar en la página puedes contactarme!")
st.text("Y muchas gracias por visitar mí proyecto!")
st.text("CherryApp es vida, CherryApp es amor")
st.title("")
st.title("")
st.title("Registrarme CherryApp🍒")
st.image("https://dynamic.design.com/preview/logodraft/90dca979-d816-4e92-8cbd-e37b79f63f33/image/large.png")
st.text("No es obligatorio registrarse!")
st.text("Pero si te registras tendrás muchas ventajas en CherryApp🍒")
st.text("¡Como ser el primero en probar las actualizaciones!")

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
        st.sidebar.success(f"{nombre, venta, cédula}: Registrados con éxito!")
    else:
        st.sidebar.warning("¡Es obligatorio poner un registro del cliente!")
        
st.sidebar.title("Productos")
producto = st.sidebar.text_input("Ingresa un producto que quieras vender")
st.text("(Ejemplo:Linterna)")

if st.sidebar.button("Registrar mi producto"):
    if producto:
        st.sidebar.success("Producto registrado en la lista!")
    else:
        st.sidebar.
