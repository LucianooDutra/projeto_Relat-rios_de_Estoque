from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        10,
        "Geladeira",
        "Brastemp",
        "2023-01-31",
        "2023-02-10",
        "123456789",
        "local com sombra",
    )

    assert str(product) == (
        f"O produto {product.nome_do_produto}"
        f" fabricado em {product.data_de_fabricacao}"
        f" por {product.nome_da_empresa} com validade"
        f" até {product.data_de_validade}"
        f" precisa ser armazenado {product.instrucoes_de_armazenamento}."
    )
