import streamlit as st
import webbrowser

st.set_page_config(
    page_title="CoinGames",
    page_icon="🧿",
    layout="wide",
    initial_sidebar_state="collapsed"
  )

st.image("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjUXlK85A0s4LWZMi9Bw6VjihteEbJW77sj6QjvVyPP14XKsGd8rLXoCSc_lglDEJXlUlVhF5kxPktYls73PEGRqT0E4_wJL82r8-tAQC5qeor6x898OLXcB3vHE60k3ha6c6DYLK_bBCv3jpNSRFpdi_LWrg2gtN19sBkcRpGPoLBbQg7uvNeoTH_dlwY/s600/wmremove-transformed%20(1).png")

hide_everything = """
    <style>
    {visibility: hidden;} 
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_everything, unsafe_allow_html=True)

opcion = st.sidebar.radio("Elige una opcion", ["Juegos", "Archivos-Bat", "Apps-Útiles"])

st.markdown(f"## {opcion}")

if opcion == "Juegos":
    st.title("Juegos-Games")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("Grand Theft Auto San Andreas")
        st.image("https://imgs.search.brave.com/HR9ceY0ONl8kRtx56QiZxOo_GZ-Y3Cit43oRLLTRhPs/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly93YWxs/cGFwZXJhY2Nlc3Mu/Y29tL2Z1bGwvMzEx/NTI2NS5qcGc")
        gtasa = st.button("Descargar Juego", key=1)
        
        if gtasa:
            webbrowser.open("https://download191.uploadhaven.com/1/application/zip/5juqQiHkNt3Vz2Fsa5izUgCaBAd4CkTE7cO47Ux5.zip?key=iFfhqbA79bnrMXWMma0U6w&expire=1748635378&filename=GrandTheftAuto-SanAndreas.zip")
            st.info("Creditos a Steamunlocked.net")
    st.title("")
    with col2:
        st.write("The Walking Dead Seasion One")
        st.image("https://imgs.search.brave.com/fmw99wgND03XM3hP5CQVacirgxq8stnK7_v9o0pXmHc/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9pbWFn/ZS5hcGkucGxheXN0/YXRpb24uY29tL2Nk/bi9VUDIwMjYvQ1VT/QTAxMDE5XzAwL3hG/ckNWN0hTczVxS2h1/SHg4TDBrZ2d5RzY1/WFNIRjhrLnBuZw")
        twd = st.button("Descargar The Walking Dead Seasion One")
        
        if twd:
            webbrowser.open("https://download2299.mediafire.com/bm40ucyjzflgowDX94HvP70INn12vDQ5HmQW7RN6AZC_DZgBKZZVm7TmQ80wK7BJzbGBT87Rz8tWYNQbMukoMkds9igFU8wLWZ_nnEG4WFk35qgh4cdFJk_vfM08-JKaFBM_OgezI87RxubhW5LhQXtZ-BXFrZf8rn2l7GFGkcV5Ow/eiu6t8a8esejsd2/The+Walking+Dead+-+Complete+First+Season.7z")
            st.info("Creditos al Amigo OptiJuegos")
    st.title("")
    with col2:
        st.write("Dead Island The Years Edition")
        st.image("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiIqyfCMS5_oWg2QOOFOvL4Da9s00Hg_lbhmxOpdtmowjOn_9YKojgvoKka9ePNNOZnyZVju0lN2yuneLNKHoEqj8-jVg6FdTV51dzJO6yP0VDkNao3LrivG9FnyXrMtfudvK_xycFKNjutcitBRnx9-MzgDLGg_Tyk7kh5bcuILCsAxKbgRAKpgA6n_uY/w320-h248/DeadIslandLogo.jpg")
        deadisland = st.button("Descargar Juego", key=2)      
        if deadisland:
            webbrowser.open("https://download944.mediafire.com/2duf1k1k0ntgXnH6nXxgieurP--iXaX-17Tt4IeBOW9zzDQUY1SnEbJcq-8vcaJt6YvjSiducrwBFYxc2jR2coaJfAx6MfocHmGBX6hctUOquz2fyyzths6Uc7C6469DUqJ7gU028CYt9evSrJwqpoaRBHtLKVcZpoZisMLVbY4Gvw/87puex12s1f0zy4/DeadIsland_GOTY_By_WikiDev.7z")
            st.info("¡Gracias por decargar el juego!")
    st.title("")
    with col3:
        st.write("Resident Evil 4(Original)")
        st.image("https://imgs.search.brave.com/PaCpLhDQqgB7Q9PPOC2oVXW7c0wGXB7RcjADXqK6HXk/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly93d3cu/cmVzaWRlbnRldmls/LmNvbS9yZTQvYXNz/ZXRzL2ltYWdlcy90/b3BpY3MvYm5yLXZy/bW9kZS1yZS5qcGc")
        re4 = st.button("Descargar Juego-PC", key=3)
    
        if re4:
            webbrowser.open("https://download947.mediafire.com/vl1iw7w6l5wgQEvYW5ElTx5kLqQWMItheF4upfdhSu5tSOQbMxWmpLt1ccLlkaUpwf_d2J48mB2r5rBgqd3J4luSKiM8pgjcdC08yqW23EN8SVawoBe0ImZfNQyOCJyDHUDNz1b4n-QAJgJ-S7Ln6_cNF-XV3yw8ffN_0bE7QJ5d2g/zr5mi4asudrny57/Resident_Evil_Lite_By_WikiDev.7z")
      
    with col1:
        st.write("Grand Theft Auto 3")
        st.image("https://imgs.search.brave.com/1O50-6gOkWcsTwXH3rKRo7ZJvsiiC9cTWuRBiTCKt64/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly93YWxs/cGFwZXJjYXZlLmNv/bS93cC93cDk4MzE5/MjMuanBn")
        gta3 = st.button("Descagargar Grand Theft Auto 3")
    
        if gta3:
            webbrowser.open("https://download1648.mediafire.com/pc4odijgtfegTwl5cFON27kKryMW-fUIzGzSd4FQ0tgNwEa0ZoK5nVOvk9WsHO_Gz__gXptWp_KXZgwGsKRJKmJjqTWxIr20FOx_ItZpFIfInUtMu7CqtX6NpTOSJASUZVxKfaWmHV52LUNE_fKCJUHM4PyhtzoIJhrNzaOMzZXXYw/br2of7ckbp4sh4m/Gta3_Portable_By_TheShadow.rar")
