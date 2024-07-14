## Listas encadeadas

Mas o que seria uma lista encadeada?
Uma lista encadeada é uma representação de uma sequência de objetos, todos do mesmo tipo, na memória RAM (= random
access memory) do computador. Cada elemento da sequência é armazenado em uma célula da lista: o primeiro elemento na
primeira célula, o segundo na segunda, e assim por diante.

Exemplo de lista encadeada:

```
class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
  }

  // Adiciona um novo nó no final da lista
  append(data) {
    let newNode = new Node(data);

    if (this.head === null) {
      this.head = newNode;
    } else {
      let current = this.head;
      while (current.next !== null) {
        current = current.next;
      }
      current.next = newNode;
    }
  }

  // Imprime todos os elementos da lista
  printList() {
    let current = this.head;
    while (current !== null) {
      console.log(current.data);
      current = current.next;
    }
  }
}

// Exemplo de uso:
let list = new LinkedList();
list.append(10);
list.append(20);
list.append(30);

list.printList();  // Output: 10 20 30

```

## Hash

Uma tabela de dispersão (ou hash table) é uma coleção de itens que são armazenados de maneira a serem encontrados com
facilidade mais tarde. Cada posição da tabela de dispersão, geralmente denominada índice (ou slot), pode guardar um item
e possui um rótulo inteiro começando a partir de 0. Por exemplo, teremos um índice com rótulo 0, um índice com rótulo 1,
outro com rótulo 2 e assim por diante. Inicialmente, a tabela de dispersão não contém nenhum item, então todos os
índices estão vazios. Nós podemos implementar uma tabela de dispersão usando uma lista com cada elemento inicializado
pelo valor especial None do Python. A Figura 4 mostra uma tabela de dispersão de tamanho m=11
. Em outras palavras, existem m índices na tabela, rotulados de 0 a 10.

O mapeamento entre a chave e o índice ao qual ela pertence na tabela é conhecido como a função de espalhamento (ou hash
function). A função de espalhamento irá receber qualquer item na coleção e irá retornar um inteiro dentro do intervalo
dos índices, isto é, entre 0 e m-1. Suponha, por exemplo, o conjunto de inteiros formado por 54, 26, 93, 17, 77 e 31.
Nossa primeira função de hash, às vezes chamada de “método do resto”, simplesmente pega um item e o divide pelo tamanho
da tabela, retornando o resto da divisão e o seu valor de espalhamento (h(item)=item%11
). A Tabela 4 mostra todos os valores de espalhamento para os itens do nosso conjunto. Observe que o método do resto (
artimética modular) tipicamente estará presente de algum modo em todas as funções de espalhamento, já que o resultado
deve estar dentro do intervalo dos índices.

Exemplo de Hash:

````
import hashlib

def string_to_ascii(input_string):
    # Converte a string para uma lista de valores ASCII
    ascii_values = [ord(char) for char in input_string]
    return ''.join(map(str, ascii_values))

def generate_hash(input_string):
    # Converte a string para valores ASCII
    ascii_string = string_to_ascii(input_string)
    # Cria um objeto hash SHA-256
    hash_object = hashlib.sha256()
    # Atualiza o objeto hash com a string ASCII
    hash_object.update(ascii_string.encode('utf-8'))
    # Retorna o hash em formato hexadecimal
    return hash_object.hexdigest()

# Exemplo de uso
input_string = "Hello, World!"
hashed_output = generate_hash(input_string)

print(f"Entrada: {input_string}")
print(f"String ASCII: {string_to_ascii(input_string)}")
print(f"Hash SHA-256: {hashed_output}")

````

### Referências:

**O que é uma lista encadeada e como implementá-la.** Disponível
em: <https://www.ime.usp.br/~pf/algoritmos/aulas/lista.html#:~:text=Uma%20lista%20encadeada%20>. Acesso em: 14 jul.

**5.5. Hashing — Resolução de Problemas Usando Python.** Disponível
em: <https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/Hashing.html>. Acesso em: 14 jul.