from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(file_path):
        type = file_path.split(".")[1]
        if type != "json":
            raise ValueError("Arquivo inválido")
        with open(file_path) as file:
            return json.load(file)
