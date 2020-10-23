

class Separatriz:
    formula_da_separatriz = 0

    def classe_separatriz(self, tabela: dict, cortes, partes) -> int:
        soma_fi = sum([x["fi"] for x in tabela.values()])
        Separatriz.formula_da_separatriz = (cortes * (soma_fi)) / partes
        for i in tabela:
            if tabela[i]["Fi"] > Separatriz.formula_da_separatriz:
                return i

    def mediana(self, tabela):
        cortes = 1
        partes = 2
        classe_da_separatriz = self.classe_separatriz(tabela, cortes, partes)

        l = tabela[classe_da_separatriz]["intervalos"][0]
        F = tabela[classe_da_separatriz - 1]["Fi"]
        amplitude = tabela[classe_da_separatriz]["intervalos"]
        h = amplitude[1] - amplitude[0]
        f = tabela[classe_da_separatriz]["fi"]
        Md = l + ((Separatriz.formula_da_separatriz - F) * h) / f

        return round(Md, 2)

    def quartil(self, tabela, cortes=...,):
        if cortes > 3:
            raise IndexError("valor do corte maior que 3")

        partes = 4
        classe_da_separatriz = self.classe_separatriz(tabela, cortes, partes)

        l = tabela[classe_da_separatriz]["intervalos"][0]
        F = tabela[classe_da_separatriz - 1]["Fi"]
        amplitude = tabela[classe_da_separatriz]["intervalos"]
        h = amplitude[1] - amplitude[0]
        f = tabela[classe_da_separatriz]["fi"]
        Md = l + ((Separatriz.formula_da_separatriz - F) * h) / f
        return round(Md, 2)

    def decil(self, tabela, cortes=...):
        partes = 10
        if cortes > 9:
            raise IndexError("valor do corte maior que 9")

        partes = 10
        classe_da_separatriz = self.classe_separatriz(tabela, cortes, partes)

        l = tabela[classe_da_separatriz]["intervalos"][0]
        F = tabela[classe_da_separatriz - 1]["Fi"]
        amplitude = tabela[classe_da_separatriz]["intervalos"]
        h = amplitude[1] - amplitude[0]
        f = tabela[classe_da_separatriz]["fi"]
        Md = l + ((Separatriz.formula_da_separatriz - F) * h) / f
        return round(Md, 2)

    def percentil(self, tabela, cortes=...):
        partes = 100
        if cortes > 99:
            raise IndexError("valor do corte maior que 99")

        classe_da_separatriz = self.classe_separatriz(tabela, cortes, partes)

        l = tabela[classe_da_separatriz]["intervalos"][0]
        F = tabela[classe_da_separatriz - 1]["Fi"]
        amplitude = tabela[classe_da_separatriz]["intervalos"]
        h = amplitude[1] - amplitude[0]
        f = tabela[classe_da_separatriz]["fi"]
        Md = l + ((Separatriz.formula_da_separatriz - F) * h) / f
        return Md


tabela = {
    1: {"intervalos": (0, 6), "fi": 10, "Fi": 10},
    2: {"intervalos": (6, 12), "fi": 15, "Fi": 25},
    3: {"intervalos": (12, 18), "fi": 8, "Fi": 33},
    4: {"intervalos": (18, 24), "fi": 7, "Fi": 40},
    5: {"intervalos": (24, 30), "fi": 5, "Fi": 45},
    6: {"intervalos": (30, 36), "fi": 4, "Fi": 49},
    7: {"intervalos": (36, 42), "fi": 1, "Fi": 50},
}

if __name__ == "__main__":

    sep = Separatriz()
    print(sep.mediana(tabela))
    print(sep.quartil(tabela, 1))
    print(sep.quartil(tabela, 3))
    print(sep.decil(tabela, 2))
    print(sep.decil(tabela, 7))
    print(sep.percentil(tabela, 35))
    print(sep.percentil(tabela, 99))
