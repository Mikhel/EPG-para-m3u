import requests
from github import Github

# Configura tus variables
GITHUB_TOKEN = 'GITHUB_TOKEN'
REPO_NAME = 'Mikhel/EPG-para-m3u'
FILE_URL = 'https://i.mjh.nz/PlutoTV/mx.xml.gz'
FILE_NAME = 'mx.xml.gz'

# Descarga el archivo
response = requests.get(FILE_URL)
if response.status_code == 200:
    with open(FILE_NAME, 'wb') as file:
        file.write(response.content)
    print(f"Archivo {FILE_NAME} descargado exitosamente.")
else:
    print(f"Error al descargar el archivo: {response.status_code}")

# Subir el archivo a GitHub
g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)

with open(FILE_NAME, 'rb') as file:
    content = file.read()
    repo.create_file(FILE_NAME, "Añadir archivo desde script", content)
    print(f"Archivo {FILE_NAME} subido exitosamente a {REPO_NAME}.")
