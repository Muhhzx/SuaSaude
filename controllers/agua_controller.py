from flask import Blueprint, render_template, session, request, redirect, url_for
from datetime import date
from models.meta_agua import MetaAgua
from models.consumo_agua import ConsumoAgua
from extensions import db
from sqlalchemy import func

agua_bp = Blueprint('agua', __name__)

@agua_bp.route('/')
def index():
    hoje = date.today()

   
    meta = MetaAgua.query.filter_by(data=hoje).first()
    if meta:
        meta_valor = meta.meta
    else:
        meta_valor = 2000  

    
    consumo = ConsumoAgua.query.filter_by(data=hoje).all()
    total_consumido = sum([c.quantidade for c in consumo])

    return render_template('index.html', 
                           agua_total=total_consumido, 
                           meta_agua=meta_valor)

@agua_bp.route('/adicionar_agua', methods=['POST'])
def adicionar_agua():
    ml = request.form.get('ml')

    if not ml:
        return "Erro: campo 'ml' não enviado", 400

    try:
        ml = int(ml)
    except ValueError:
        return "Erro: valor inválido para ml", 400

    consumo = ConsumoAgua(quantidade=ml, data=date.today())
    db.session.add(consumo)
    db.session.commit()

    return redirect(url_for('agua.index'))

@agua_bp.route('/definir_meta', methods=['POST'])
def definir_meta():
    meta = request.form.get('meta')

    if not meta:
        return "Erro: campo 'meta' não enviado", 400

    try:
        meta = int(meta)
    except ValueError:
        return "Erro: valor inválido para meta", 400

   
    meta_existente = MetaAgua.query.filter_by(data=date.today()).first()
    if meta_existente:
        meta_existente.meta = meta
    else:
        nova_meta = MetaAgua(meta=meta, data=date.today())
        db.session.add(nova_meta)

    db.session.commit()

    return redirect(url_for('agua.index'))

@agua_bp.route('/historico')
def historico():
   consumos_agrupados = db.session.query(
       ConsumoAgua.data,
       func.sum(ConsumoAgua.quantidade).label('total_consumido')
   ).group_by(ConsumoAgua.data).order_by(ConsumoAgua.data.desc()).all()

   metas = MetaAgua.query.all()
   metas_dict = {meta.data: meta.meta for meta in metas}

   historico = []
   for consumo in consumos_agrupados:
       data = consumo.data
       total_consumido = consumo.total_consumido
       meta = metas_dict.get(data)
       historico.append({
           'data': data,
           'total_consumido' : total_consumido,
           'meta': meta
       })

       consumos = ConsumoAgua.query.order_by(ConsumoAgua.data.desc()).all()
       return render_template('historico.html', historico = historico, consumos=consumos, metas=metas)