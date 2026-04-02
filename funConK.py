def sa(sm: int):
    sa = sm*12  #sm = salario mensal
    return sa   #sa = salario anual

def eid(sm: int): #eid = employment income deduction dedução salarial
    vsa = sa(sm)
    if vsa <= 1_900_000:
        ds = 650_000
    elif vsa <= 3_600_000:
        ds = int(vsa*0.30 + 80_000)
    elif vsa <= 6_600_600:
        ds = int(vsa*0.20 + 440_000)
    elif vsa <= 8_500_000:
        ds = int(vsa*0.10 + 1_100_000)
    else:
        ds = 1_950_000
    #vsa = valor do salario anual
    #ds = quantidade deducionada do salario
    return ds

def prev(sm: int): #prev = previdencia
    vsa = sa(sm)
    prev = int(vsa*0.0915)
    return prev

def saude(sm: int): #saude = plano de saude
    vsa = sa(sm)
    saude = int(vsa*0.045)
    return saude

def bd(sm: int): #basic deduction = dedução basica 2 dedução
   vsa = sa(sm)

   if vsa <= 24_000_000:
       bd = 480_000
   elif vsa <= 24_500_000:
       bd = 320_000
   elif vsa <= 25_000_000:
       bd = 160_000
   else:
       bd = 0
   return bd

def rt(sm: int):#renda tributavel
    vsa = sa(sm)
    rt = vsa - eid(sm) - prev(sm) - saude(sm) - bd(sm)
    if rt< 0:
        rt = 0
    return rt

def imp(sm: int):#imposto de renda nacional
    rtb = rt(sm)

    if rtb < 1_000:
        imposto = 0
    elif rtb <= 1_949_000:
        imposto = int(rtb*0.05)
    elif rtb <= 3_299_000:
        imposto = int(rtb*0.10 - 97_500)
    elif rtb <= 6_949_000:
        imposto = int(rtb*0.20 - 427_500)
    elif rtb <= 8_999_000:
        imposto = int(rtb*0.23 - 636_000)
    elif rtb <= 17_999_000:
        imposto = int(rtb*0.33 - 1_536_000)
    elif rtb <= 39_999_000:
        imposto = int(rtb*0.40 - 2_796_000)
    else:
        imposto = int(rtb*0.45 - 4_796_000)

    if imposto < 0:
        imposto = 0

    return imposto

def resimp(sm: int):#imposto residencial

    valor = rt(sm)*0.10 + 5_000
    return valor

def seg(sm: int):#seguro desemprego

    vsa = sa(sm)
    seg = int(vsa*0.006)
    return seg
