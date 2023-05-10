from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xml.etree.ElementTree as ET


class Inventory:
    def csv(file_path):
        with open(file_path) as file:
            if file_path.endswith(".csv"):
                return [row for row in csv.DictReader(file)]

    def json(path):
        with open(path) as file:
            return json.load(file)

    def xml(path):
        roots = ET.parse(path).getroot()
        content = []

        for root in roots:
            item = {}

            for sub_root in root:
                item[sub_root.tag] = sub_root.text

            content.append(item)

        return content

    @classmethod
    def import_data(self, file_path, file_type):
        type = file_path.split(".")[1]
        product_list = []

        if type == "csv":
            product_list = self.csv(file_path)
        elif type == "json":
            product_list = self.json(file_path)
        else:
            product_list = self.xml(file_path)

        if file_type == "simples":
            return SimpleReport.generate(product_list)
        elif file_type == "completo":
            return CompleteReport.generate(product_list)
