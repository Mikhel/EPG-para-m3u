import requests
from github import Github

# Configura tus variables
GITHUB_TOKEN = 'tu_token_de_github'
REPO_NAME = 'tu_usuario/tu_repositorio'
FILE_URL = 'https://ejemplo.com/archivo.txt'
FILE_NAME = 'archivo.txt'

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
