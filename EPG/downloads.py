import os
import requests

def download_file(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        # Comprobar si el archivo existe
        if os.path.exists(filename):
            # Leer el contenido del archivo existente
            with open(filename, 'rb') as f:
                existing_content = f.read()
            
            # Comparar con el nuevo contenido
            if existing_content == response.content:
                print(f"El archivo '{filename}' ya está actualizado.")
                return  # No hay cambios, así que no hacemos nada
        
        # Guardar el nuevo contenido en el archivo
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Archivo descargado y guardado como {filename}")
    else:
        print(f"Error al descargar el archivo '{filename}': {response.status_code}")

if __name__ == "__main__":
    files_to_download = {
        "https://i.mjh.nz/PlutoTV/mx.xml.gz": "EPG/PLUTO/PLUTOmx.xml.gz",  # Reemplaza con la URL y nombre del archivo
        "https://i.mjh.nz/Stirr/.channels.json": "EPG/epg.json",
        "http://m3u4u.com/epg/d5k2nv4ejds3ed71n984": "EPG/kika.xml.gz",
        "http://m3u4u.com/epg/4z2xnj7kxza24gxmyv15": "EPG/pass.xml.gz",
        "https://tvpass.org/epg.xml": "EPG/pass2.xml",

    }
    
    for url, filename in files_to_download.items():
        download_file(url, filename)
