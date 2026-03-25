# Relatório do Projeto CardioIA – Fase 5: Assistente Cardiológico Inteligente

## 1. Introdução
Este relatório descreve o desenvolvimento do protótipo funcional do **Assistente Cardiológico Inteligente (CardioIA)**, focado na experiência do paciente e na comunicação via Processamento de Linguagem Natural (NLP). O objetivo é simular um atendimento inicial em saúde cardíaca, integrando serviços de IA conversacional com uma interface amigável.

## 2. Arquitetura do Fluxo Conversacional
O assistente foi modelado utilizando a plataforma **IBM Watson Assistant**, com foco em quatro pilares principais:

### 2.1 Intenções (Intents)
Foram definidas intenções para capturar o propósito das mensagens do usuário:
- `#saudacao`: Identifica o início da conversa.
- `#sintomas_dor_peito`: Detecta relatos de dor ou desconforto torácico.
- `#agendar_consulta`: Identifica o desejo do usuário em marcar um atendimento médico.
- `#despedida`: Reconhece o encerramento da interação.

### 2.2 Entidades (Entities)
As entidades ajudam a extrair informações específicas:
- `@sintoma`: Categoriza tipos de sintomas (dor no peito, palpitação, tontura).
- `@periodo`: Identifica preferências de horário para agendamento (manhã, tarde, noite).

### 2.3 Fluxo de Diálogo (Dialog Nodes)
O fluxo foi estruturado para ser empático e informativo:
1. **Boas-vindas**: O bot se apresenta e convida o usuário a interagir.
2. **Triagem Inicial**: Caso o usuário relate sintomas graves (dor no peito), o assistente faz perguntas de acompanhamento e sugere cautela.
3. **Encaminhamento**: O fluxo permite o agendamento simulado de consultas.
4. **Tratamento de Exceções**: Um nó "Anything Else" garante que o bot responda educadamente caso não entenda a entrada.

## 3. Implementação Técnica
A solução foi dividida em duas camadas principais:

### 3.1 Backend (Python/Flask)
Desenvolvido em Python utilizando o framework **Flask**, o backend atua como um middleware entre a interface do usuário e a API do IBM Watson. Ele gerencia as sessões de chat e processa as respostas do serviço de NLP.

### 3.2 Frontend (HTML/JS)
Uma interface web responsiva foi criada para permitir a interação em tempo real. Utilizou-se **Bootstrap** para o design e **JavaScript (Fetch API)** para a comunicação assíncrona com o backend, proporcionando uma experiência de chat fluida.

## 4. Conclusão
O protótipo demonstra a viabilidade de assistentes virtuais na triagem inicial de pacientes cardiológicos. A integração de técnicas de NLP permite uma comunicação mais humana e eficiente, respeitando as boas práticas de saúde digital discutidas ao longo da fase.

---
**Equipe:** [Nomes dos Integrantes]
**Curso:** [Nome do Curso]
**Instituição:** [Nome da Instituição]
