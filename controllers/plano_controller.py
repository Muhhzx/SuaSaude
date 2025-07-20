from flask import (
    Blueprint, render_template, request,
    redirect, url_for, session
)
from services.tips_service import gerar_dicas

bp = Blueprint('plano', __name__)

# Passo 1: escolha do objetivo
@bp.route('/plano/objetivo', methods=['GET', 'POST'])
def escolher_objetivo():
    if request.method == 'POST':
        session['objetivo'] = request.form.get('objetivo')
        return redirect(url_for('plano.questionario'))
    # GET: mostra opções de objetivo
    return render_template('objetivo.html')

# Passo 2: questionário de estado físico
@bp.route('/plano/questionario', methods=['GET', 'POST'])
def questionario():
    if 'objetivo' not in session:
        return redirect(url_for('plano.escolher_objetivo'))

    if request.method == 'POST':
        session['nome']             = request.form.get('nome')
        session['idade']            = request.form.get('idade')
        session['nivel_atividade']  = request.form.get('nivel_atividade')
        return redirect(url_for('plano.dicas'))

    return render_template('questionario.html',
                           objetivo=session['objetivo'])

# Passo 3: resultados e dicas
@bp.route('/plano/dicas')
def dicas():
    # Garante que todos os dados estejam na sessão
    required_keys = ('objetivo', 'idade', 'nivel_atividade', 'nome')
    if not all(k in session for k in required_keys):
        return redirect(url_for('plano.escolher_objetivo'))

    dicas_ = gerar_dicas(
        session['objetivo'],
        session['nivel_atividade'],
        n=3
    )
    return render_template(
        'dicas.html',
        nome=session['nome'],
        objetivo=session['objetivo'],
        idade=session['idade'],
        nivel=session['nivel_atividade'],
        dicas=dicas_
    )
from flask import Blueprint, request, render_template
from planner import gerar_plano_simples 

plano_bp = Blueprint('plano', __name__)

@plano_bp.route('/resultado', methods=['POST'])
def resultado():
    objetivo = request.form['objetivo']
    plano = gerar_plano_simples(objetivo)
    return render_template('resultado.html', objetivo=objetivo, plano=plano)
