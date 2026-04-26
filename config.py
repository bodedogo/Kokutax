CIDADES = {
    "Tokyo": {"saude": 0.05, "residencial_fixo": 5000},
    "Osaka": {"saude": 0.045, "residencial_fixo": 6000},
    "Kyoto": {"saude": 0.043, "residencial_fixo": 4500},
    "Yokohama": {"saude": 0.045, "residencial_fixo":6000},
    "Nagoya": {"saude": 0.050, "residencial_fixo":7000},
    "Sapporo": {"saude":0.060, "residencial_fixo":8000},
}

VISTOS = {
    "Kosei": {"previdencia": 0.0915, "tipo": "empregado", "seguro_desemprego": True},
    "Autonomo": {"previdencia": 0.05,"tipo": "autonomo", "seguro_desemprego": False},
    "Estudante": {"previdencia":0.02, "tipo": "empregado", "seguro_desemprego": False},
    "Dependente": {"previdencia":0.02,"tipo": "empregado", "seguro_desemprego": True},
    "Residente_Permanente": {"previdencia":0.02,"tipo": "empregado", "seguro_desemprego": True},
}