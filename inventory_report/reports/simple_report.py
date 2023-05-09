from datetime import datetime


class SimpleReport:
    @staticmethod
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
        produtos_por_empresa = {}
        for produto in list:
            if produto["nome_da_empresa"] in produtos_por_empresa:
                produtos_por_empresa[produto["nome_da_empresa"]] += 1
            else:
                produtos_por_empresa[produto["nome_da_empresa"]] = 1
        empresa_mais_produtos = max(
            produtos_por_empresa, key=produtos_por_empresa.get)

        return (
            f"Data de fabricação mais antiga: {fabricação_mais_antiga}\n"
            f"Data de validade mais próxima: {validade_mais_próxima}\n"
            f"Empresa com mais produtos: {empresa_mais_produtos}"
        )
