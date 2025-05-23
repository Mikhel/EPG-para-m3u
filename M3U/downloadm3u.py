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
      "https://tinyurl.com/miklist?region=all&service=SamsungTVPlus": "M3U/SAM/samall.m3u",  # Reemplaza con la URL y nombre del archivo
      "https://tinyurl.com/miklist?region=us&service=SamsungTVPlus": "M3U/SAM/samus.m3u",
      "https://tinyurl.com/miklist?region=ca&service=SamsungTVPlus": "M3U/SAM/samca.m3u",
      "https://tinyurl.com/miklist?region=gb&service=SamsungTVPlus": "M3U/SAM/samgb.m3u",
      "https://tinyurl.com/miklist?region=es&service=SamsungTVPlus": "M3U/SAM/sames.m3u",
      "https://tinyurl.com/miklist?region=all&service=PlutoTV": "M3U/PLUTO/all.m3u",
      "https://tinyurl.com/miklist?region=us&service=PlutoTV": "M3U/PLUTO/us.m3u",
      "https://tinyurl.com/miklist?region=ca&service=PlutoTV": "M3U/PLUTO/ca.m3u",
      "https://tinyurl.com/miklist?region=gb&service=PlutoTV": "M3U/PLUTO/gb.m3u",
      "https://tinyurl.com/miklist?region=mx&service=PlutoTV": "M3U/PLUTO/mx.m3u",
      "https://tinyurl.com/miklist?region=es&service=PlutoTV": "M3U/PLUTO/es.m3u",
      "https://tinyurl.com/miklist?region=all&service=Stirr": "M3U/STIR/all.m3u",
      "https://tinyurl.com/miklist?region=all&service=Roku": "M3U/ROK/rokall.m3u",
      "https://tinyurl.com/miklist?region=all&service=Tubi": "M3U/ROK/tubiall.m3u",
      "https://tinyurl.com/miklist?region=mx&service=Plex": "M3U/ROK/plexmx.m3u",
   }
    
    for url, filename in files_to_download.items():
        download_file(url, filename)
      
