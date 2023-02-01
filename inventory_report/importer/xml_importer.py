from inventory_report.importer.importer import Importer
import xmltodict

# https://acervolima.com/programa-python-para-converter-xml-em-dicionario/
# https://python-guide-pt-br.readthedocs.io/pt_BR/latest/scenarios/xml.html


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path: str):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        with open(path, "r") as file:
            reader = xmltodict.parse(file.read())
            formated = reader["dataset"]["record"]
            return formated
