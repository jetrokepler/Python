from fpdf import FPDF

class PDF(FPDF):
    def adicionar_pagina(self):
        self.add_page()
        self.image('Imagens/Header do gerador de revisão.png', 0, 0, 210, 41)
        self.image('Imagens/Rodapé do gerador de revisão.png', 0, 288, 210, 9)

    def margens(self, left: float, top: float, right: float = -1):
        self.set_margins(left, top, right)

    def titulo(self):
        self.set_font('Arial', 'B', 16)
        self.set_text_color(0, 0, 0)
        self.cell(0, 0, 'Questões geradas com ChatGPT', ln = True, align = 'C')

    def adicionar_questoes(self, questao, num_questao):
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 4, f"[QUESTÃO {num_questao}] {questao}", border = 0, align='J', fill = False)
        self.image('Imagens/Header do gerador de revisão.png', 0, 0, 210, 41)
        self.image('Imagens/Rodapé do gerador de revisão.png', 0,288, 210, 9)
        self.ln(3)

    def salvar(self):
        self.output('Questões.pdf', 'F')