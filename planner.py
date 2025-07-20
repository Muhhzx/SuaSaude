def gerar_plano_simples(objetivo):
    planos = {
        "Emagrecer":{
            "Alimentação":[
                "Evite alimentos ultraprocessados",
                "Inclua mais vegetais e fibras nas suas refeições"
            ],
            "Exercicios":[
                "Caminhada por 30 minutos por dia ",
                "Treinos funcionais 3x por semana"
            ],
            "Sono":[
                "Durma pelo menos 8 horas por dia, o sono é uma base na melhora de saúde de vida",
                "Evite usar telas 1h antes de dormir, isso vai deixar seu sono melhor"
            ]
        },
            "Ganhar massa muscular":{
                "Alimentação": [
                    "Coma mais proteína para garantir o ganho de massa(carnes, ovos são uma boa fonte de proteína para isso)",
                    "Fracionar refeições a cada 3 horas"
                ],
                 "Exercícios": [
                "Treinos de força 4x por semana",
                "Aumentar progressivamente as cargas"
            ],
            "Sono": [
                "Durma 8 horas por noite",
                "Tenha uma rotina regular de sono"
            ]
        }
    }
    return planos.get(objetivo, {})