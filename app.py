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

@app.route("/user")
def user():
    return render_template("user.html")



@app.route("/calcular", methods=["POST"])
def calcular():
    salario_cru = request.form.get("salario") or ""
    
    salario_cru = salario_cru.replace(".", "").replace(",",".")
    try:
        sm = float(salario_cru)
    except:
        return render_template("index.html", erro="valor invalido")
    if sm <= 95_000:
        return render_template("index.html", erro="salario abaixo do minimo permitido! (95.000)",
        link = "https://youtu.be/dQw4w9WgXcQ?si=AbdXcK7v8ncoeNfP")

    cidade = request.form.get("cidade") or "tokyo"
    visto = request.form.get("visto") or "kosei"

    salario_anual = sm * 12
    deducao_salario = eid(sm)
    salario_apos_deducao = salario_anual - deducao_salario

    previdencia = prev(sm, visto)
    seguro_de_saude = saude(sm, cidade)
    seguro_desemprego = seg(sm)

    deducao_basica = bd(sm)
    renda_tributavel = rt(sm, cidade, visto)

    imposto = imp(sm, cidade, visto)
    residencia = resimp(sm, cidade, visto)

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



app.run(debug=True)