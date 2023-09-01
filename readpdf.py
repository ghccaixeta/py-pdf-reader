# import pandas as pd
# import pdfquery

# pdf = pdfquery.PDFQuery('recibo-pagamento.pdf')
# pdf.load()

# # convert the pdf to XML
# pdf.tree.write('customers.xml', pretty_print = True)




# # access the data using coordinates
# customer_name = pdf.pq('LTTextLineHorizontal:in_bbox("14.94, 744.24, 151.26, 753.24")').text()

# print(customer_name)




# from PyPDF2 import PdfReader

# reader = PdfReader("recibo.pdf")
# number_of_pages = len(reader.pages)
# page = reader.pages[0]
# text = page.extract_text()

# print(text)

import pdfplumber

inputPDF = pdfplumber.open('recibo-pagamento.pdf')


pageNumber = 0;

output = None

conteudoArray = []
contrachequesArray = []

for page in inputPDF.pages:
    pdfText = page.extract_text()
    conteudoArray.append(pdfText)


inputPDF.close()

for item in conteudoArray:
    
    posicao_primeira_linha = item.find("\n") + 1
    posicao_etsen = item.find("etsen", posicao_primeira_linha)

    if posicao_primeira_linha != -1 and posicao_etsen != -1:
        contracheque = item[posicao_primeira_linha:posicao_etsen].strip()
        contrachequesArray.append(contracheque)


for item in contrachequesArray:
    print(item)
    print("----------------------------------------------------")

# Seu texto completo

# texto = """
# Código Descrição Referência Vencimentos Descontos
# 980 ADIANTAMENTO SALARIAL 40,00 950,40 .obicer
# 980 ADIANTAMENTO SALARIAL 40,00 950,40 .obicer
# 980 ADIANTAMENTO SALARIAL 40,00 950,40 .obicer
# etsen
# Outro texto aqui.
# """

# # Encontre a posição inicial e final
# posicao_inicio = texto.find("Código Descrição Referência Vencimentos Descontos")
# posicao_fim = texto.find("etsen")

# # Verifique se ambas as strings foram encontradas
# if posicao_inicio != -1 and posicao_fim != -1:
#     # Extraia o conteúdo entre as posições encontradas
#     conteudo = texto[posicao_inicio + len("Código Descrição Referência Vencimentos Descontos"):posicao_fim].strip()
#     print(conteudo)
# else:
#     print("Uma ou ambas as strings não foram encontradas no texto.")