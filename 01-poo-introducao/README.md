# 📘 Tema 01 – Introdução à Programação Orientada a Objetos (POO)

## 🧠 O que é POO?

A Programação Orientada a Objetos (POO) é um paradigma de programação baseado no conceito de "objetos", que são instâncias de "classes". A ideia é representar elementos do mundo real (ou conceitos abstratos) dentro do código, organizando informações e comportamentos de forma mais estruturada.

### 🤔 Como assim?

Imagina que eu queira criar uma "tarefa" para um sistema onde eu gerencio minhas atividades do dia a dia. Se fosse em programação procedural, eu poderia fazer algo assim:

```python
tarefa1 = "Lavar a louça"
tarefa1_feita = True
tarefa1_entrega = "2025-04-20"
tarefa1_responsavel = "Luan"
```

Com uma ou duas tarefas isso funciona. Mas e se o sistema tiver centenas, milhares ou até milhões de tarefas? E se cada tarefa tiver vários atributos como prazo, responsável, status, prioridade, etc.? Começa a ficar caótico.

É aí que entra a POO.

Com POO, podemos criar uma estrutura padrão (classe) que define o que é uma tarefa, e depois criar objetos baseados nela, cada um com seus próprios dados. Exemplo:

```python
class Tarefa:
    def __init__(self, titulo, feita, entrega, pessoa):
        self.titulo = titulo
        self.feita = feita
        self.entrega = entrega
        self.pessoa = pessoa

    def exibir(self):
        status = "✔️ Feita" if self.feita else "❌ Pendente"
        print(f"Tarefa: {self.titulo} | Entrega: {self.entrega} | Responsável: {self.pessoa} | Status: {status}")

# Criando objetos
tarefa1 = Tarefa("Lavar a louça", True, "2025-04-20", "Luan")
tarefa2 = Tarefa("Estudar para prova", False, "2025-04-22", "Ana")

tarefa1.exibir()
tarefa2.exibir()
```
Agora sim, o código está organizado, reutilizável e com todas as informações encapsuladas dentro de cada objeto.

💡 Isso é Programação Orientada a Objetos na prática:
organização, reuso e clareza — tudo em um só lugar!

---

## 🧱 Conceitos Básicos

| Conceito     | Explicação                                                                 |
|--------------|----------------------------------------------------------------------------|
| **Classe**   | Um modelo (molde) que define atributos e comportamentos de um objeto       |
| **Objeto**   | Instância de uma classe; é quem "existe" no programa                       |
| **Atributos**| Variáveis que pertencem ao objeto                                          |
| **Métodos**  | Funções que pertencem ao objeto e definem seu comportamento               |
| **Instância**| O processo de criar um objeto a partir de uma classe                      |

---

## 🧮 Outro Exemplo Prático (Python)

```python
class Pessoa:
    def __init__(self, nome, idade, amigo=None):
        self.nome = nome
        self.idade = idade
        self.amigo = amigo

    def apresentar(self):
        print(f"Olá! Meu nome é {self.nome} e tenho {self.idade} anos.")

    def ver_amizade(self):
        if self.amigo:
            print(f"{self.nome} é amigo de {self.amigo.nome}.")
        else:
            print(f"{self.nome} ainda não tem amigo cadastrado.")

    def set_amigo(self, amigo):
        self.amigo = amigo

# Criando objetos
p1 = Pessoa("Luan", 20)
p2 = Pessoa("Maria", 20)

p1.apresentar()
p2.apresentar()

p1.set_amigo(p2)
p1.ver_amizade()
```
Viu só? Além de criar os objetos e exibi-los, também podemos definir funções específicas para eles, como ver_amizade, que usa os próprios atributos do objeto para construir uma ação lógica.

🔁 Esse é um exemplo de objetos interagindo entre si — aqui a pessoa tem outra pessoa como atributo (uma amizade!).
Não precisa se preocupar com isso agora se parecer complexo — o importante é entender que objetos podem carregar outros objetos e isso permite criar sistemas muito mais realistas e completos.

---

## 🧩 Comparando com o paradigma procedural

| Procedural                  | Orientado a Objetos                 |
|----------------------------|-------------------------------------|
| Baseado em funções e dados | Baseado em objetos (dados + ações)  |
| Código menos modular       | Código mais organizado e reutilizável |
| Menor encapsulamento       | Forte encapsulamento                |

---

## ✅ Vantagens da POO

- **Modularidade**: divide o código em partes menores (classes)
- **Reutilização**: classes podem ser reaproveitadas
- **Facilidade de manutenção**: mais organizado e legível
- **Expansibilidade**: fácil de estender sem alterar muito o que já existe

---

## 🧪 Exercício Proposto

> Crie uma classe `Livro` com os atributos `titulo`, `autor` e `ano`.  
> Implemente um método `exibir_info()` que imprime os dados do livro formatados.

### 🧠 Exemplo de saída:
```shell
Livro: Dom Casmurro  
Autor: Machado de Assis  
Ano: 1899
```
#### 💡 Desafio extra:
Adicione um método atrasado() na classe Livro, que verifica se o ano do livro é anterior a 2000
e retorna "Antigo" ou "Atual".

---

## 🧪 Teste os códigos você mesmo

Você pode testar os exemplos usados neste material clicando nos links abaixo:

- 📄 [Código: Classe `Tarefa`](./tarefa.py)
- 📄 [Código: Classe `Pessoa`](./pessoa_amizade.py)
- 📄 [Código: Resposta do Exercício `Livro`](./livro_exercicio.py)

💡 Esses arquivos estarão disponíveis na mesma pasta deste material.  
Você pode baixar, modificar e executar os exemplos no seu ambiente Python.

---

## 🔗 Dica de material complementar

- [Como Funcionam Classes e POO em Python (Hashtag Programação)](https://www.youtube.com/watch?v=97A_Cyyh-eU)
- [Documentação oficial – Python Classes](https://docs.python.org/3/tutorial/classes.html)

---
