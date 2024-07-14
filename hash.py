class Node:
    def __init__(self, sigla, nome_estado):
        self.sigla = sigla
        self.nome_estado = nome_estado
        self.proximo = None


class TabelaHash:
    def __init__(self):
        self.tabela = [None] * 10

    def hash(self, sigla):
        if sigla == 'DF':
            return 7
        ascii_sum = ord(sigla[0]) + ord(sigla[1])
        return ascii_sum % 10

    def inserir(self, sigla, nome_estado):
        posicao = self.hash(sigla)
        novo_nodo = Node(sigla, nome_estado)
        novo_nodo.proximo = self.tabela[posicao]
        self.tabela[posicao] = novo_nodo

    def imprimir(self):
        for i in range(len(self.tabela)):
            print(f"{i}: ", end="")
            nodo_atual = self.tabela[i]
            if nodo_atual is None:
                print("None")
            else:
                while nodo_atual:
                    print(f"{nodo_atual.sigla}", end="")
                    nodo_atual = nodo_atual.proximo
                    if nodo_atual:
                        print(" -> ", end="")
                print(" -> None")  # Indica o final da lista


tabela_hash = TabelaHash()

print("------------Tabela Hash------------")
tabela_hash.imprimir()

estados = [
    ("AC", "Acre"),
    ("AL", "Alagoas"),
    ("AP", "Amapá"),
    ("AM", "Amazonas"),
    ("BA", "Bahia"),
    ("CE", "Ceará"),
    ("DF", "Distrito Federal"),
    ("ES", "Espírito Santo"),
    ("GO", "Goiás"),
    ("MA", "Maranhão"),
    ("MT", "Mato Grosso"),
    ("MS", "Mato Grosso do Sul"),
    ("MG", "Minas Gerais"),
    ("PA", "Pará"),
    ("PB", "Paraíba"),
    ("PR", "Paraná"),
    ("PE", "Pernambuco"),
    ("PI", "Piauí"),
    ("RJ", "Rio de Janeiro"),
    ("RN", "Rio Grande do Norte"),
    ("RS", "Rio Grande do Sul"),
    ("RO", "Rondônia"),
    ("RR", "Roraima"),
    ("SC", "Santa Catarina"),
    ("SP", "São Paulo"),
    ("SE", "Sergipe"),
    ("TO", "Tocantins")
]

for sigla, nome_estado in estados:
    tabela_hash.inserir(sigla, nome_estado)

print("\n------------Estados e DF------------")
tabela_hash.imprimir()

estado_ficticio = ("NA", "Nicolle Anjos")
tabela_hash.inserir(*estado_ficticio)

print("\n------------Estado fictício------------")
tabela_hash.imprimir()
