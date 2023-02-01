from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, report: list):
        simple_report = super().generate(report)

        quantity_company = dict()
        for company in report:
            if company["nome_da_empresa"] in quantity_company:
                quantity_company[company["nome_da_empresa"]] += 1
            else:
                quantity_company[company["nome_da_empresa"]] = 1

        phrase = "Produtos estocados por empresa:\n"
        for company in quantity_company:
            phrase += f"- {company}: {quantity_company[company]}\n"

        return f"{simple_report}\n" f"{phrase}"
