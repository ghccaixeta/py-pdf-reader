# Seu texto
texto = """
Código Nome do Funcionário CBO Departamento Filial
8 EDIMARA CAMILA ROLIM DE MOURA 521110 1 1
VENDEDOR PLENO Admissão: 08/03/2023
Código Descrição Referência Vencimentos Descontos
980 ADIANTAMENTO SALARIAL 40,00 1.200,00 .obicer
"""

# Divida o texto em linhas usando splitlines()
linhas = texto.splitlines()

# Itere pelas linhas para encontrar a linha que contém ".obicer" e imprima-a
for linha in linhas:
    if ".obicer" in linha:
        print(linha)