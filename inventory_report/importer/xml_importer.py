from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @staticmethod
    def import_data(file_path):
        type = file_path.split(".")[1]
        if type != "xml":
            raise ValueError("Arquivo inválido")
        roots = ET.parse(file_path).getroot()
        content = []

        for root in roots:
            item = {}

            for sub_root in root:
                item[sub_root.tag] = sub_root.text

            content.append(item)

        return content
