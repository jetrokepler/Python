import pickle

openai_api_key = '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'

nome_do_arquivo = "OPENAI_API_KEY.pkl"

# Salva a variável no arquivo
with open(nome_do_arquivo, "wb") as arquivo:
    pickle.dump(openai_api_key, arquivo)