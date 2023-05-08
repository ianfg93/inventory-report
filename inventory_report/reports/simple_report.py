from datetime import datetime


class SimpleReport:
    def generate(list):
        fabricação_mais_antiga = min([
            produto["data_de_fabricacao"] for produto in list
            ])
        validade_mais_próxima = min([
            produto["data_de_validade"]
            for produto in list
            if produto["data_de_validade"]
            > datetime.today().strftime("%Y-%m-%d")
        ])
        empresa = {}
        for produto in list:
            if produto["nome_da_empresa"] in empresa:
                empresa[produto["nome_da_empresa"]] += 1
            else:
                empresa[produto["nome_da_empresa"]] = 0
        mais_produtos = max(empresa, key=empresa.get)

        return (
            f"Data de fabricação mais antiga: {fabricação_mais_antiga}\n"
            f"Data de validade mais próxima: {validade_mais_próxima}\n"
            f"Empresa com mais produtos: {mais_produtos}"
        )
