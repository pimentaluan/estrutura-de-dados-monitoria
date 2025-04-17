# 📘 Tema 03 – Encapsulamento

## 🔒 O que é encapsulamento?

Encapsulamento é um dos pilares da Programação Orientada a Objetos. Ele consiste em **esconder os detalhes internos** de um objeto (como seus atributos e a forma como ele faz certas operações), expondo apenas o necessário para quem vai usar.

---

### 🧠 Mas pra que encapsular?

A ideia principal é **proteger os dados** de acessos e modificações indevidas.  
Ao encapsular, você controla **como e quando** alguém pode alterar o estado de um objeto, o que ajuda a manter a integridade do programa.

---

### 🛡️ Vantagens do encapsulamento:

- Evita que dados sejam modificados de forma incorreta ou acidental
- Permite aplicar regras ou validações antes de aceitar um valor
- Torna o código mais seguro, organizado e fácil de manter
- Ajuda a manter a lógica de negócio **dentro da classe** (coesa)
- Facilita alterações futuras sem quebrar outras partes do sistema

---

## 🔍 Níveis de visibilidade em Python

| Tipo         | Prefixo    | Acesso                          |
|--------------|------------|----------------------------------|
| Público      | `self.nome`     | Acessível normalmente           |
| Protegido    | `self._nome`    | Sinaliza que **deveria** ser interno |
| Privado      | `self.__nome`   | Oculto fora da classe (name mangling) |

---

## 📄 Exemplo prático

```python
class Conta:
    def __init__(self, titular, saldo):
        self.__titular = titular     # privado
        self.__saldo = saldo         # privado

    def exibir_saldo(self):
        print(f"{self.__titular}, seu saldo é R${self.__saldo:.2f}")

    def sacar(self, valor):
        if valor > self.__saldo:
            print("Saldo insuficiente.")
        else:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado.")
```
---

## 👀 Tentando acessar diretamente de fora:

```python
conta = Conta("Luan", 1000)

# Isso vai funcionar:
conta.exibir_saldo()

# Isso NÃO vai funcionar:
print(conta.__saldo)  # AttributeError

# Mas você pode "forçar" com:
print(conta._Conta__saldo)  # Acesso por name mangling (NÃO recomendado)
```

## ✅ Vantagens do encapsulamento

- Protege os dados  
- Evita alterações diretas não autorizadas  
- Permite controle sobre o acesso com métodos (`get` / `set`)  
- Deixa o código mais confiável e fácil de manter  

---

## 🧪 Exercício Proposto

> Crie uma classe `Produto` com os atributos privados `nome` e `preco`.  
> Implemente:
>
> - Um método `exibir()` que mostra nome e preço  
> - Um método `aplicar_desconto(percentual)` que reduz o preço proporcionalmente  
> - Uma validação no desconto (não aplicar se for maior que 50%)

---

### 💡 Desafio extra

> Use `@property` e `@<atributo>.setter` para permitir acessar e modificar o preço com validação.  
> Por exemplo: o novo preço não pode ser negativo.

---

## ▶️ Teste o código

- 📄 [Código: `Conta`](./conta_encapsulada.py)  
- 📄 [Resposta do Exercício `Produto`](./produto_exercicio.py)

---

## 🔗 Dica de material complementar

- [Orientação a objetos: Encapsulamento (PETEE UFMG)](https://www.youtube.com/watch?v=rw0uP9yNFCU)  
- [Python Docs – Classes e Atributos](https://docs.python.org/3/tutorial/classes.html#private-variables)
