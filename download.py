import os
import requests

def download_file(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        # Comprobar si el archivo ya existe
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
        print(f"Error al descargar el archivo: {response.status_code}")

if __name__ == "__main__":
    url = "https://i.mjh.nz/PlutoTV/ca.xml"  # Reemplaza con la URL del archivo
    filename = "ca.xml"  # Cambia la extensión según el tipo de archivo
    download_file(url, filename)
