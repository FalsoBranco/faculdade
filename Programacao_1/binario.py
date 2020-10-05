def bin_to_dec(numero: str):
    return int(numero, 2)


def dec_to_bin(numero: int):
    if numero == 0:
        return ''
    else:
        return dec_to_bin(numero // 2) + str(numero % 2)


if __name__ == "__main__":
    print(dec_to_bin(329))
    print(dec_to_bin(284))
    print(bin_to_dec("101001001"))
    print(bin_to_dec("11001101"))
