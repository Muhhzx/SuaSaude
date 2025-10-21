CLASSIFICACOES_IMC = [
    (18.5, "Abaixo do peso"),
    (24.9, "Peso normal"),
    (29.9, "Sobrepeso"),
    (34.9, "Obesidade Grau I"),
    (39.9, "Obesidade Grau II"),
    (float("inf"), "Obesidade Grau III")
]

# Dicas personalizadas para ganho de massa conforme IMC
DICAS_IMC = {
    "Abaixo do peso": "Aumente a ingestão calórica com proteínas e carboidratos de qualidade, treine com foco em força e faça 6 refeições ao dia.",
    "Peso normal": "Mantenha um superávit calórico moderado, priorize treino com sobrecarga progressiva e ajuste macros semanalmente.",
    "Sobrepeso": "Foque no ganho de massa magra controlando gordura corporal, priorize proteína e treino de força.",
    "Obesidade Grau I": "Ajuste a dieta para reduzir gordura e ganhar massa magra de forma equilibrada, com treinos resistidos.",
    "Obesidade Grau II": "Busque acompanhamento nutricional, reduza gordura corporal antes de focar no ganho de massa acelerado.",
    "Obesidade Grau III": "Procure orientação médica e nutricional antes de iniciar um plano intenso de ganho de massa."
}

def calcular_imc(peso: float, altura: float) -> float:
    """Calcula o IMC com validação de entrada."""
    if peso <= 0 or altura <= 0:
        raise ValueError("Peso e altura devem ser valores positivos.")
    return round(peso / (altura ** 2), 2)

def classificar_imc(imc: float) -> str:
    """Classifica o IMC com base nas faixas."""
    for limite, classificacao in CLASSIFICACOES_IMC:
        if imc <= limite:
            return classificacao
    return "Classificação desconhecida"

def obter_dica(imc: float) -> str:
    """Retorna dica personalizada baseada na classificação."""
    classificacao = classificar_imc(imc)
    return DICAS_IMC.get(classificacao, "Sem dica disponível para este IMC.")