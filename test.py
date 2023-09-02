# Seu texto completo
texto = """
TOUCH COMUNICACAO INTEGRADA LTDA.
CNPJ: 08.968.873/0001-02 CC: Centro de Custo Adiantamento
Mensalista Julho de 2023
Código Nome do Funcionário CBO Departamento Filial
3 GISLAINE DE VARGAS TRENZ 521110 1 1
VENDEDOR PLENO Admissão: 15/08/2022
Código Descrição Referência Vencimentos Descontos
980 ADIANTAMENTO SALARIAL 40,00 1.200,00 .obicer
etsen
oiránoicnuF
adanimircsid
od
arutanissA
adiuqíl
aicnâtropmi
a
odibecer
ret
oralceD
_______/____/____
Total de Vencimentos Total de Descontos
1.200,00 0,00 ataD

Valor Líquido 1.200,00
Salário Base Sal. Contr. INSS Base Cálc. FGTS F.G.T.S do Mês Base Cálc. IRRF Faixa IRRF
3.000,00 0,00 0,00 0,00 0,00 0,00
TOUCH COMUNICACAO INTEGRADA LTDA.
CNPJ: 08.968.873/0001-02 CC: Centro de Custo Adiantamento
"""

# Encontre a posição da linha que contém "Faixa IRRF"
posicao_faixa_irrf = texto.find("IRRF")
print(posicao_faixa_irrf)

# Encontre a posição da primeira linha após "Faixa IRRF"
linha_1_apos_faixa_irrf = texto.find("\n", posicao_faixa_irrf + 1)
print(linha_1_apos_faixa_irrf)
# Encontre a posição da segunda linha após "Faixa IRRF"
linha_2_apos_faixa_irrf = texto.find("\n", linha_1_apos_faixa_irrf + 1)
print(linha_2_apos_faixa_irrf)

# Verifique se ambas as posições foram encontradas
if posicao_faixa_irrf != -1 and linha_2_apos_faixa_irrf != -1:
    # Pegue o conteúdo entre a primeira linha e a segunda linha abaixo de "Faixa IRRF"
    conteudo = texto[:linha_2_apos_faixa_irrf].strip()
    print(conteudo)
else:
    print("Linha com 'Faixa IRRF' ou segunda linha abaixo não foi encontrada.")
