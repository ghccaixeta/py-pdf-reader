# Sua string de texto
texto = """xsdasd
a
b
c
Código Descrição Referência Vencimentos Descontos
980 ADIANTAMENTO SALARIAL 40,00 950,40 .obicer
etsen
Outro texto aqui.
"""

# Encontre a posição da primeira linha
posicao_primeira_linha = texto.find("\n") +2  # Adicione 1 para ignorar o caractere de nova linha

# Encontre a posição de "etsen" a partir da posição da primeira linha
posicao_etsen = texto.find("etsen", posicao_primeira_linha)

# Verifique se ambas as strings foram encontradas
if posicao_primeira_linha != -1 and posicao_etsen != -1:
    # Extraia o conteúdo entre as posições encontradas
    conteudo = texto[posicao_primeira_linha:posicao_etsen].strip()
    print(conteudo)
else:
    print("A primeira linha ou 'etsen' não foi encontrada no texto.")