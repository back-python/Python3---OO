class Programa:
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @property
    def likes(self):
        return self.__likes

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Duração: {self.duracao} min - Likes: {self.likes}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Duração: {self.temporadas} temporadas - Likes: {self.likes}'


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome.title()
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)


filme1 = Filme('Se beber, não case 2', '2011', '102')
serie1 = Serie('Anne with an E', '2017', '3')
filme2 = Filme('Todo mundo em pânico', '1999', '100')
serie2 = Serie('Demolidor', '2016', '2')

for i in range(0, 4):
    filme1.dar_like()
    filme1.dar_like()
    filme2.dar_like()
    filme2.dar_like()
    serie1.dar_like()
    serie2.dar_like()

programas = [filme1, serie1, filme2, serie2]
playlist1 = Playlist('fim de semana', programas)

print(f'TAMANHO DA PLAYLIST: {len(playlist1)}')

for programa in playlist1:
    print(programa)

# Polimorfismo me permite executar métodos de dois objetos diferentes com um laço de repetição
# programas = [filme1, serie1, filme2, serie2]
# for programa in programas:
#     print(programa)
