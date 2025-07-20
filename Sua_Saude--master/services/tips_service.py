import random

DICAS = {
  'emagrecer': [  'Beba pelo menos 2 L de água por dia.',
        'Inclua 30 min de caminhada após as refeições.',
        'Tome chá verde sem açúcar entre as refeições.'
],
  'ganhar_massa': [ 'Consuma proteína em todas as refeições.',
        'Faça 5–6 refeições menores ao longo do dia.',
        'Invista em shakes pós-treino.'
 ],
}

def gerar_dicas(objetivo, nivel_atividade, n=3):
    base = DICAS.get(objetivo, [])
    escolhidas = random.sample(base, k=min(n, len(base)))
    if nivel_atividade == 'alta':
        escolhidas.append('Beba mais água durante o treino.')
    elif nivel_atividade == 'baixa':
        escolhidas.append('Caminhe 10 min extras por dia.')
    return escolhidas
