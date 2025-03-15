from tkinter import *
import clima

class Aplicacao:
    def __init__(self):

        self.layout = Tk()

        self.layout.title("Captador de Temperatura e Umidade")

        self.layout.geometry("400x200")

        self.tela = Frame(self.layout)

        self.descricao = Label(self.tela, text="Buscar Clima de São Paulo")
        self.descricao.pack(pady=30) 

        self.exportar = Button(self.tela, text="Buscar Previsão", command=self.buscar_previsao,)
        self.exportar.pack(pady=10) 

        self.tela.pack()
        self.descricao.pack()
        self.exportar.pack()
    
        mainloop()

    def buscar_previsao(self):
        dados = clima.capturar_dados_clima("São Paulo")
        if dados:
            clima.salvar_dados_em_xlsx(dados)
            print("Dados salvos em clima.xlsx")
        else:
            print("Cidade não encontrada ou dados não disponíveis")
            
tl = Aplicacao()