import requests

def download_file(https://i.mjh.nz/PlutoTV/mx.xml, mx.xml):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Archivo descargado y guardado como {filename}")
    else:
        print(f"Error al descargar el archivo: {response.status_code}")

if __name__ == "__main__":
    url = "https://i.mjh.nz/PlutoTV/mx.xml"  # Reemplaza con la URL del archivo
    filename = "mx.xml"  # Cambia la extensión según el tipo de archivo
    download_file(url, filename)
