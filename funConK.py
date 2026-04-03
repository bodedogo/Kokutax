from config import CIDADES, VISTOS


def sa(sm: int):
    return sm * 12


def eid(sm: int):
    vsa = sa(sm)
    if vsa <= 1_900_000:
        return 650_000
    elif vsa <= 3_600_000:
        return int(vsa * 0.30 + 80_000)
    elif vsa <= 6_600_600:
        return int(vsa * 0.20 + 440_000)
    elif vsa <= 8_500_000:
        return int(vsa * 0.10 + 1_100_000)
    else:
        return 1_950_000



def prev(sm: int, visto: str):
    vsa = sa(sm)
    taxa = VISTOS[visto]["previdencia"]
    return int(vsa * taxa)



def saude(sm: int, cidade: str):
    vsa = sa(sm)
    taxa = CIDADES[cidade]["saude"]
    return int(vsa * taxa)


def bd(sm: int):
    vsa = sa(sm)

    if vsa <= 24_000_000:
        return 480_000
    elif vsa <= 24_500_000:
        return 320_000
    elif vsa <= 25_000_000:
        return 160_000
    else:
        return 0



def rt(sm: int, cidade: str, visto: str):
    vsa = sa(sm)
    valor = vsa - eid(sm) - prev(sm, visto) - saude(sm, cidade) - bd(sm)
    return max(valor, 0)



def imp(sm: int, cidade: str, visto: str):
    rtb = rt(sm, cidade, visto)

    if rtb < 1_000:
        imposto = 0
    elif rtb <= 1_949_000:
        imposto = int(rtb * 0.05)
    elif rtb <= 3_299_000:
        imposto = int(rtb * 0.10 - 97_500)
    elif rtb <= 6_949_000:
        imposto = int(rtb * 0.20 - 427_500)
    elif rtb <= 8_999_000:
        imposto = int(rtb * 0.23 - 636_000)
    elif rtb <= 17_999_000:
        imposto = int(rtb * 0.33 - 1_536_000)
    elif rtb <= 39_999_000:
        imposto = int(rtb * 0.40 - 2_796_000)
    else:
        imposto = int(rtb * 0.45 - 4_796_000)

    return max(imposto, 0)

def resimp(sm: int, cidade: str, visto: str):
    base = rt(sm, cidade, visto)
    fixo = CIDADES[cidade]["residencial_fixo"]
    return int(base * 0.10 + fixo)


def seg(sm: int):
    vsa = sa(sm)
    return int(vsa * 0.006)