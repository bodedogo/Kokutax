from funConK import (seguro, imposto as calc_imposto, saude, previdencia as calc_previdencia,
                     deducao_inicial, deducao_secundaria as calc_deducao_secundaria,
                     renda_tributavel as calc_renda_tributavel, salario_anual as calc_salario_anual,
                     imposto_residencial, salario_depois_deducao,
                     salario_pos_impostos_extras as calc_salario_pos)
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

@app.route("/user")
def user():

    return render_template("user.html")



@app.route("/calcular", methods=["POST"])
def calcular():
    salario_cru = request.form.get("salario") or ""

    salario_cru = salario_cru.replace(".", "").replace(",", ".")
    try:
        salario_mensal = float(salario_cru)
    except ValueError:
        return render_template("index.html", erro="Valor inválido.")

    if salario_mensal <= 95_000 or "":
        return render_template(
            "index.html",
            erro="Salário abaixo do mínimo permitido! (95.000)",
            link="https://youtu.be/dQw4w9WgXcQ?si=AbdXcK7v8ncoeNfP",
        )

    cidade = request.form.get("cidade") or "tokyo"
    visto  = request.form.get("visto")  or "kosei"

    valor_salario        = calc_salario_anual(salario_mensal)
    deducao_salario      = deducao_inicial(valor_salario)
    deducao_basica       = calc_deducao_secundaria(valor_salario)
    salario_apos_deducao = salario_depois_deducao(valor_salario, deducao_salario, deducao_basica)

    valor_previdencia = calc_previdencia(salario_apos_deducao, visto)
    seguro_de_saude   = saude(salario_apos_deducao, cidade)
    seguro_desemprego    = seguro(valor_salario)

    base_tributavel      = calc_salario_pos(salario_apos_deducao, valor_previdencia, seguro_de_saude)
    valor_renda_trib     = calc_renda_tributavel(base_tributavel)

    valor_imposto        = calc_imposto(valor_renda_trib, cidade, visto)
    residencia           = imposto_residencial(valor_renda_trib, cidade, visto)

    return render_template(
        "index.html",
        salario_anual=valor_salario,
        deducao_salario=deducao_salario,
        salario_apos_deducao=salario_apos_deducao,
        previdencia=valor_previdencia,
        seguro_de_saude=seguro_de_saude,
        seguro_desemprego=seguro_desemprego,
        deducao_basica=deducao_basica,
        renda_tributavel=valor_renda_trib,
        imposto=valor_imposto,
        residencia=residencia,
    )


if __name__ == "__main__":
    app.run(debug=True)