def bin_to_dec(numero: str):

    soma = []
    for k, i in enumerate(numero[::-1]):
        if i == "0":
            continue

        soma.append(2**k)

    return sum(soma)


def dec_to_bin(numero: int):
    if numero == 0:
        return ''
    else:
        return dec_to_bin(numero // 2) + str(numero % 2)


if __name__ == "__main__":
    print(dec_to_bin(329))
    print(dec_to_bin(284))
    print(bin_to_dec("11011101"))
    print(bin_to_dec("11001101"))
