# Lógica de Programação: Guia de Aprendizado e Prática

Este documento serve como material de apoio para as aulas de **Lógica de Programação**, abordando os conceitos fundamentais para o desenvolvimento do pensamento computacional e escrita de algoritmos.

---

## 1. Conteúdo Programático da Aula

*   **Introdução:** O que é lógica, algoritmos e pensamento computacional.
*   **Variáveis e Tipos de Dados:** Como o computador armazena informações na memória.
*   **Operadores:** Matemáticos, relacionais e lógicos.
*   **Estruturas de Decisão:** Controle de fluxo condicional (`Se-Senão`).
*   **Estruturas de Repetição:** Loops e laços de repetição (`Enquanto`, `Para`).

---

## 2. O que é um Algoritmo?

Um **algoritmo** é uma sequência finita de passos lógicos, claros e bem definidos que, quando seguidos, resolvem um problema ou executam uma tarefa específica.

### 📝 Exemplo Clássico: Algoritmo para Chupar uma Bala
1. Pegar a bala.
2. Retirar o papel da bala.
3. Colocar a bala na boca.
4. Jogar o papel no lixo.

---

## 3. Variáveis e Tipos de Dados

Uma **variável** é um espaço reservado na memória do computador para armazenar um dado que pode mudar durante a execução do programa. Cada variável deve possuir um nome (identificador) e um tipo.

### 📌 Tipos de Dados Primitivos
*   **Inteiro:** Números sem casas decimais. (Ex: `10`, `-5`, `0`).
*   **Real / Flutuante:** Números com casas decimais. (Ex: `10.5`, `3.1415`).
*   **Caracter / Texto:** Letras, palavras ou símbolos delimitados por aspas. (Ex: `"Ana"`, `"A"`, `"123"`).
*   **Lógico / Booleano:** Aceita apenas dois valores possíveis. (Ex: `Verdadeiro` ou `Falso`).

---

## 4. Operadores Básicos

Os operadores permitem manipular os valores das variáveis para realizar cálculos e testes lógicos.


| Categoria | Operadores | Significado |
| :--- | :--- | :--- |
| **Aritméticos** | `+`, `-`, `*`, `/`, `%` | Adição, Subtração, Multiplicação, Divisão, Resto da divisão |
| **Relacionais** | `>`, `<`, `>=`, `<=`, `==`, `!=` | Maior, Menor, Maior ou Igual, Menor ou Igual, Igual, Diferente |
| **Lógicos** | `E` (AND), `OU` (OR), `NÃO` (NOT) | Conjunção, Disjunção, Negação |

---

## 5. Estruturas de Decisão (Condicionais)

Permitem que o programa execute diferentes blocos de código com base em uma condição.

### 🔹 Estrutura Condicional Simples / Composta
```pseudocode
Se (idade >= 18) Entao
    Escreva("Você é maior de idade. Acesso permitido.")
Senao
    Escreva("Você é menor de idade. Acesso negado.")
FimSe
```

---

## 6. Estruturas de Repetição (Loops)

Utilizadas para executar o mesmo bloco de código várias vezes, até que uma condição de parada seja atingida.

### 🔹 Laço "Enquanto" (While)
Executa o bloco **enquanto** a condição for verdadeira. O teste lógico é feito no início.
```pseudocode
Inteiro contador = 1

Enquanto (contador <= 5) Faca
    Escreva(contador)
    contador = contador + 1 // Incremento para evitar loop infinito
FimEnquanto
```

### 🔹 Laço "Para" (For)
Utilizado quando já se sabe previamente a quantidade exata de repetições que serão realizadas.
```pseudocode
Para i de 1 Ate 5 Passo 1 Faca
    Escreva(i)
FimPara
```

---

## 7. Desafio Prático para a Aula 🚀

**Exercício:** Escreva um algoritmo (em pseudocódigo) que receba duas notas de um aluno, calcule a média aritmética e exiba se ele foi **Aprovado** (média maior ou igual a 7) ou **Reprovado** (média menor que 7).

### 💡 Resolução Esperada:
```pseudocode
Algoritmo "CalculaMedia"
Var
    nota1, nota2, media : Real
Inicio
    Escreva("Digite a primeira nota: ")
    Leia(nota1)
    Escreva("Digite a segunda nota: ")
    Leia(nota2)
    
    media <- (nota1 + nota2) / 2
    
    Escreva("Média final: ", media)
    
    Se (media >= 7.0) Entao
        Escreva(" Situação: APROVADO!")
    Senao
        Escreva(" Situação: REPROVADO!")
    FimSe
FimAlgoritmo
```
