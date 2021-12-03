from extrator_url import Extrator_url
from busca_cotacao import Busca_cotacao

url = 'https://bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real'
extrator_url = Extrator_url(url)

moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")

cotacao = Busca_cotacao(moeda_origem)
conversao = float(cotacao.cotacao) * int(quantidade)

if moeda_origem == 'real':
    print(f'Você possui U$ {conversao}')
else:
    print(f'Você possui R$ {conversao}')
