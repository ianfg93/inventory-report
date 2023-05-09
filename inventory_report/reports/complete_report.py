from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(list):
        relatorio_completo = SimpleReport.generate(list)
        relatorio_completo += "\nProdutos estocados por empresa:\n"

        produtos_por_empresa = {}
        for produto in list:
            if produto["nome_da_empresa"] in produtos_por_empresa:
                produtos_por_empresa[produto["nome_da_empresa"]] += 1
            else:
                produtos_por_empresa[produto["nome_da_empresa"]] = 1

        for empresa, qtd_produto in produtos_por_empresa.items():
            relatorio_completo += f"- {empresa}: {qtd_produto}\n"

        return relatorio_completo
