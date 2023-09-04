texto = """
Código Descrição Referência Vencimentos Descontos
980 ADIANTAMENTO SALARIAL 40,00 950,40 .obicer
980 ADIANTAMENTO SALARIAL 40,00 950,40 .obicer
980 ADIANTAMENTO SALARIAL 40,00 950,40 .obicer
etsen
Outro texto aqui.
"""

# Encontre a posição inicial e final
posicao_inicio = texto.find("Código Descrição Referência Vencimentos Descontos")
posicao_fim = texto.find("etsen")

# Verifique se ambas as strings foram encontradas
if posicao_inicio != -1 and posicao_fim != -1:
    # Extraia o conteúdo entre as posições encontradas
    conteudo = texto[posicao_inicio + len("Código Descrição Referência Vencimentos Descontos"):posicao_fim].strip()
    print(conteudo)
else:
    print("Uma ou ambas as strings não foram encontradas no texto.")