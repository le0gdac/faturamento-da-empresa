import json

with open("dados.json") as dados_faturamento:
    dados = json.load(dados_faturamento)

menor_valor = (min(dados_faturamento))
print(menor_valor)

