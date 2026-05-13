# Engenharia de Requisitos: Guia de Estudo e Prática

Este documento serve como material de apoio para as aulas de **Levantamento, Análise e Especificação de Requisitos**, abordando desde conceitos fundamentais até técnicas de elicitação e documentação técnica.

---

## 1. Conteúdo Programático da Aula

*   **Introdução:** O que é Engenharia de Requisitos e sua importância no ciclo de software.
*   **Classificação:** Diferenciação entre Requisitos Funcionais (RF) e Não Funcionais (RNF).
*   **Elicitação:** Técnicas práticas para descobrir as reais necessidades do cliente.
*   **Modelagem:** Tradução de necessidades em Diagramas visuais.
*   **Documentação:** Estruturação de Relatórios Técnicos e especificações.

---

## 2. Requisitos Funcionais (RF) vs. Não Funcionais (RNF)

A correta classificação dos requisitos garante que o sistema faça o que é esperado com a qualidade necessária.

### 📌 Requisitos Funcionais (RF)
Definem as funções, ações e serviços que o sistema deve executar. Representam o **comportamento** e o que o sistema **faz**.
*   **RF01 - Cadastro de Usuários:** O sistema deve permitir o registro de novos usuários informando Nome, E-mail e CPF.
*   **RF02 - Autenticação:** O sistema deve validar as credenciais de login via integração com o Google OAuth.
*   **RF03 - Emissão de Recibo:** O sistema deve gerar um comprovante financeiro automaticamente após cada transação confirmada.

### 📌 Requisitos Não Funcionais (RNF)
Definem as características de qualidade, restrições, premissas e propriedades de desempenho. Representam **como** o sistema deve operar.
*   **RNF01 - Desempenho:** O sistema deve processar as consultas de busca em menos de 1,5 segundos sob carga normal.
*   **RNF02 - Segurança:** Todas as senhas de usuários armazenadas no banco de dados devem ser criptografadas usando o algoritmo bcrypt.
*   **RNF03 - Disponibilidade:** O sistema deve possuir uma taxa de disponibilidade (uptime) de 99,9% em base anual.

---

## 3. Técnicas de Elicitação de Requisitos

Abaixo estão as três principais técnicas práticas abordadas nesta disciplina para extrair informações dos *stakeholders*:

### 🗣️ 1. Entrevistas
Conversas diretas (estruturadas, semiestruturadas ou livres) com os usuários.
*   **Vantagem:** Permite aprofundar em dores específicas e capturar nuances operacionais.
*   **Dica Prática:** Evite perguntas indutivas. Em vez de *"Você quer um botão de busca aqui?"*, pergunte *"Como você localiza uma informação hoje?"*.

### 🧠 2. Brainstorming
Sessões dinâmicas de tempestade de ideias com a equipe de desenvolvimento e clientes.
*   **Objetivo:** Gerar o maior volume possível de ideias e soluções inovadoras sem julgamentos iniciais.
*   **Fluxo de Execução:** 
    1. Definição do problema central.
    2. Fase de ideação livre (registro de todas as ideias).
    3. Fase de filtragem, agrupamento e priorização das melhores propostas.

### 📐 3. Prototipagem
Criação de modelos visuais (wireframes de baixa fidelidade ou telas interativas de alta fidelidade) antes do desenvolvimento do código.
*   **Importância:** Reduz falhas de comunicação. O cliente consegue enxergar a dinâmica do sistema e validar o fluxo de navegação de forma antecipada.

---

## 4. Diagramas na Engenharia de Requisitos

Os diagramas traduzem os requisitos textuais em modelos visuais compreensíveis para desenvolvedores e clientes. Os dois mais comuns são:

### 🔹 Diagrama de Casos de Uso (UML)
Mapeia os atores (usuários/sistemas) e suas interações com as funcionalidades do sistema.

