from text_analysis import preprocessar_texto

texto_original = """Olá! Este é um TEXTO de Teste.
Possui   espaços   extras, pontuação!!!"""

texto_processado = preprocessar_texto(texto_original)

print("Texto original:")
print(texto_original)

print("\nTexto após pré-processamento:")
print(texto_processado)
