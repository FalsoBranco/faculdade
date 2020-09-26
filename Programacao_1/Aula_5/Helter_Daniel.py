"""
Exercício 6, valor 2 ponto:
Construa um algoritmo de votação para a Prefeitura Municipal de Volta
Redonda. Os votos serão computados da seguinte maneira:

"""


def vencedor():
    """ Retorna uma string com o canditado vencedor ou canditados, caso haja empate """

    _ = ["Branco", "Nulo"]  # Remove os valore (Branco, Nulo)
    listaVotos = [i for k, i in canditados.items() if k not in _]
    votoVencedor = max(listaVotos)
    candidatoVencedor = [k for k, i in canditados.items() if i == votoVencedor and k not in _]  # Comprara os valores de casa candidato com o maior voto
    porcentagem = (votoVencedor / sum(canditados.values()))*100

    if len(candidatoVencedor) > 1:
        return f"Ouve um empade entre: {candidatoVencedor} com {votoVencedor} voto(s)"

    return f"O candidato vencedor foi {candidatoVencedor} com {votoVencedor} votos ({porcentagem} % dos votos) "


def votosBrancos():
    return f"O total de votos em branco foram: {canditados['Branco']}"


def votosNulos():
    return f"O total de votos Nulos foram: {canditados['Nulo']}"


def totalEleitores():
    totalVotos = sum(canditados.values())
    return f"O total de votos foram: {totalVotos}"


def resultados():
    print('=-'*30)
    print(vencedor())
    print(votosBrancos())
    print(votosNulos())
    print(totalEleitores())
    print('=-'*30)


canditados = {"Branco": 0,
              "Samuca": 0,
              "Neto": 0,
              "Baltazar": 0,
              "Nulo": 0, }

print("""0 - branco
1 - Samuca
2 - Neto
3 - Baltazar
>= 4 - Nulo""")
while True:
    ID = int(input("ID do Candidato: "))

    if ID < 0:
        break
    if ID >= 4:
        canditados["Nulo"] += 1
        continue

    idCandidato = list(canditados)[ID]
    canditados[idCandidato] += 1

resultados()
