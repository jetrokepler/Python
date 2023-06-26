# Gerador de revisão para ENEM. 📘

### _Jetro Kepler, 2º Informática._

Este projeto consiste em um gerador de questões controladas, desenvolvido em Python utilizando o modelo ChatGPT 3.5 Turbo da OpenAI. O objetivo principal é fornecer uma ferramenta para criar uma revisão eficiente e abrangente para o Exame Nacional do Ensino Médio (ENEM). Acridito que este projeto possa ir mais longe e ser aplicado em salas de aula, pois tem se mostrado bastante eficiente.

O script é capaz de abrir o navegador automaticamente, e foi programado para abrir um site específico e coletar dados acerca de asssuntos que são abordados no ENEM, e, logo depois, as questões são geradas pelo modelo ChatGPT 3.5 Turbo de inteligência artificial, a partir dos dados coletados do site.

Espero que este código seja útil para a sua preparação e revisão do ENEM ou algum vestibular. Boa sorte em seus estudos!

## Funcionalidades

Geração automática de questões: O script utiliza o poder do modelo ChatGPT 3.5 Turbo para gerar questões de múltiplas perguntas relacionadas a diferentes disciplinas e fornecidas pelo currículo do ENEM.

Respostas e gabarito: Além de gerar as questões, o script também fornece as respostas correspondentes e um gabarito completo para auxiliar na correção e revisão.

Saída em formato de arquivo: O resultado final, contendo as questões, respostas e gabarito, é gerado em um arquivo de texto para facilitar o compartilhamento e impressão.

## Requsitos e como usar

Recomendo que certifique-se de ter uma versão recente do Python instalada em seu sistema, e que, dentro de um ambiente virtual tenha as seguintes bibliotecas instaladas:

- Selenium: Utilizada para interagir com páginas web e recolher as informações necessárias para a geração das questões.

- FPDF: Para gerar o arquivo de saída em formato PDF.

- Webdriver Manager: Facilita o gerenciamento dos drivers necessários para a execução do Selenium.

Certifique-se também que está conectado à internet.

Primeiro coloque dontro das aspas vazias no arquivo "OPENAI_API_KEY.py" sua chave da API da OpenAI, e depois execute o código, pois ele gerará um arquivo ".pkl" que será importado pelo arquivo "main.py".
Depois execute o arquivo "main.py", e se todos os requisitos estiverem ok, a mágica irá funcionar.