import requests

class Busca_cotacao:
    def __init__(self, moeda_origem):
        self.cotacao = self.requisicao(moeda_origem)

    def requisicao(self, moeda_origem):
        requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,BRL-USD")
        requisicao_dic = requisicao.json()
        if moeda_origem == 'dolar':
            return requisicao_dic["USDBRL"]["bid"]
        else:
            return requisicao_dic["BRLUSD"]["bid"]

