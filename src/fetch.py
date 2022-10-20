from bs4 import BeautifulSoup as bs
import requests


class Fetcher():
    def calcPrazo(self, cod_servico="04014", cep_origem="", cep_destino=""):
        URL = f"http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx/CalcPrazo?nCdServico={cod_servico}&sCepOrigem={cep_origem}&sCepDestino={cep_destino}"

        request = requests.get(URL)

        if (request.status_code == 200):
            soup = bs(request.text, 'xml')

            data = {
                "codigo": soup.Codigo.text,
                "prazoEntrega": soup.PrazoEntrega.text,
                "entregaDomiciliar": soup.EntregaDomiciliar.text,
                "entregaSabado": soup.EntregaSabado.text,
                "erro": soup.Erro.text,
                "msgErro": soup.MsgErro.text,
                "obsFim": soup.obsFim.text,
                "dataMaxEntrega": soup.DataMaxEntrega.text
            }

            return data


    def calcPreco(
        self,
        ncdempresa="",
        sdssenha="",
        ncdservico="04014",
        sceporigem="",
        scepdestino="",
        nvlpeso="",
        ncdformato="",
        nvlcomprimento="",
        nvlaltura="",
        nvllargura="",
        nvldiametro="",
        scdmaopropria="",
        nvlvalordeclarado="",
        scdavisorecebimento=""
    ):

        URL = \
            "http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx/CalcPreco?" +\
            f"nCdEmpresa={ncdempresa}" +\
            f"&sDsSenha={sdssenha}" +\
            f"&nCdServico={ncdservico}" +\
            f"&sCepOrigem={sceporigem}" +\
            f"&sCepDestino={scepdestino}" +\
            f"&nVlPeso={nvlpeso}" +\
            f"&nCdFormato={ncdformato}" +\
            f"&nVlComprimento={nvlcomprimento}" +\
            f"&nVlAltura={nvlaltura}" +\
            f"&nVlLargura={nvllargura}" +\
            f"&nVlDiametro={nvldiametro}" +\
            f"&sCdMaoPropria={scdmaopropria}" +\
            f"&nVlValorDeclarado={nvlvalordeclarado}" +\
            f"&sCdAvisoRecebimento={scdavisorecebimento}"

        request = requests.get(URL)

        if (request.status_code == 200):
            soup = bs(request.text, 'xml')

            data = {
                "codigo": soup.Codigo.text,
                "valor": soup.Valor.text,
                "valorMaoPropria": soup.ValorMaoPropria.text,
                "valorAvisoRecebimento": soup.ValorAvisoRecebimento.text,
                "valorValorDeclarado": soup.ValorValorDeclarado.text,
                "erro": soup.Erro.text,
                "msgErro": soup.MsgErro.text,
                "valorSemSdicionais": soup.ValorSemAdicionais.text
            }

            return data
