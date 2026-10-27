from sklearn.feature_extraction.text import TfidfVectorizer
from text_analysis import preprocessar_texto

t1 = "Gamificação melhora o engajamento dos alunos."
t2 = "O uso de gamificação aumenta o envolvimento dos estudantes."

corpus = [preprocessar_texto(t1), preprocessar_texto(t2)]

vectorizer = TfidfVectorizer()
matriz = vectorizer.fit_transform(corpus)

print("Vocabulário:")
print(vectorizer.get_feature_names_out())

print("\nMatriz TF-IDF:")
print(matriz.toarray())
