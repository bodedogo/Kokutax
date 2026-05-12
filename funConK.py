from config import CIDADES, VISTOS


def salario_anual(salario_mensal: int):
    return salario_mensal * 12


def deducao_inicial(salario_anual: int):
    if salario_anual <= 1_900_000:
        return 650_000
    elif salario_anual <= 3_600_000:
        return int(salario_anual * 0.30 + 80_000)
    elif salario_anual <= 6_600_600:
        return int(salario_anual * 0.20 + 440_000)
    elif salario_anual <= 8_500_000:
        return int(salario_anual * 0.10 + 1_100_000)
    else:
        return 1_950_000


def deducao_secundaria(salario_anual: int):
    if salario_anual <= 24_000_000:
        return 480_000
    elif salario_anual <= 24_500_000:
        return 320_000
    elif salario_anual <= 25_000_000:
        return 160_000
    else:
        return 0


def salario_depois_deducao(salario_anual: int, deducao_inicial: int, deducao_secundaria: int):
    soma_das_deducoes = deducao_inicial + deducao_secundaria
    return salario_anual - soma_das_deducoes


def previdencia(salario_anual: int, visto: str):
    taxa = VISTOS[visto]["previdencia"]
    return int(salario_anual * taxa)


def saude(salario_anual: int, cidade: str):
    taxa = CIDADES[cidade]["saude"]
    return int(salario_anual * taxa)


def salario_pos_impostos_extras(valor: int, valor_previdencia: int, valor_saude: int):
    soma_dos_impostos = valor_saude + valor_previdencia
    return valor - soma_dos_impostos


def renda_tributavel(salario_pos_impostos_extras: int):
    return max(salario_pos_impostos_extras)


def imposto(renda_tributavel: int, cidade: str, visto: str):
    if renda_tributavel < 1_000:
        imposto_a_pagar = 0
    elif renda_tributavel <= 1_949_000:
        imposto_a_pagar = int(renda_tributavel * 0.05)
    elif renda_tributavel <= 3_299_000:
        imposto_a_pagar = int(renda_tributavel * 0.10 - 97_500)
    elif renda_tributavel <= 6_949_000:
        imposto_a_pagar = int(renda_tributavel * 0.20 - 427_500)
    elif renda_tributavel <= 8_999_000:
        imposto_a_pagar = int(renda_tributavel * 0.23 - 636_000)
    elif renda_tributavel <= 17_999_000:
        imposto_a_pagar = int(renda_tributavel * 0.33 - 1_536_000)
    elif renda_tributavel <= 39_999_000:
        imposto_a_pagar = int(renda_tributavel * 0.40 - 2_796_000)
    else:
        imposto_a_pagar = int(renda_tributavel * 0.45 - 4_796_000)
    return max(imposto_a_pagar, 0)


def imposto_residencial(base: int, cidade: str, visto: str):
    fixo = CIDADES[cidade]["residencial_fixo"]
    return int(base * 0.10 + fixo)


def seguro(salario_anual: int):
    return int(salario_anual * 0.006)