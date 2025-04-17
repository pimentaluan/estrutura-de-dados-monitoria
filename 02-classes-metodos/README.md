[🏠 Voltar para o Início](../README.md)
# 📘 Tema 02 – Classes, Métodos e Atributos

## 🧠 O que são classes, métodos e atributos?

Na Programação Orientada a Objetos, uma **classe** é como um molde.  
**Atributos** são as características (dados) e **métodos** são as ações (funções) que os objetos dessa classe podem realizar.

---

### 🧱 Exemplo prático (Python)

```python
class ContaBancaria:
    taxa_juros = 0.02  # atributo de classe

    def __init__(self, titular, saldo):
        self.titular = titular     # atributo de instância
        self.saldo = saldo         # atributo de instância

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")

    def exibir_saldo(self):
        print(f"Titular: {self.titular} | Saldo: R${self.saldo:.2f}")

    @staticmethod
    def banco():
        return "Banco Python"

    @classmethod
    def alterar_juros(cls, nova_taxa):
        cls.taxa_juros = nova_taxa
```

#### 🧪 Usando a classe

```python
conta1 = ContaBancaria("Luan", 500)
conta1.exibir_saldo()

conta1.depositar(200)

print("Banco:", ContaBancaria.banco())
print("Taxa atual:", ContaBancaria.taxa_juros)
ContaBancaria.alterar_juros(0.03)
print("Nova taxa:", ContaBancaria.taxa_juros)

```

## 🔍 Explicação dos tipos de métodos

| Tipo             | Exemplo              | Quando usar                           |
|------------------|----------------------|----------------------------------------|
| Método comum     | `def sacar(self)`    | Usa atributos do próprio objeto        |
| Método de classe | `@classmethod`       | Modifica/usa a classe, não o objeto    |
| Método estático  | `@staticmethod`      | Função independente dentro da classe   |

---

## 🧪 Exercício Proposto

> Crie uma classe `Carro` com os atributos `modelo`, `ano` e `velocidade_atual`.  
> Implemente os métodos:
> 
> - `acelerar(valor)` → aumenta a velocidade  
> - `frear(valor)` → diminui a velocidade (não pode ser menor que 0)  
> - `exibir_velocidade()` → imprime a velocidade atual  

### 🧠 Exemplo de saída:
```shell
Carro: Uno | Ano: 2015  
Velocidade atual: 40 km/h
```
### 💡 Desafio extra

> Crie um atributo de classe `limite_velocidade` e, ao acelerar, limite a velocidade ao máximo permitido.  
> Exemplo: se o limite for 180 km/h e o carro tentar passar disso, mantenha no 180.

---

## ▶️ Teste o código

- 📄 [Código: `ContaBancaria`](./conta_bancaria.py)
- 📄 [Resposta do Exercício `Carro`](./carro_exercicio.py)

---

## 🔗 Dica de material complementar

- [(Grande mas bem detalhado) Como Sair do Zero em Classes no Python - Self e Init Explicados](https://www.youtube.com/watch?v=gomDSZaay3E)
- [Python Classes e Métodos – Dev Aprender](https://www.youtube.com/watch?v=j6B8shHXzks)
- [Documentação oficial – Python Classes](https://docs.python.org/3/tutorial/classes.html)
