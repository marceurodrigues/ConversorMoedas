# Sistema de Cotação de Moedas
# Tech Stack: Python(Kivy)
# Dev Marcéu Rodrigues

from kivy.app import App
from kivy.lang import Builder
import requests

GUI = Builder.load_file("tela.kv")

class MeuAplicativo(App):
    def build(self):
        return GUI

    def on_start(self):
        self.pegar_cotacao('USD')

        self.root.ids["moeda1"].text = f"Dólar: USA R${self.pegar_cotacao('USD')}"
        self.root.ids["moeda2"].text = f"Euro: R${self.pegar_cotacao('EUR')}"
        self.root.ids["moeda3"].text = f"Libra: R${self.pegar_cotacao('GBP')}"
        self.root.ids["moeda4"].text = f"Iene: R${self.pegar_cotacao('JPY')}"
        self.root.ids["moeda5"].text = f"Dólar AUS: R${self.pegar_cotacao('AUD')}"
        self.root.ids["moeda6"].text = f"Franco Suíço: R${self.pegar_cotacao('CHF')}"
        self.root.ids["moeda7"].text = f"Dólar CAN: R${self.pegar_cotacao('CAD')}"
        self.root.ids["moeda8"].text = f"Yuan: R${self.pegar_cotacao('CNY')}"
        self.root.ids["moeda9"].text = f"Bitcoin: R${self.pegar_cotacao('BTC')}"
        self.root.ids["moeda10"].text = f"Ethereum: R${self.pegar_cotacao('ETH')}"

    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        # print(requisicao.json())
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao


MeuAplicativo().run()
