from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @classmethod
    def import_data(cls, path: str, type_report: str):

        if path.endswith(".csv"):
            list_data = CsvImporter.import_data(path)
        elif path.endswith(".json"):
            list_data = JsonImporter.import_data(path)
        elif path.endswith(".xml"):
            list_data = XmlImporter.import_data(path)
        return cls.read_type(type_report, list_data)

    @classmethod
    def read_type(cls, type_report: str, list_data: list):
        if type_report == "simples":
            return SimpleReport.generate(list_data)
        elif type_report == "completo":
            return CompleteReport.generate(list_data)
