from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.importer.csv_importer import CsvImporter


def test_decorar_relatorio():
    data = "inventory_report/data/inventory.csv"

    simple_report = ColoredReport(SimpleReport)
    data_csv = CsvImporter.import_data(data)

    result = simple_report.generate(data_csv)

    assert (
        result == "\033[32mData de fabricação mais antiga:\033[0m"
        " \033[36m2020-09-06\033[0m\n"
        "\033[32mData de validade mais próxima:\033[0m"
        " \033[36m2023-09-17\033[0m\n"
        "\033[32mEmpresa com mais produtos:\033[0m"
        " \033[31mTarget Corporation\033[0m"
    )
