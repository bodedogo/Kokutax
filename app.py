from funConK import seg, imp, saude, prev, eid, bd, rt, resimp
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "index.html",
        salario_anual=0,
        deducao_salario=0,
        salario_apos_deducao=0,
        previdencia=0,
        seguro_de_saude=0,
        deducao_basica=0,
        renda_tributavel=0,
        imposto=0,
        residencia=0,
        seguro_desemprego=0,
    )


@app.route("/calcular", methods=["POST"])
def calcular():
    sm = int(request.form.get("salario") or 0)

    

    salario_anual = sm * 12
    deducao_salario = eid(sm)
    salario_apos_deducao = salario_anual - deducao_salario

    previdencia = prev(sm)
    seguro_de_saude = saude(sm)
    seguro_desemprego = seg(sm)
    deducao_basica = bd(sm)
    renda_tributavel = rt(sm)
    imposto = imp(sm)
    residencia = resimp(sm)

    if sm < 95000:
        return render_template(
            "index.html",
            erro="Salário deve ser maior que 95.000 ienes, caso contrário peça insenção a sua prefeitura ",
            salario_anual=0,
            deducao_salario=0,
            salario_apos_deducao=0,
            previdencia=0,
            seguro_de_saude=0,
            seguro_desemprego=0,
            deducao_basica=0,
            renda_tributavel=0,
            imposto=0,
            residencia=0,
        )

    return render_template(
        "index.html",
        salario_anual=salario_anual,
        deducao_salario=deducao_salario,
        salario_apos_deducao=salario_apos_deducao,
        previdencia=previdencia,
        seguro_de_saude=seguro_de_saude,
        seguro_desemprego=seguro_desemprego,
        deducao_basica=deducao_basica,
        renda_tributavel=renda_tributavel,
        imposto=imposto,
        residencia=residencia,
    )


if __name__ == "__main__":
    app.run(debug=True)

app.run(debug=True)
