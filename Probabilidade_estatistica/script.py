# função que retorna a media
def media(lst: list) -> int:
    mean = sum(lst) / len(lst)
    return round(mean, 2)


# função que retorna a moda
def moda(lst: list) -> int:

    max_value = max([lst.count(x) for x in lst])
    mode = set([x for x in lst if lst.count(x) == max_value])
    if set(lst) == mode:
        return "Não há moda"

    return mode

# função que retorna mediana


def mediana(lst: list) -> int:
    length = len(lst)
    middle = length // 2
    if length % 2 == 0:
        return((lst[middle - 1] + lst[middle]) / 2)

    return lst[middle]


# função do loop
def loop() -> list:
    number_list = []
    while True:
        try:
            number = int(input("Digite um numero inteiro"))
        except:
            print("Por favor, Digite um numero inteiro")
            continue

        if number <= 0:
            break

        number_list.append(number)

    return sorted(number_list)


list_ = loop()


print("media =", media(list_))
print("mediana =", mediana(list_))
print("moda =", moda(list_))
