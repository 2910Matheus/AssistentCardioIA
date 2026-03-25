import os
from flask import Flask, request, jsonify, render_template
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

app = Flask(__name__)

# Configurações do Watson Assistant (a serem preenchidas pelo usuário)
API_KEY = os.environ.get('WATSON_API_KEY', 'YOUR_API_KEY_HERE')
SERVICE_URL = os.environ.get('WATSON_SERVICE_URL', 'YOUR_SERVICE_URL_HERE')
ASSISTANT_ID = os.environ.get('WATSON_ASSISTANT_ID', 'YOUR_ASSISTANT_ID_HERE')

# Inicialização do Watson Assistant
try:
    authenticator = IAMAuthenticator(API_KEY)
    assistant = AssistantV2(
        version='2021-06-14',
        authenticator=authenticator
    )
    assistant.set_service_url(SERVICE_URL)
    session_id = None
except Exception as e:
    print(f"Erro ao configurar Watson: {e}")
    assistant = None

def get_session_id():
    global session_id
    if assistant:
        try:
            response = assistant.create_session(assistant_id=ASSISTANT_ID).get_result()
            return response['session_id']
        except Exception as e:
            print(f"Erro ao criar sessão: {e}")
            return None
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message', methods=['POST'])
def message():
    user_input = request.json.get('message', '')
    
    # Se o Watson não estiver configurado, simulamos uma resposta (Mock)
    if not assistant or API_KEY == 'YOUR_API_KEY_HERE':
        return jsonify({
            'response': f"Simulação: Você disse '{user_input}'. (Configure as chaves do Watson para integração real.)",
            'source': 'Mock/Simulação'
        })

    try:
        global session_id
        if not session_id:
            session_id = get_session_id()

        response = assistant.message(
            assistant_id=ASSISTANT_ID,
            session_id=session_id,
            input={'text': user_input}
        ).get_result()

        # Extraindo o texto da resposta
        generic = response['output'].get('generic', [])
        if generic:
            reply = generic[0].get('text', 'Não entendi.')
        else:
            reply = "Desculpe, não consegui processar sua mensagem."

        return jsonify({'response': reply, 'source': 'Watson Assistant'})
    except Exception as e:
        # Tenta resetar sessão em caso de erro (ex: sessão expirada)
        session_id = None
        return jsonify({'response': f"Ocorreu um erro na comunicação: {str(e)}", 'source': 'Error'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
