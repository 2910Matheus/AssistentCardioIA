# CardioIA - Assistente Cardiológico Inteligente (Fase 5)

Este repositório contém o protótipo funcional do **Assistente Cardiológico Conversacional (Chatbot)**, desenvolvido para a Fase 5 do projeto CardioIA.

## 🚀 Estrutura do Projeto

O projeto está organizado da seguinte forma:

- `/backend`: Código-fonte do servidor em Python (Flask).
- `/backend/templates`: Interface web (HTML/CSS/JS).
- `/docs`: Documentação e relatório explicativo do projeto.
- `assistant_workspace.json`: Arquivo de exportação do IBM Watson Assistant com as intents, entities e dialog nodes configurados.

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python 3.x, Flask.
- **NLP:** IBM Watson Assistant API.
- **Frontend:** HTML5, CSS3 (Bootstrap 5), JavaScript.

## 📋 Como Executar

1.  **Pré-requisitos:**
    - Python 3 instalado.
    - Instalar as dependências: `pip install flask ibm-watson ibm-cloud-sdk-core`.

2.  **Configuração do Watson:**
    - Importe o arquivo `assistant_workspace.json` para o seu IBM Watson Assistant.
    - Obtenha sua `API_KEY`, `SERVICE_URL` e `ASSISTANT_ID`.

3.  **Configurar Variáveis de Ambiente:**
    - No arquivo `backend/app.py`, substitua as chaves ou configure-as como variáveis de ambiente:
      ```bash
      export WATSON_API_KEY='sua_chave'
      export WATSON_SERVICE_URL='sua_url'
      export WATSON_ASSISTANT_ID='seu_id'
      ```

4.  **Iniciar o Servidor:**
    - Execute: `python backend/app.py`.
    - Acesse `http://localhost:5000` no seu navegador.

## 👥 Equipe
- Matheus Augusto Rodrigues Maia - RM560683
- Matheus Conciani - RM559473

## Apresentção do projeto
[CardioIA Aprensentação](https://www.youtube.com/watch?v=tZzjODVdYG4)
---
*Este projeto foi desenvolvido para fins acadêmicos, simulando um atendimento inicial em saúde.*
