from text_analysis import calcular_similaridade

pares = [
    (
        "O sistema calcula a similaridade textual utilizando a técnica TF-IDF.",
        "O sistema realiza o cálculo de similaridade textual por meio da técnica TF-IDF."
    ),
    (
        "O método TF-IDF transforma textos em vetores numéricos para análise.",
        "O método TF-IDF transforma textos em vetores numéricos para análise textual."
    ),
    (
        "Gamificação melhora o engajamento dos alunos.",
        "O uso de gamificação aumenta o envolvimento dos estudantes."
    ),
    (
        "O aluno apresentou bom desempenho na prova.",
        "O estudante obteve resultados satisfatórios na avaliação."
    ),
    (
        "O sistema calcula similaridade textual.",
        "A previsão do tempo indica chuva amanhã."
    )
]

for i, (t1, t2) in enumerate(pares, 1):
    print(f"\nPar {i}")
    print(f"Texto 1: {t1}")
    print(f"Texto 2: {t2}")
    print(f"Similaridade: {calcular_similaridade(t1, t2)}%")
