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
        "http://m3u4u.com/m3u/26p5n3d9p6hxrqj5yv7j": "EPG/PLUTO/PUTOSAMS.m3u",
        "https://i.mjh.nz/PlutoTV/us.xml.gz": "EPG/PLUTO/PLUTOus.xml.gz",
        "https://i.mjh.nz/PlutoTV/ca.xml.gz": "EPG/PLUTO/PLUTOca.xml.gz",
        "https://i.mjh.nz/SamsungTVPlus/us.xml.gz": "EPG/PLUTO/SAMSus.xml.gz",  # Otro archivo,
        "https://i.mjh.nz/SamsungTVPlus/ca.xml.gz": "EPG/PLUTO/SAMSca.xml.gz",  # Y otro más
        "https://i.mjh.nz/Plex/mx.xml.gz": "EPG/PLUTO/PLEXmx.xml.gz",
        "https://i.mjh.nz/PlutoTV/.channels.json": "EPG/PLUTO/stirr.json",
    }
    
    for url, filename in files_to_download.items():
        download_file(url, filename)
