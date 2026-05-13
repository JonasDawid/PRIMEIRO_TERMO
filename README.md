# Resumo Integrado: Do Requisito ao Sistema Conectado

Este documento apresenta um resumo executivo que integra os conceitos fundamentais de Engenharia de Requisitos, Sistemas Operacionais, Lógica de Programação e Arquitetura IoT, demonstrando como essas disciplinas se conectam na construção de sistemas modernos.

---

## 1. Visão Geral da Integração das Disciplinas

Para construir qualquer solução de software ou hardware, seguimos um fluxo lógico de dependências:
1. **O Que Fazer?** (Engenharia de Requisitos) -> Define o escopo e as regras.
2. **Como Pensar?** (Lógica de Programação) -> Estrutura o raciocínio e os algoritmos para resolver o problema.
3. **Onde Executar?** (Sistemas Operacionais) -> Gerencia o hardware e provê o ambiente de execução para o código.
4. **Como Conectar ao Mundo?** (Arquitetura IoT) -> Estende o sistema para coletar dados do mundo físico através de redes distribuídas.

---

## 2. Pilares Fundamentais por Disciplina

### 📌 Engenharia de Requisitos
Focada em garantir que o sistema certo seja construído.
*   **Requisitos Funcionais (RF):** O comportamento esperado (Ex: "O sistema deve emitir um alerta se a temperatura exceder 40°C").
*   **Requisitos Não Funcionais (RNF):** As restrições de qualidade (Ex: "O alerta deve ser enviado em menos de 1 segundo").
*   **Técnicas de Elicitação:** Entrevistas para entender o cliente, Brainstorming para gerar ideias e Prototipagem para validar interfaces.

### 📌 Lógica de Programação
A base para a escrita de qualquer software através do pensamento computacional.
*   **Variáveis e Dados:** Armazenamento temporário de informações na memória.
*   **Estruturas Condicionais (`Se-Senão`):** Tomada de decisões com base em regras de negócio.
*   **Estruturas de Repetição (`Enquanto`, `Para`):** Automação de tarefas e processamento contínuo de dados.

### 📌 Sistemas Operacionais (SO)
O gerenciador invisível que dita a eficiência da execução do código no hardware.
*   **Kernel:** O núcleo que faz a ponte entre o software (algoritmo) e o hardware através de *System Calls*.
*   **Processos e Threads:** A unidade de execução dos algoritmos na CPU.
*   **Gerenciamento de Memória:** Paginação e memória virtual que evitam que uma aplicação interfira no espaço de outra.

### 📌 Arquitetura IoT (Internet das Coisas)
A expansão dos sistemas para o monitoramento e controle do ambiente físico.
*   **Camada de Percepção:** Onde sensores (capturam dados) e atuadores (executam ações físicas) operam.
*   **Distribuição de Processamento:** Decisão arquitetural entre processar na Borda (*Edge* para baixa latência) ou na Nuvem (*Cloud* para Big Data).
*   **Protocolos Leves:** Uso de comunicação eficiente como o MQTT (*Publish/Subscribe*) para economizar banda e energia.

---

## 3. Mapeamento de um Cenário Real: Telemetria Industrial

Para consolidar o resumo, veja como as quatro áreas interagem no desenvolvimento de um sistema de monitoramento de temperatura de máquinas:

