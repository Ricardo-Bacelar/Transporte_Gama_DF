import tkinter as tk
from tkinter import ttk, messagebox

class TransporteEscolar:

    def __init__(self):
        self.setores_direcoes = {
            'gama oeste': {'Cef1': 'Tio Adalto, fone: 99999-1234', 'Cef2': 'Tio Carlos, fone: 96666-8888', 'Cef5':'Tia Sol', 'Sesc': 'Tio Reinaldo, fone: 98527-1910'},
            'gama leste': {'Cef1': 'Tio Fulano de tal, fone: 96666-5588', 'Cef2': 'Albertino da Silva, fone: 97777-8888'},
            'gama norte': {'Cef1': 'Tio Max, fone: 95555-7777', 'Sesc': 'Tio Reinaldo, fone: 98527-1910','Adventista':'Tio Reinaldo fone: 98527-1910'},
            'gama sul': {'Cef1': 'Abidias, fone: 91425-3698', 'Cef4': 'Tia Ciclano, fone 92222-1111', 'Sesc': 'Tio Reinaldo, fone: 98527-1910'},
            'gama central': {'Cef1': 'Joca, fone: 91233-4567', 'Cef4': 'Jairo, fone: 98877-4455', 'Sesc': 'Tio Reinaldo, fone: 98527-1910'},
            'residencial santos dumont' :{'Elite' : 'Tia Márcia, fone: 98497-1203','Sesi' : 'Tia Márcia, fone: 98497-1203', 
                            'Blue Scholl' : 'Tia Márcia, fone: 98497-1203', 'Adventista' : 'Tia Márcia, fone: 98497-1203',
                            'Cemi' : 'Tia Márcia, fone: 98497-1203', 'Cg': 'Tia Márcia, fone: 98497-1203 e Tio Zé Maria, Fone: 99100-6568', 'Sesc': 'Tia Márcia, fone: 98497-1203'},
            'ponte alta norte': {'Cef1': 'Tio Davis, fone: 92222-1111 e Filho Davis, fone: 93333-2222'}, 
            'novo gama':{'Cef1': 'Tio Jacaré, fone: 97777-3333',},
            'valparaiso':{'Cef1': 'Tio Jurandi, fone: 94444-3333',},
            'céu azul':{'Cef1': 'Tio Jamelão, fone: 96666-5555',},
            'lago azul':{'Cef1': 'Tio Tomate, fone: 96666-1111',},
            'pedregal':{'Cef1': 'Tio Simoneide, fone: 96666-2222',},
                                           
            # Adicione mais direções e escolas conforme necessário
        }

    def solicitar_transporte(self, direcao, escola):
        direcao = direcao.lower()
        escola = escola.title()

        if direcao in self.setores_direcoes and escola in self.setores_direcoes[direcao]:
            motorista = self.setores_direcoes[direcao][escola]
            return f"Transporte solicitado do(a) {direcao.upper()} em direção à {escola}.\nO motorista que conduz do(a) {direcao.upper()} para {escola} é {motorista}."
        else:
            return "Desculpe, a combinação de direção e escola informada não está disponível, verifique se os dados informados estão dentro do solicitado."

class TransporteEscolarApp:

    def __init__(self, root):
        self.transporte_escolar = TransporteEscolar()

        self.root = root
        self.root.title("Transporte Escolar")

        # Direção
        self.lbl_direcao = tk.Label(root, text="Cidade e setor onde reside o aluno:")
        self.lbl_direcao.grid(row=0, column=0, padx=10, pady=10)
        
        self.cbo_direcao = ttk.Combobox(root, values=list(self.transporte_escolar.setores_direcoes.keys()))
        self.cbo_direcao.grid(row=0, column=1, padx=10, pady=10)

        # Escola
        self.lbl_escola = tk.Label(root, text="Escola para onde você deseja o transporte:")
        self.lbl_escola.grid(row=1, column=0, padx=10, pady=10)
        
        self.cbo_escola = ttk.Combobox(root)
        self.cbo_escola.grid(row=1, column=1, padx=10, pady=10)
        
        self.cbo_direcao.bind("<<ComboboxSelected>>", self.update_escolas)

        # Botão solicitar
        self.btn_solicitar = tk.Button(root, text="Solicitar Transporte", command=self.solicitar_transporte)
        self.btn_solicitar.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def update_escolas(self, event):
        direcao = self.cbo_direcao.get().lower()
        if direcao in self.transporte_escolar.setores_direcoes:
            escolas = list(self.transporte_escolar.setores_direcoes[direcao].keys())
            self.cbo_escola['values'] = escolas

    def solicitar_transporte(self):
        direcao = self.cbo_direcao.get()
        escola = self.cbo_escola.get()
        mensagem = self.transporte_escolar.solicitar_transporte(direcao, escola)
        messagebox.showinfo("Solicitação de Transporte", mensagem)

if __name__ == "__main__":
    root = tk.Tk()
    app = TransporteEscolarApp(root)
    root.mainloop()
