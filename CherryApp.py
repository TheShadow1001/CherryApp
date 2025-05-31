import streamlit as st
import webbrowser

st.set_page_config(
    page_title="COINGAMES",
    page_icon="🧿",
    layout="wide",
    initial_sidebar_state="collapsed"
  )

st.title("C O I N  🧿  G A M E S")

hide_everything = """
    <style>
    {visibility: hidden;} 
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_everything, unsafe_allow_html=True)

opcion = st.sidebar.radio("Elige una opcion", ["Juegos", "Celular", "Archivos-Bat", "Apps-Útiles"])

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
        gta3 = st.button("Descargar Grand Theft Auto 3")
    
        if gta3:
            webbrowser.open("https://download1648.mediafire.com/pc4odijgtfegTwl5cFON27kKryMW-fUIzGzSd4FQ0tgNwEa0ZoK5nVOvk9WsHO_Gz__gXptWp_KXZgwGsKRJKmJjqTWxIr20FOx_ItZpFIfInUtMu7CqtX6NpTOSJASUZVxKfaWmHV52LUNE_fKCJUHM4PyhtzoIJhrNzaOMzZXXYw/br2of7ckbp4sh4m/Gta3_Portable_By_TheShadow.rar")
    with col3:
        st.write("Counter Strike 1.6(1.0)")
        st.image("https://imgs.search.brave.com/2F8vIUDyvQ4gH_3bJqMKdOVLB7-qjjZhxA5iPkA_hGQ/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly93YWxs/cGFwZXJhY2Nlc3Mu/Y29tL2Z1bGwvMzUy/MTMwMy5qcGc")
        csgo = st.button("Descargar Counter Strike(Source)")
        
        if csgo:
            webbrowser.open("https://down-cs.su/download/1/direct")
    with col1:
        st.write("SchoolBoy Runaway_v1.0")
        st.image("https://imgs.search.brave.com/GpVMKIuHrCs7WEcP-WfGxBtObNHKY4wd0g7VTu3bDtQ/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YXByb3h5LnR2dHJv/cGVzLm9yZy93aWR0/aC8xMjAwL2h0dHBz/Oi8vc3RhdGljLnR2/dHJvcGVzLm9yZy9w/bXdpa2kvcHViL2lt/YWdlcy9zY2hvb2xi/b3lydW5hd2F5LnBu/Zw")
        school1 = st.button("Descargar SchoolBoy RunAway por Mediafire")
        school2 = st.button("Descargar SchoolBoy RunAway por Gofile(No es directo)")
        
        if school1:
            webbrowser.open("https://download1324.mediafire.com/4fke0tfnunugvZLcUPm5nEIOvSachvwvbzrmEWNkwz9PRAzFZqF7ViMxOkYSS-iEOBUec4EGqeyTPxCZL_caFE0Yv8-rYQY6meVuhSq8pX7o3de2Mhenw_pbssntYPLaBdgCkGJZp-QdmwiWPKmocLdoSb1QKVJjjnjvDTsRtioRMA/5b94f8ixd3j8yf0/SchoolBoy.Runaway+CoinGames.7z")
            
        if school2:
            webbrowser.open("https://gofile.io/d/cTlw04")
            
    with col2:
        st.write("Simpsons Hit And Run")
        st.image("https://imgs.search.brave.com/vdsKIFGbaRNBmdWqPcbEGQYVYfMdCsMQqovqTy6GDbU/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9hcmNo/aXZlLm9yZy9kb3du/bG9hZC90aGUtc2lt/cHNvbnMtaGl0LXJ1/bl8yMDIyMDIvVGhl/X1NpbXBzb25zX0hp/dF9hbmRfUnVuX2Nv/dmVyLnBuZw")
        hit = st.button("Descargar Simpsons Hit And Run")
        
        if hit:
            webbrowser.open("https://download1351.mediafire.com/yorbdkbkndfgbgUM_q0Puu0bKgRnS-QrI83EYFOgP8LqEvUVRyYgdxHVfPxmYpRyZH8PX2wIZmYkxTGq8OhTnK9uIJlMHrcCD5vi4gY2Eyn5AoyQUbQs3btNbQV6qLx0ToliiZQzq_Gtkb5Wcy8114PM5MiYPtSS4MR7LCu8zj3MZw/0z9zevnxr0rgri3/TheSimpsons_Portable_By_TheShadow.rar")
            st.info("'¡¡Gracias por descargar El Juego!!")

if opcion == "Archivos-Bat":
    st.subheader("Optimizadores, Atajos Etc")
    optimizador = st.button("Descargar Optimizador(NORMAL)")
    
    if optimizador:
        webbrowser.open("https://download1501.mediafire.com/vtbskqqc6eagCwP4UENghncfvE4m2ksy6thOerPGCHnE2KkRxfzybXXm1ScTlu6D2CA_4Be5NQgyMVPr6uV5HjOTE72lH7GwGALMO9TBhWWm2jlHfaI6py7ujQ6jwgzkLHzFv35usRYJcWucHa7nOMzSkiPbAKG5Zrrh8HkbvLBIrw/mfqp0juz05amllw/Optimizador_normal.7z")
        
if opcion == "Celular":
    st.title("Programas-Juegos-Archivos")
    st.write("Geometry Dash APK(BETA)")
    st.image("https://imgs.search.brave.com/w9QiRfnv1cLFMLmuVjAkVZw6UUQGlsdb0V8bU0-mcMg/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9pbWFn/ZXMtd2l4bXAtZWQz/MGE4NmI4YzRjYTg4/Nzc3MzU5NGMyLndp/eG1wLmNvbS9mLzQ0/YmM2ZDM0LTQyOTIt/NDk1Ny05YTg0LTFj/OThjNzc0MGQ4NS9k/aGZqNDhuLWJhNGE5/MGE4LTg4OTQtNGU4/Ny05ZTM5LWFmNWFm/NTRhY2MzMS5wbmc_/dG9rZW49ZXlKMGVY/QWlPaUpLVjFRaUxD/SmhiR2NpT2lKSVV6/STFOaUo5LmV5Snpk/V0lpT2lKMWNtNDZZ/WEJ3T2pkbE1HUXhP/RGc1T0RJeU5qUXpO/ek5oTldZd1pEUXhO/V1ZoTUdReU5tVXdJ/aXdpYVhOeklqb2lk/WEp1T21Gd2NEbzNa/VEJrTVRnNE9UZ3lN/alkwTXpjellUVm1N/R1EwTVRWbFlUQmtN/alpsTUNJc0ltOWlh/aUk2VzF0N0luQmhk/R2dpT2lKY0wyWmNM/elEwWW1NMlpETTBM/VFF5T1RJdE5EazFO/eTA1WVRnMExURmpP/VGhqTnpjME1HUTRO/Vnd2WkdobWFqUTRi/aTFpWVRSaE9UQmhP/QzA0T0RrMExUUmxP/RGN0T1dVek9TMWha/alZoWmpVMFlXTmpN/ekV1Y0c1bkluMWRY/U3dpWVhWa0lqcGJJ/blZ5YmpwelpYSjJh/V05sT21acGJHVXVa/RzkzYm14dllXUWlY/WDAudnQwWURwdnF3/RlVYSWVBRzN0bkFx/MkhQVHExVFBablVs/WEZPWTh3djgxbw")
    geometry = st.button("Descargar Geometry Dash")
    
    if geometry:
        webbrowser.open("https://download1085.mediafire.com/jhyaytm72ifgVRXVD4X0dzh2mWrEWL_RyVKmJ1Xa-P8oDLptwzbW1eOfB0XhuQSRvU3bf3oFXU2IAGN4S-g1anKAKLNa5wAfkEKIF3JTfPiAzRyM6TLHZW_IV6tkXUyACVFtwNKamEEW34wS0_eGVpEzRSeqBvx2BNA2kzRwsp7Z1A/7xhqnxjjlmnwu25/GeometryDash_By_%40WikiDev.apk")
        st.info("¡¡Gracias por descargar El Juego!!")

if opcion == "Apps-Útiles":
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("Discord Lite(Combatible con windows 7)")
        st.image("https://lh5.googleusercontent.com/ZggWfvCANuFBWzS8B1Wi80XyjDY98XmwBzRjvw2zT3Eqk0qLO50H68T7KCXSYG-F7QV2kMy2RmrBbKNu5QdU9gOxyTbesBJEMiBrXNBrBMybx8qMxDO7AjdY4dlO36-2BQ=w1280")
        discord = st.button("Descargar Discord Lite")
    
        if discord:
            webbrowser.open("https://download1589.mediafire.com/7kwi9b60zukglViFqn_Q_ngtKpyQXtJ0El8cO6VvvV6qq3zNilAxy1CzocZoddZmxEmijgT8LObjIIY2OPdxK1uIOOxzYUNizfX4EUfBE0JlKKD_Rbl8PAQ-2wbYNhf9q73Nss-0ujKS4YAVGGVCEumBK1e0ePuo_eskvR-HFVR5Xw/u7rcwpnlpc8cgcm/Discord_by_WikiDev.7z")
            st.info("¡¡Gracias por descargar el programa!!")
        
    with col2:
        st.write("Mem reduct")
        st.image("https://lh6.googleusercontent.com/hu2q8PUiWR0a25TiZ7qnRj3qrAHSZWjymP8UN5P7cDGm8GeCvOYeucfB_L2yWwXv4hhKTJ4eLdONTreuZXwbEFY2FAhdNQoT2WNsNjvInDlFY6RfJvt5mwj3TqkpDjSAfA=w1280")
        mem = st.button("Descargar mem reduct")
        
        if mem:
            webbrowser.open("https://download946.mediafire.com/d2vy983bplsgtXaZ2kDDzF_rGE1lLIf7pavsMRZVVVFWir1AckzWD-8D3iRxuPnzlKxjSoV9wwlcMrbQ5YDClRV4u11vVQxmSQoa6DhRb3AWuBcnavg79MHzC_ddFSwad8imFSm1gp1ZBKlPIjbwKUVryWmIFuErWD-WhZNR4XyyYQ/3qdw5503pdzo93p/MemReduct_By_WikiDev.7z")
            st.info("¡¡Gracias por descargar el programa!!")
