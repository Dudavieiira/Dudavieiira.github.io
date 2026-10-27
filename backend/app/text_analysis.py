# Pré-processar textos (lowercase, limpeza)

# Vetorizar textos (TF-IDF)

# Calcular similaridade (cosine similarity)

import re
from sklearn.feature_extraction.text import TfidfVectorizer # Conversão de dados não estruturados em representação vetorial
from sklearn.metrics.pairwise import cosine_similarity # Mede o ângulo entre dois vetores: Quanto menor o ângulo mais parecidos


def preprocessar_texto(texto: str) -> str: # pré-processamento para padronização dos textos antes da análise
    """
    Realiza limpeza básica do texto:
    - converte para minúsculas
    - remove caracteres especiais
    - remove espaços extras
    """
    texto = texto.lower()
    texto = re.sub(r"[^a-zà-ú0-9\s]", "", texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto


def calcular_similaridade(texto1: str, texto2: str) -> float:
    """
    Calcula a similaridade textual entre dois textos
    utilizando TF-IDF e similaridade do cosseno.
    Retorna o valor em porcentagem.
    """

    texto1 = preprocessar_texto(texto1)
    texto2 = preprocessar_texto(texto2)

    corpus = [texto1, texto2]

    vectorizer = TfidfVectorizer()
    matriz_tfidf = vectorizer.fit_transform(corpus)

    similaridade = cosine_similarity(matriz_tfidf[0:1], matriz_tfidf[1:2])

    return float(round(similaridade[0][0] * 100, 2))

