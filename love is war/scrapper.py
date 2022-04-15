# Importar bibliotecas
import requests
import os

capitulo = 0
pagina = 0
for i in range(3000):
    if i >= 1:
        try:
            pagina = pagina + 1
            url = f"https://cdn.statically.io/img/imgs.muitomanga.com/f=auto/imgs/ijiranaide-nagatoro-san/{capitulo}/{pagina}.jpg"
            page = requests.get(url)
            if page.status_code == 200:
                if os.path.exists(f"nagatoro chap {capitulo}") == False:
                    os.mkdir(f"nagatoro chap {capitulo}")
                open(f"nagatoro chap {capitulo}\{pagina} nagatoro.png", "wb").write(page.content)
            elif page.status_code == 404:
                capitulo = capitulo + 1
                pagina = 0
            print(f"{page.status_code} para página {pagina} e  capitulo {capitulo} {url}")
        except Exception as ex:
            print(ex.args)
            break