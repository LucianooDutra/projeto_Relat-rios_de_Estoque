from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path: str):
        list_product = []
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        with open(path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                list_product.append(row)
            return list_product
