import pdfplumber

inputPDF = pdfplumber.open('recibo-pagamento.pdf')

class Contracheque:
    def __init__(
        self,
        nomeFantasia, 
        cnpj, 
        centroDeCusto,
        tipoLancamento,
        tipoJornada,
        periodo,
        codigoFuncionario,
        nomeFuncionario,
        cargoFuncionario,
        cbo,
        departamento,
        filial,
        admissaoFuncionario,
        lancamentos,
        totalVencimentos,
        totalDescontos,
        valorLiquido,
        salarioBase,
        salarioINSS,
        baseCalcFGTS,
        fgtsMes,
        baseCalcIRRF,
        faixaIRRF
        ):
        self.nomeFantasia = nomeFantasia, 
        self.cnpj = cnpj, 
        self.centroDeCust = centroDeCusto,
        self.tipoLancament = tipoLancamento,
        self.period = periodo,
        self.codigoFuncionari = codigoFuncionario,
        self.nomeFuncionari = nomeFuncionario,
        self.cargoFuncionari = cargoFuncionario,
        self.cb = cbo,
        self.departament = departamento,
        self.filia = filial,
        self.admissaoFuncionari = admissaoFuncionario,
        self.lancamento = lancamentos,
        self.totalVenciment = totalVencimentos
        self.totalDescont = totalDescontos
        self.valorLiquid = valorLiquido,
        self.salarioBas = salarioBase,
        self.salarioINS = salarioINSS,
        self.baseCalcFGT = baseCalcFGTS,
        self.fgtsMe = fgtsMes,
        self.baseCalcIRR = baseCalcIRRF,
        self.faixaIR = faixaIRRF

def getLineContent(fullText, searchText):
    
    for item in fullText:
        if searchText in item:
            return item

    
    return ""

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

contracheques = [];

for item in contrachequesArray:
    lines = item.splitlines()
    nomeFantasia = lines[0]
    linha02 = lines[1]
    cnpj = linha02.split(" ")[1]
    linha03 = lines[2]
    tipoJornada = linha03.split(" ")[:-3][0]
    periodo = ' '.join(linha03.split(" ")[-3:])

    vencimentos = getLineContent(lines, 'ataD')

    totalVencimentos = vencimentos.split(" ")[0]
    totalDescontos = vencimentos.split(" ")[1]

    linesSplit = lines[-1].split(" ")

    salarioBase = linesSplit[0]
    salarioINSS = linesSplit[1]
    baseCalcFGTS = linesSplit[2]
    fgtsMes = linesSplit[3]
    baseCalcIRRF = linesSplit[4]
    faixaIRRF = linesSplit[5]

    print(salarioBase, salarioINSS,baseCalcFGTS,fgtsMes,baseCalcIRRF,faixaIRRF)

    
    