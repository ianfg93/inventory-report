from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(self, file_path, file_type):
        type = file_path.split(".")[1]
        product_list = []

        if type == "csv":
            product_list = self.CsvImporter(file_path)
        elif type == "json":
            product_list = self.JSONImporter(file_path)
        else:
            product_list = self.XMLImporter(file_path)

        if file_type == "simples":
            return SimpleReport.generate(product_list)
        elif file_type == "completo":
            return CompleteReport.generate(product_list)
