import openai
import gradio as gr
from gradio import components

with open("OPENAI_API_KEY.txt") as file:
    openai.api_key = file.read()

messages = [{"role": "system", "content": "You are a financial experts that specializes in real estate investment and negotiation"}]

def CustomChatGPT(user_input): #Esse método envia as mensagens acumuladas na lista messages até o momento para o modelo de linguagem GPT-3.5-turbo e obtém uma resposta gerada pelo modelo. 
    # A entrada do usuário (user_input) está sendo fornecida automaticamente pela gradio quando o usuário digitar uma mensagem na interface.

    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )

    # Para extrair o conteúdo da resposta, usamos a notação de acesso ao dicionário. Aqui está a decomposição passo a passo:

    # 1 - response["choices"]: A chave "choices" no dicionário response contém uma lista de escolhas geradas pelo modelo. Cada escolha possui informações como a mensagem gerada e sua avaliação.
    # 2 - [0]: Acessamos o primeiro elemento dessa lista de escolhas. Geralmente, apenas uma escolha é retornada pelo modelo, mas poderia haver várias opções se configuradas assim.
    # 3 - ["message"]: A chave "message"no dicionário da escolha contém informações sobre a mensagem gerada.
    # 4 - ["content"]: A chave "content"dentro do dicionário da mensagem contém o conteúdo real da mensagem gerada pelo chatbot.

    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

descricao_input = "Faça sua pergunta aqui:"
descricao_output = 'Bot "marketeiro":'

inputs = components.Textbox(label = descricao_input)
outputs = components.Textbox(label = descricao_output)

link = "https://github.com/jetrokepler/Python/tree/main/IA"

gr.Interface(
    fn = CustomChatGPT, 
    inputs = inputs, 
    outputs = outputs, 
    title = "Chatbot de negócios construido por Jetro Kepler - 2º Informática.",
    allow_flagging = "never",
    description = f"O chatbot foi treinado com o objetivo de fornecer respostas relacionadas a marketing e dicas de negócios. Ele utiliza o modelo GPT-3.5-turbo da OpenAI para gerar respostas com base nas mensagens fornecidas pelo usuário.\nPara mais informações e o código completo, você pode acessar o repositório no GitHub: Link para o Repositório no GitHub: {link}"
    ).launch(share = True)