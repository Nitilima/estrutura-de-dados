class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.head = None

    def inserirSemPrioridade(self, nodo):
        if not self.head:
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = nodo

    def inserirComPrioridade(self, nodo):
        if not self.head:
            self.head = nodo
        elif self.head.cor == 'V':
            nodo.proximo = self.head
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo and atual.proximo.cor == 'A':
                atual = atual.proximo
            nodo.proximo = atual.proximo
            atual.proximo = nodo

    def inserir(self):
        cor = input("Insira a cor do cartão (A/V): ").upper()
        numero = int(input("Insira o número do cartão: "))
        nodo = Nodo(numero, cor)

        if not self.head:
            self.head = nodo
        elif cor == 'V':
            self.inserirSemPrioridade(nodo)
        elif cor == 'A':
            self.inserirComPrioridade(nodo)

    def imprimirListaEspera(self):
        atual = self.head
        if not atual:
            print("A lista está vazia.")
            return
        print("Lista ->", end=' ')
        while atual:
            print(f"[{atual.cor},{atual.numero}]", end=' ')
            atual = atual.proximo
        print()

    def atenderPaciente(self):
        if self.head:
            paciente = self.head
            self.head = self.head.proximo
            print(f"Chamando paciente com cartão {paciente.numero} para o atendimento.")
        else:
            print("Nenhum paciente na fila.")


def menu():
    lista_espera = ListaEncadeada()

    while True:
        print("\nMenu:")
        print("1 - Adicionar paciente à fila")
        print("2 - Mostrar pacientes na fila")
        print("3 - Chamar paciente")
        print("4 - Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            lista_espera.inserir()
        elif opcao == 2:
            lista_espera.imprimirListaEspera()
        elif opcao == 3:
            lista_espera.atenderPaciente()
        elif opcao == 4:
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    menu()
