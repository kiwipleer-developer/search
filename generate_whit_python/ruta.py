import json
def read_index_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        print("Archivo index.json cargado correctamente.")
        return data
    except Exception as e:
        print(f"Error al cargar el archivo index.json: {e}")
        return None

def modify_and_save_json(data, file_path, href_prefix):
    modified_data = []
    for item in data:
        modified_item = item.copy()
        modified_item["href"] = f"{href_prefix}{item['href'].split('/')[-1]}"
        modified_data.append(modified_item)

    try:
        with open(file_path, 'w') as file:
            json.dump(modified_data, file, indent=2)
        print(f"Archivo {file_path} generado y guardado correctamente.")
    except Exception as e:
        print(f"Error al generar o guardar el archivo {file_path}: {e}")

# Ruta del archivo "index.json"
source_file_path = r'F:\work\search\index.json'

# Leer el archivo "index.json"
data = read_index_json(source_file_path)

if data is not None:
    # Generar y guardar "index_root.json"
    index_0_file_path = r'F:\work\search\index_root.json'
    modify_and_save_json(data, index_0_file_path, "./assets/index/search/")

    # Generar y guardar "index_0.json"
    index_0_file_path = r'F:\work\search\index_0.json'
    modify_and_save_json(data, index_0_file_path, "./search/")

    # Generar y guardar "index_1.json"
    index_1_file_path = r'F:\work\search\index_1.json'
    modify_and_save_json(data, index_1_file_path, "./../assets/index/search/")

    # Repetir el patrón hasta llegar al 10
    for i in range(2, 11):
        file_path = fr'F:\work\search\index_{i}.json'
        href_prefix = "./" + "../" * i + "assets/index/search/"
        modify_and_save_json(data, file_path, href_prefix)

    print("Archivos generados y guardados correctamente.")