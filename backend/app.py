import os
from flask import Flask, request, jsonify, render_template
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

app = Flask(__name__)

# Configurações do Watson Assistant (a serem preenchidas pelo usuário)
API_KEY = os.environ.get('WATSON_API_KEY', '')
SERVICE_URL = os.environ.get('WATSON_SERVICE_URL', '')
ENVIRONMENT_ID = os.environ.get('WATSON_ENVIRONMENT_ID', '')
ASSISTANT_ID = os.environ.get("WATSON_ASSISTANT_ID", "")

session_id_global = None

try:
    authenticator = IAMAuthenticator(API_KEY)
    assistant = AssistantV2(version='2021-06-14', authenticator=authenticator)
    assistant.set_service_url(SERVICE_URL)
except Exception as e:
    print(f"Erro: {e}")

def get_session():
    global session_id_global
    if session_id_global is None:
        try:
            res = assistant.create_session(assistant_id=ENVIRONMENT_ID, environment_id=ENVIRONMENT_ID).get_result()
            session_id_global = res['session_id']
        except: return None
    return session_id_global

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message', methods=['POST'])
def message():
    global session_id_global
    user_input = request.json.get('message', '')
    sid = get_session()
    
    try:
        response = assistant.message(
            assistant_id=ENVIRONMENT_ID,
            environment_id=ENVIRONMENT_ID,
            session_id=sid,
            user_id='matheus_fiap',
            input={
                'message_type': 'text',
                'text': user_input,
                'options': {'return_context': True} # CRUCIAL: Mantém a variável $frequencia
            }
        ).get_result()

        output = response.get('output', {})
        generic = output.get('generic', [])
        
        respostas = []
        if generic:
            for item in generic:
                if item.get('response_type') == 'text':
                    respostas.append(item.get('text'))
                elif item.get('response_type') == 'option':
                    if item.get('title'): respostas.append(item.get('title'))
                    for opt in item.get('options', []):
                        respostas.append(f"• {opt['label']}")
            
            return jsonify({'response': "\n".join(respostas), 'source': 'Watson'})
        
        return jsonify({'response': "O Watson não retornou resposta.", 'source': 'Watson'})

    except Exception as e:
        session_id_global = None
        return jsonify({'response': "Sessão expirada. Tente novamente.", 'source': 'Retry'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
