from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path: str):
        if not path.endswith(".json"):
            raise ValueError("Arquivo inválido")
        with open(path, "r") as file:
            reader = json.load(file)
            return reader
