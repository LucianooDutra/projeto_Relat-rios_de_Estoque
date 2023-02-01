from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        10,
        "Geladeira",
        "Brastemp",
        "2023-01-31",
        "2023-02-10",
        "123456789",
        "local com sombra",
    )

    assert product.id == 10
    assert product.nome_da_empresa == "Brastemp"
    assert product.nome_do_produto == "Geladeira"
    assert product.data_de_fabricacao == "2023-01-31"
    assert product.data_de_validade == "2023-02-10"
    assert product.numero_de_serie == "123456789"
    assert product.instrucoes_de_armazenamento == "local com sombra"
