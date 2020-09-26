"""
Criar um algoritmo capaz de calcular o faturamento de uma lista de produtos com suas respectivas quantidades e preço.

Verifique a entrada dos produtos, ao digitar sair a captação se encerra.

Calcular o faturamento com a equação:
    faturamento = faturamento + (quantidade * preço)

Utilize uma estrutura for para percorrer toda a lista e pegar as variáveis
quantidade e preço
"""

from random import randint
import os

# Remove os, random


def faturamento_total(produtos: list) -> int:
    faturamento = 0
    for produto in produtos:
        total = produto[0] * produto[1]
        faturamento += total

    return round(faturamento, 2)


def faturamento(produtos: list):
    for produto in produtos:
        yield produto[0], produto[1]


lista_produtos = []

while True:
    nome_item = input("Nome do Produto ou sair: ")
    if nome_item.lower() == "sair":
        break

    valor = float(input(f"Valor do(a) {nome_item}: "))
    quantidade = int(input(f"quantidade do(a) {nome_item} "))
    info = (quantidade, valor)
    lista_produtos.append(info)


os.system('cls' if os.name == 'nt' else 'clear')

for v in faturamento(lista_produtos):
    produto_Id = randint(10000, 999999)
    print(f"produto_ID: {produto_Id}, valor: {v[1]}, quantidade: {v[0]}, total:{v[0] * v[1]:.2f}")

faturamento_total = faturamento_total(lista_produtos)
print(f"O faturamento total foi de R${faturamento_total}")
