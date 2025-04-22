[🏠 Voltar para o Início](../README.md)

# 📘 Tema 04 – Tratamento de Exceções

## 💥 O que é uma exceção?

Uma exceção é um erro que ocorre **durante a execução do programa**.  
Em vez de o programa parar completamente, podemos usar o tratamento de exceções para **lidar com o erro de forma controlada**.

---

### 🔍 Por que tratar exceções?

- Evita que o programa quebre do nada
- Permite personalizar mensagens de erro
- Melhora a experiência do usuário
- Facilita testes e manutenção

---

## 🧱 Sintaxe básica

```python
try:
    # código que pode gerar erro
    ...
except TipoDoErro:
    # o que fazer se der erro
    ...
else:
    # executa se NÃO der erro
    ...
finally:
    # executa sempre, com ou sem erro
    ...

```

## 📄 Exemplo prático

```python
def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Erro: divisão por zero não é permitida.")
    else:
        print(f"Resultado: {resultado}")
    finally:
        print("Fim da operação.")

dividir(10, 2)
dividir(5, 0)
```
## 🧪 Exercício Proposto

> Crie uma função chamada `ler_numero()` que solicita ao usuário um número inteiro.  
> Se o valor digitado for inválido, mostre uma mensagem de erro e peça novamente até funcionar.

---

### 💡 Desafio extra

> Crie uma função `sacar(valor, saldo)` que lança uma exceção (`raise`) se o valor for maior que o saldo disponível.  
> Trate essa exceção com `try/except` e exiba a mensagem “Saldo insuficiente”.

---

## ▶️ Teste o código

- 📄 [Código: `dividir`](./dividir.py)  
- 📄 [Resposta do Exercício `ler_numero`](./ler_numero.py)  
- 📄 [Desafio com `raise`](./sacar_valor.py)

---

## 🔗 Dica de material complementar

- [Curso Python #23 - Tratamento de Erros e Exceções – Curso em Vídeo](https://www.youtube.com/watch?v=xz2B3bfNjEk)  
- [Python Docs – Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)

