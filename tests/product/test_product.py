from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        id=1,
        nome_do_produto="Heineken",
        nome_da_empresa="Zé Birita",
        data_de_fabricacao="08/05/2023",
        data_de_validade="08/05/2024",
        numero_de_serie="abc123",
        instrucoes_de_armazenamento="Frezzer",
    )

    assert product.id == 1
    assert product.nome_do_produto == "Heineken"
    assert product.nome_da_empresa == "Zé Birita"
    assert product.data_de_fabricacao == "08/05/2023"
    assert product.data_de_validade == "08/05/2024"
    assert product.numero_de_serie == "abc123"
    assert product.instrucoes_de_armazenamento == "Frezzer"
