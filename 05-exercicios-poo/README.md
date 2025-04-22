[🏠 Voltar para o Início](../README.md)
# 📘 Tema 05 – Exercícios de POO

Esta seção contém exercícios para reforçar os conceitos de Programação Orientada a Objetos em Python.

Cada exercício traz uma situação prática que envolve:
- Criação de classes
- Atributos públicos e privados
- Métodos com retorno
- Encapsulamento usando `@property`
- Validações com `if`, `raise` e `try/except`

Tente resolver os exercícios antes de ver a solução. Todos os exemplos possuem arquivos `.py` com a resolução comentada.

---

## 1️⃣ Livraria

Crie uma classe chamada `Livro` com os seguintes atributos:

- `titulo`
- `autor`
- `preco`

### Regras:
- O preço deve ser acessado usando `@property`
- Se alguém tentar definir um valor negativo, deve exibir:  
  `"❌ Preço inválido!"`

### Métodos:
- `exibir_info()`: mostra os dados do livro formatados  

📄 [Ver solução](./livraria.py)

---

## 2️⃣ Aluno

Crie a classe `Aluno` com os seguintes atributos:

- `nome`
- `nota1`, `nota2`

### Métodos:
- `media()`: retorna a média das duas notas
- `situacao()`: retorna um texto de acordo com a média:
  - `"Aprovado"` (média >= 7)
  - `"Recuperação"` (média >= 5 e < 7)
  - `"Reprovado"` (média < 5)

📄 [Ver solução](./aluno.py)

---

## 3️⃣ Elevador

Crie uma classe `Elevador` com:

- `capacidade`: número máximo de pessoas
- `pessoas`: número atual

### Métodos:
- `entrar()`: adiciona uma pessoa, mas **não ultrapassa a capacidade**
- `sair()`: remove uma pessoa, **não pode ser menor que 0**

📄 [Ver solução](./elevador.py)

---

## 4️⃣ Conta Digital

Crie a classe `ContaDigital` com os atributos:

- `titular`
- `saldo`

### Métodos:
- `depositar(valor)`: adiciona ao saldo (não permite valores negativos ou zero)
- `sacar(valor)`: remove valor do saldo (não permite sacar mais do que tem)
- `exibir()`: mostra nome e saldo

### Regras:
- Use `raise ValueError()` nas validações
- Trate os erros com `try/except`

📄 [Ver solução](./conta_digital.py)

---

## 5️⃣ Agenda

Crie duas classes:

### `Contato`:
- `nome`
- `telefone`

### `Agenda`:
- Uma lista de contatos
- Métodos:
  - `adicionar(contato)`
  - `listar()`
  - `buscar(nome)` — retorna o contato ou lança erro
Use `raise LookupError()` e trate com `try/except`.

📄 [Ver solução](./agenda.py)

---

## 🧠 Desafio extra (opcional)

Pegue qualquer exercício acima e:

- Aplique `@property` e `@setter` para encapsular algum atributo
- Adicione tratamento de exceções com `try/except`
- Faça uma versão com entrada de dados via `input()`

---
