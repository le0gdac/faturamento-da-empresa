import json

with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)

total_faturamento = 0
dias_com_faturamento = 0
menor_faturamento = float('inf')
maior_faturamento = float('-inf')

for item in dados:
    if item['valor'] > 0:
        total_faturamento += item['valor']
        dias_com_faturamento += 1
        if item['valor'] < menor_faturamento:
            menor_faturamento = item['valor']
        if item['valor'] > maior_faturamento:
            maior_faturamento = item['valor']

media_mensal = total_faturamento / dias_com_faturamento

print("Menor valor de faturamento: R$ {:.2f}".format(menor_faturamento))
print("Maior valor de faturamento: R$ {:.2f}".format(maior_faturamento))
print("Número de dias em que o faturamento foi superior à média mensal: {}".format(sum(item['valor'] > media_mensal for item in dados if item['valor'] > 0)))
