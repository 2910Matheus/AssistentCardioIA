# 🫀 Relatório do Projeto CardioIA – Fase 5

![Status](https://img.shields.io/badge/Status-Protótipo_Ativo-success)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-Backend-lightgrey)
![IBM Watson](https://img.shields.io/badge/IBM_Watson-Assistant-blueviolet)

## 📖 1. Introdução
Este repositório documenta o desenvolvimento do protótipo funcional do **Assistente Cardiológico Inteligente (CardioIA)**. O projeto foca na triagem primária e na experiência do paciente via Processamento de Linguagem Natural (NLP). O objetivo é simular um atendimento inicial de saúde cardiovascular, integrando inteligência artificial para capturar dados vitais, analisar riscos e fornecer orientações preventivas ou alertas de emergência de forma ágil e humanizada.

---

## 🧠 2. Arquitetura do Fluxo Conversacional
O assistente foi modelado utilizando a plataforma **IBM Watson Assistant (Dialog Skills)**, estruturado em uma árvore de decisão complexa para lidar com variáveis clínicas.

### 2.1 Intenções (Intents)
Foram definidas intenções para mapear as requisições do usuário com alta precisão:
- `#verificar_bpm` e `#verificar_pressao`: Identificam o desejo de analisar métricas numéricas.
- `#dor_no_peito`: Detecta relatos de desconforto torácico, ativando imediatamente o protocolo de urgência.
- `#sintomas_graves`: Reconhece sinais de alerta, como falta de ar, tontura e irradiação de dor.
- `#afirmacao` / `#negacao`: Gerenciam respostas binárias durante a anamnese digital.

### 2.2 Entidades e Variáveis de Contexto (Entities & Context)
O sistema utiliza entidades de sistema e variáveis para reter dados matemáticos:
- `@sys-number`: Entidade nativa do Watson utilizada para capturar os valores exatos de Frequência Cardíaca e Pressão Arterial.
- **Variáveis de Contexto (`$frequencia`, `$pressao_maxima`):** Armazenam os valores extraídos para permitir operações lógicas e condicionais (ex: `$frequencia > 100`) nos nós subsequentes.

### 2.3 Fluxo de Diálogo (Dialog Nodes)
O fluxo foi estruturado em formato de cascata (*Parent/Child*) para simular uma triagem médica:
1. **Saudação e Menu:** Apresentação das capacidades do bot (BPM, Pressão, Dor no Peito, Dicas).
2. **Protocolo de Emergência (Dor no Peito):** Avaliação de sintomas associados. Em caso positivo, o bot emite um alerta visual e orienta o acionamento do SAMU (192).
3. **Análise Quantitativa:** Solicitação de dados numéricos com o recurso de interrupção *Wait for user input*, processamento da variável e devolução do diagnóstico simulado (Normal, Baixo, Alto).
4. **Tratamento de Exceções (Fallback):** O nó *Anything Else* garante que o bot redirecione o usuário de volta ao escopo cardiológico em caso de entradas não reconhecidas.

---

## 💻 3. Implementação Técnica
A solução opera em um modelo cliente-servidor, dividida em duas camadas principais:

### 3.1 Backend (Python/Flask)
Desenvolvido em **Python** utilizando o microframework **Flask**, o backend atua como middleware entre a interface do usuário e a API da IBM Cloud. O script é responsável por:
- Gerenciar a autenticação via IAM.
- Manter a persistência da sessão do chat (garantindo que o Watson lembre o contexto e as variáveis salvas).
- Formatar as respostas (textos e botões de opções) recebidas via JSON.

### 3.2 Frontend (HTML/JS/CSS)
A interface web foi desenvolvida para ser responsiva e amigável. Utiliza **JavaScript (Fetch API)** para comunicação assíncrona via requisições POST com o backend, proporcionando uma experiência de chat em tempo real, sem recarregamento da página.

---

## 🚀 4. Conclusão
O protótipo do CardioIA comprova a viabilidade do uso de assistentes virtuais na triagem inicial de pacientes. A integração do Watson Assistant com o ecossistema Python/Flask resultou em uma aplicação escalável. A implementação de cálculos lógicos dentro do próprio diálogo e protocolos de segurança para sintomas graves elevam o projeto além de um simples chatbot, apresentando uma solução tecnológica aplicável e relevante para a saúde digital.

---
*Desenvolvido para a Fase 5 do projeto de Assistente Cardiológico Inteligente - FIAP.*
