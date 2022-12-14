import PySimpleGUI as sg
from fetch import Fetcher

class Gui():
    
    fetcher = Fetcher()

    def __init__(self):
        sg.change_look_and_feel("DarkGrey11")
        # Layout
        self.layout_prazo = [
            # [sg.Text("COD Serviço",size=(8,0)), sg.Input(key="cod_servico",size=(8,3))],
            [sg.Text("CEP Origem", size=(15, 0)), sg.Input(key="cep_origem1", size=(15, 3))],
            [sg.Text("CEP Destino", size=(15, 0)), sg.Input(key="cep_destino1", size=(15, 3))],
            [sg.Multiline(size=(60,15), disabled=True, autoscroll=False, key="output_prazo")],
            [sg.Button("Calcular Prazo")]
        ]
        self.layout_preco = [
            [sg.Text("CEP Origem", size=(15, 0)), sg.Input(key="cep_origem2", size=(8, 3))],
            [sg.Text("CEP Destino", size=(15, 0)), sg.Input(key="cep_destino2", size=(8, 3))],

            [sg.Text("Peso", size=(15, 0)), sg.Input(key="peso", size=(8, 3))],
            [sg.Text("Formato", size=(15, 0)), sg.Slider(key="formato",range=(1,3), default_value=1, size=(10,5), orientation="h")],

            [sg.Text("Comprimento", size=(15, 0)), sg.Input(key="comprimento", size=(5, 0))],
            [sg.Text("Altura", size=(15, 0)), sg.Input(key="altura", size=(5, 0))],
            [sg.Text("Largura", size=(15, 0)), sg.Input(key="largura", size=(5, 0))],
            [sg.Text("Diametro", size=(15, 0)), sg.Input(key="diametro", size=(5, 0))],
            [sg.Text("Valor Declarado", size=(15, 0)), sg.Input(key="valor_declarado", size=(5, 0))],

            [sg.Checkbox("Recebimento Mão Propria", key="mao_propria", size=(30, 0))],
            [sg.Checkbox("Aviso de Recebimento", key="aviso_recebimento", size=(30, 0))],
            [sg.Multiline(size=(60,15), disabled=True, autoscroll=False, key="output_preco")],

            [sg.Button("Calcular Preço")]  
        ]

        # Tabs
        self.tab_group = [
            [
                sg.TabGroup(
                    [
                        [
                            sg.Tab("Calcular Prazo", self.layout_prazo,
                                   background_color="gray"),
                            sg.Tab("Calcular Preço", self.layout_preco,
                                   background_color="gray")
                        ]
                    ]
                )
            ]
        ]

        # Janela
        self.window = sg.Window(
            "Atividade de consumir WebService", self.tab_group)

    def run(self):
        while True:
            self.event, self.values = self.window.read()
            if(self.event == sg.WIN_CLOSED):
                break
            if(self.event == "Calcular Prazo"):
                cep_origem = self.values["cep_origem1"]
                cep_destino = self.values["cep_destino1"]

                data = self.fetcher.calcPrazo("04014", cep_origem, cep_destino)

                self.window["output_prazo"].print(
                    f"""
                    CEP de Origem: {cep_origem}
                    CEP de Destino: {cep_destino}
                    Prazo de entrega: {data["prazoEntrega"]}
                    Data máxima para entrega: {data["dataMaxEntrega"]}
                    Entrega Domiciliar? : {data["entregaDomiciliar"]}
                    Entrega aos Sábados? : {data["entregaSabado"]}
                    ----------------------------------------------
                    Erro: {data["erro"]}
                    Mensagem de Erro: {data["msgErro"]}
                    Observação final: {data["obsFim"]}
                    """+"\n"
                )
            if(self.event == "Calcular Preço"):
                ncdempresa = ""
                sdssenha = ""
                ncdservico = "04014"
                sceporigem = self.values["cep_origem2"]
                scepdestino = self.values["cep_destino2"]
                nvlpeso = self.values["peso"]
                ncdformato = int(self.values["formato"])
                nvlcomprimento = self.values["comprimento"]
                nvlaltura = self.values["altura"]
                nvllargura = self.values["largura"]
                nvldiametro = self.values["diametro"]
                scdavisorecebimento = "S" if self.values["aviso_recebimento"] else "N"
                scdmaopropria = "S" if self.values["mao_propria"] else "N"
                nvlvalordeclarado = self.values["valor_declarado"]

                data = self.fetcher.calcPreco(
                    ncdempresa,
                    sdssenha,
                    ncdservico,
                    sceporigem,
                    scepdestino,
                    nvlpeso,
                    ncdformato,
                    nvlcomprimento,
                    nvlaltura,
                    nvllargura,
                    nvldiametro,
                    scdmaopropria,
                    nvlvalordeclarado,
                    scdavisorecebimento
                )
                
                self.window["output_preco"].print(
                    f"""
                    CEP de Origem: {sceporigem}
                    CEP de Destino: {scepdestino}
                    Valor declarado do objeto: {data["valorValorDeclarado"]}
                    Valor de entrega à Mão Própria?: {data["valorMaoPropria"]}
                    Valor de envio: {data["valor"]}
                    Valor sem os adicionais: {data["valorSemSdicionais"]}
                    ----------------------------------------------
                    Erro: {data["erro"]}
                    Mensagem de Erro: {data["msgErro"]}
                    """+"\n"
                )


        
    
