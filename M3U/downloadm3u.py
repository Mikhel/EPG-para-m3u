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
      "https://tinyurl.com/multiservice21?region=all&service=SamsungTVPlus": "M3U/SAM/samall",  # Reemplaza con la URL y nombre del archivo
      "https://tinyurl.com/multiservice21?region=us&service=SamsungTVPlus": "M3U/SAM/samus",
      "https://tinyurl.com/multiservice21?region=ca&service=SamsungTVPlus": "M3U/SAM/samca",
      "https://tinyurl.com/multiservice21?region=gb&service=SamsungTVPlus": "M3U/SAM/samgb",
      "https://tinyurl.com/multiservice21?region=es&service=SamsungTVPlus": "M3U/SAM/sames",
      "https://tinyurl.com/multiservice21?region=all&service=PlutoTV": "M3U/PLUTO/all",
      "https://tinyurl.com/multiservice21?region=us&service=PlutoTV": "M3U/PLUTO/us",
      "https://tinyurl.com/multiservice21?region=ca&service=PlutoTV": "M3U/PLUTO/ca",
      "https://tinyurl.com/multiservice21?region=gb&service=PlutoTV": "M3U/PLUTO/gb",
      "https://tinyurl.com/multiservice21?region=mx&service=PlutoTV": "M3U/PLUTO/mx",
      "https://tinyurl.com/multiservice21?region=es&service=PlutoTV": "M3U/PLUTO/es",
     
    }
    
    for url, filename in files_to_download.items():
        download_file(url, filename)
