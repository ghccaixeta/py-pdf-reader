import pdfplumber
import json
import openpyxl
import shutil
import datetime

pdfFile = "recibo-pagamento.pdf"
xlsFile = pdfFile.replace(".pdf",".xlsx")

year = datetime.date.today().year
month = datetime.date.today().month

inputPDF = pdfplumber.open(pdfFile)

class Contracheque:
    def __init__(
        self,
        nomeFantasia = None,
        cnpj = None,
        centroDeCusto = None,
        evento = None,
        tipoJornada = None,
        periodo = None,
        codigoFuncionario = None,
        nomeFuncionario = None,
        cargoFuncionario = None,
        cbo = None,
        departamento = None,
        filial = None,
        admissaoFuncionario = None,
        lancamentos = None,
        totalVencimentos = None,
        totalDescontos = None,
        valorLiquido = None,
        salarioBase = None,
        salarioINSS = None,
        baseCalcFGTS = None,
        fgtsMes = None,
        baseCalcIRRF = None,
        faixaIRRF = None
        ):
        self.nomeFantasia = nomeFantasia, 
        self.cnpj = cnpj, 
        self.centroDeCusto = centroDeCusto,
        self.evento = evento,
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

    def to_dict(self):
        return {
            "nomeFantasia": self.nomeFantasia,
            "cnpj": self.cnpj,
            "centroDeCusto": self.centroDeCusto,
            "evento": self.evento,
            "tipoJornada": self.tipoJornada,
            "periodo": self.periodo,
            "codigoFuncionario": self.codigoFuncionario,
            "nomeFuncionario": self.nomeFuncionario,
            "cargoFuncionario": self.cargoFuncionario,
            "cbo": self.cbo,
            "departamento": self.departamento,
            "filial": self.filial,
            "admissaoFuncionario": self.admissaoFuncionario,
            "lancamentos": self.lancamentos,
            "totalVencimentos": self.totalVencimentos,
            "totalDescontos": self.totalDescontos,
            "valorLiquido": self.valorLiquido,
            "salarioBase": self.salarioBase,
            "salarioINSS": self.salarioINSS,
            "baseCalcFGTS": self.baseCalcFGTS,
            "fgtsMes": self.fgtsMes,
            "baseCalcIRRF": self.baseCalcIRRF,
            "faixaIRRF": self.faixaIRRF,
        }

    # def __str__(self):
    #     return f"nomeFantasia: {self.nomeFantasia},cnpj: {self.cnpj},evento: {self.evento},tipoJornada: {self.tipoJornada},periodo: {self.periodo},codigoFuncionario: {self.codigoFuncionario},nomeFuncionario: {self.nomeFuncionario},cargoFuncionario: {self.cargoFuncionario},cbo: {self.cbo},departamento: {self.departamento},filial: {self.filial},admissaoFuncionario: {self.admissaoFuncionario},lancamentos: {self.lancamentos},totalVencimentos: {self.totalVencimentos},totalDescontos: {self.totalDescontos},valorLiquido: {self.valorLiquido},salarioBase: {self.salarioBase},salarioINSS: {self.salarioINSS},baseCalcFGTS: {self.baseCalcFGTS},fgtsMes: {self.fgtsMes},baseCalcIRRF: {self.baseCalcIRRF},faixaIRRF: {self.faixaIRRF}"

def getLineContent(fullText, searchText):
    
    for item in fullText:
        if searchText in item:
            return item

    
    return ""

def getLancamento(fulltext):
    cabecalho = fulltext.find("Descontos\n") + 9
    fimLancamentos = fulltext.find("etsen")

    lancamentos = fulltext[cabecalho:fimLancamentos].strip()

    lines = lancamentos.splitlines()

    lancamentosArray = []

    for item in lines:
        colunas = item.split(" ")

        lancamento = {
            "cod": colunas[0],
            "descricao": ' '.join(map(str, colunas[1:-3])),
            "referencia": colunas[-3],
            "vencimentos": colunas[-2],
            "descontos": colunas[-1] if colunas[-1] != '.obicer' else None,
        }

        lancamentosArray.append(lancamento)
        
    return lancamentosArray

pageNumber = 0

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

    contracheque = Contracheque()

    lines = item.splitlines()
    contracheque.nomeFantasia = lines[0]
    
    linha02 = lines[1]
    contracheque.cnpj = linha02.split(" ")[1]
    
    linha03 = lines[2]
    contracheque.tipoJornada = linha03.split(" ")[:-3][0]
    contracheque.periodo = ' '.join(linha03.split(" ")[-3:])

    linha04 = lines[4]
    splitLinha04 = linha04.split(" ")
    contracheque.codigoFuncionario = splitLinha04[0]
    contracheque.nomeFuncionario = ' '.join(splitLinha04[1:-3])
    contracheque.cbo = splitLinha04[-3]
    contracheque.departamento = splitLinha04[-2]
    contracheque.filial = splitLinha04[-1]

    linha05 = lines[5]
    splitLinha05 = linha05.split("Admissão")
    contracheque.cargoFuncionario= splitLinha05[0]
    contracheque.admissaoFuncionario = splitLinha05[1]

    vencimentos = getLineContent(lines, 'ataD')

    contracheque.totalVencimentos = vencimentos.split(" ")[0]
    contracheque.totalDescontos = vencimentos.split(" ")[1]


    lineValorLiquido = getLineContent(lines, 'Valor Líquido')
    contracheque.valorLiquido = lineValorLiquido.split(" ")[-1]
    

    linesSplit = lines[-1].split(" ")

    contracheque.salarioBase = linesSplit[0]
    contracheque.salarioINSS = linesSplit[1]
    contracheque.baseCalcFGTS = linesSplit[2]
    contracheque.fgtsMes = linesSplit[3]
    contracheque.baseCalcIRRF = linesSplit[4]
    contracheque.faixaIRRF = linesSplit[5]

    contracheque.lancamentos = getLancamento(item)

    contracheques.append(contracheque)
    

shutil.copy('Template_Contracheques.xlsx', xlsFile)

workbook = openpyxl.load_workbook(xlsFile)
sheet = workbook.active

lineNumber = 2

for item in contracheques:

    for lancamentoItem in item.lancamentos:

        sheet[f'A{lineNumber}'] = item.codigoFuncionario
        sheet[f'B{lineNumber}'] = f"{lancamentoItem['cod']}_{year}_{month}"
        # sheet[f'C{lineNumber}'] = item.codigoFuncionario
        sheet[f'D{lineNumber}'] = datetime.date.today()
        sheet[f'F{lineNumber}'] = item.totalVencimentos
        sheet[f'G{lineNumber}'] = item.totalDescontos
        sheet[f'H{lineNumber}'] = item.valorLiquido
        sheet[f'I{lineNumber}'] = item.nomeFantasia
        sheet[f'J{lineNumber}'] = item.cnpj
        sheet[f'K{lineNumber}'] = item.codigoFuncionario
        sheet[f'L{lineNumber}'] = item.nomeFuncionario
        sheet[f'M{lineNumber}'] = item.cargoFuncionario
        sheet[f'N{lineNumber}'] = item.departamento
        sheet[f'P{lineNumber}'] = item.tipoJornada
        sheet[f'Q{lineNumber}'] = item.salarioBase
        sheet[f'R{lineNumber}'] = lancamentoItem["cod"]
        sheet[f'S{lineNumber}'] = lancamentoItem["descricao"]
        sheet[f'T{lineNumber}'] = lancamentoItem["vencimentos"]
        sheet[f'U{lineNumber}'] = lancamentoItem["descontos"]
        sheet[f'V{lineNumber}'] = lancamentoItem["referencia"]

        lineNumber += 1

workbook.save(xlsFile)

