# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, report: list):
        old_date = cls.old_date(report)
        expiration_date = cls.expiration_date(report)
        name_company = cls.biggest_company(report)

        return (
            f"Data de fabricação mais antiga: {old_date}\n"
            f"Data de validade mais próxima: {expiration_date}\n"
            f"Empresa com mais produtos: {name_company}"
        )

    @staticmethod
    def old_date(products: list):
        return min([product["data_de_fabricacao"] for product in products])

    @staticmethod
    def expiration_date(products: list):
        return min(
            [
                product["data_de_validade"]
                for product in products
                if datetime.strptime(product["data_de_validade"], "%Y-%m-%d")
                >= datetime.today()
            ]
        )

    @staticmethod
    def biggest_company(products: list):
        result = dict()
        for product in products:
            if product["nome_da_empresa"] in result:
                result[product["nome_da_empresa"]] += 1
            else:
                result[product["nome_da_empresa"]] = 1

        return max(result, key=result.get)
