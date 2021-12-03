class Extrator_url:
    def __init__(self, url):
        self.url = url

    def __str__(self):
        return self.url

    def __len__(self):
        return len(self.url)

    def get_url_base(self):
        return self.url[0:self.url.find('?')]

    def get_url_parametro(self):
        indice_divisor = self.url.find('?') + 1
        return self.url[indice_divisor:]

    def get_valor_parametro(self, parametro):
        indice_parametro = self.get_url_parametro().find(parametro)
        indice_valor = indice_parametro + len(parametro) + 1
        indice_e_comercial = self.get_url_parametro().find('&', indice_parametro)
        if indice_e_comercial >= 0:
            return self.get_url_parametro()[indice_valor:indice_e_comercial]
        else:
            return self.get_url_parametro()[indice_valor:]
