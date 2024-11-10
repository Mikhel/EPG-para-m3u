import json
import xmltodict

# Cargar el archivo JSON
with open('EPG/epg.json', 'r') as json_file:
    json_data = json.load(json_file)

# Convertir JSON a XML
xml_data = xmltodict.unparse({"epg": json_data}, pretty=True)

# Guardar el archivo XML
with open('epg.xml', 'w') as xml_file:
    xml_file.write(xml_data)

print("Conversión de JSON a XML completada. Archivo guardado como 'epg.xml'.")
