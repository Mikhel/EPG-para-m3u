import os
import gzip
import xml.etree.ElementTree as ET
import requests

save_as_gz = True  # Set to True to save an additional .gz version

tvg_ids_file = os.path.join(os.path.dirname(__file__), 'plutotvg-ids.txt')
output_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'EPG/plutoepg.xml')
output_file_gz = output_file + '.gz'

def fetch_and_extract_xml(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch {url}")
        return None

    if url.endswith('.gz'):
        try:
            decompressed_data = gzip.decompress(response.content)
            return ET.fromstring(decompressed_data)
        except Exception as e:
            print(f"Failed to decompress and parse XML from {url}: {e}")
            return None
    else:
        try:
            return ET.fromstring(response.content)
        except Exception as e:
            print(f"Failed to parse XML from {url}: {e}")
            return None

def filter_and_build_epg(urls):
    with open(tvg_ids_file, 'r') as file:
        valid_tvg_ids = set(line.strip() for line in file)

    root = ET.Element('tv')

    for url in urls:
        epg_data = fetch_and_extract_xml(url)
        if epg_data is None:
            continue

        for channel in epg_data.findall('channel'):
            tvg_id = channel.get('id')
            if tvg_id in valid_tvg_ids:
                root.append(channel)

        for programme in epg_data.findall('programme'):
            tvg_id = programme.get('channel')
            if tvg_id in valid_tvg_ids:
                root.append(programme)

    tree = ET.ElementTree(root)
    tree.write(output_file, encoding='utf-8', xml_declaration=True)
    print(f"New EPG saved to {output_file}")

    if save_as_gz:
        with gzip.open(output_file_gz, 'wb') as f:
            tree.write(f, encoding='utf-8', xml_declaration=True)
        print(f"New EPG saved to {output_file_gz}")

urls = [
    'https://i.mjh.nz/PlutoTV/us.xml.gz',
    'https://i.mjh.nz/PlutoTV/ca.xml.gz',
    'https://i.mjh.nz/PlutoTV/gb.xml.gz',
    'https://i.mjh.nz/PlutoTV/mx.xml.gz',
    'https://i.mjh.nz/PlutoTV/es.xml.gz',
    'https://i.mjh.nz/SamsungTVPlus/us.xml.gz',
    'https://i.mjh.nz/SamsungTVPlus/gb.xml.gz',
    'https://i.mjh.nz/SamsungTVPlus/ca.xml.gz',
    'https://i.mjh.nz/SamsungTVPlus/es.xml.gz',
    'https://helmerluzo.github.io/RakutenTV_HL/epg/RakutenTV.xml.gz',
    'https://helmerluzo.github.io/RuntimeTV_HL/epg/RuntimeTV.xml.gz',
    'https://helmerluzo.github.io/CanelaTV_HL/epg/CanelaTV.xml.gz',
    'https://i.mjh.nz/Plex/mx.xml.gz',
    ]

if __name__ == "__main__":
    filter_and_build_epg(urls)
