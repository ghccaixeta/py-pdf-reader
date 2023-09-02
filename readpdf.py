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
    
    rodape = item.find("IRRF")
    
    if rodape != -1:
        posicaoAntePenultimaLinha = item.find("\n", rodape + 1)
        posicaoUltimaLinha = item.find("\n", posicaoAntePenultimaLinha + 1)
        contracheque = item[:posicaoUltimaLinha].strip()
        contrachequesArray.append(contracheque)
    else:
        print("Não foi possível localizar o rodapé.")


for item in contrachequesArray:
    print(item)
    print("----------------------------------------------------")