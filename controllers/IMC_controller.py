from flask import Blueprint, request, render_template
from models.IMC_models import calcular_imc, classificar_imc, obter_dica

imc_bp = Blueprint('imc', __name__)

@imc_bp.route('/imc', methods=['POST'])
def imc():
    peso = request.form.get('peso')
    altura = request.form.get('altura')
    unidade_altura = request.form.get('unidade_altura')

    if not peso or not altura:
        erro = "Por favor, preencha todos os campos."
        return render_template('imc.html', erro=erro)

    try:
        peso = float(peso)
        altura = float(altura)

        # Conversão se estiver em centímetros
        if unidade_altura == 'cm':
            altura = altura / 100  # converte para metros
    except ValueError as e:
        return render_template('imc.html', erro="Valores inválidos.")

    imc_valor = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc_valor)
    dica = obter_dica(imc_valor)

    # Define cor com base na classificação
    if classificacao == "Peso normal":
        classe_css = "resultado-sucesso"
    elif classificacao in ["Sobrepeso", "Levemente abaixo do peso"]:
        classe_css = "resultado-atencao"
    else:
        classe_css = "resultado-perigo"

    resultado = {
        "imc": f"{imc_valor:.2f}",
        "classificacao": classificacao,
        "dica": dica
    }

    return render_template('imc.html', resultado=resultado, classe_css=classe_css)
