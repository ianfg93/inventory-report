import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(file_path):
        type = file_path.split(".")[1]
        if type != "csv":
            raise ValueError("Arquivo inválido")
        with open(file_path, newline="") as file:
            return [row for row in csv.DictReader(file)]
