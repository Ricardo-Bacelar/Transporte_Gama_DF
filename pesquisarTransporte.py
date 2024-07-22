

class TransporteEscolar:

    def __init__(self):
        self.setores_direcoes = {
            'gama oeste': {'Cef1': 'Tio Adalto, fone: 99999-1234', 'Cef2': 'Tio Carlos, fone: 96666-8888', 'Cef5':'Tia Sol', 'Sesc': 'Tio Reinaldo, fone: 98527-1910'},
            'gama leste': {'Cef1': 'Tio Fulano de tal, fone: 96666-5588', 'Cef2': 'Albertino da Silva, fone: 97777-8888'},
            'gama norte': {'Cef1': 'Tio Max, fone: 95555-7777', 'Sesc': 'Tio Reinaldo, fone: 98527-1910','Adventista':'Tio Reinaldo fone: 98527-1910'},
            'gama sul': {'Cef1': 'Abidias, fone: 91425-3698', 'Cef4': 'Tia Cilcano, fone 92222-1111', 'Sesc': 'Tio Reinaldo, fone: 98527-1910'},
            'gama central': {'Cef1': 'Joca, fone: 91233-4567', 'Cef4': 'Jairo, fone: 98877-4455', 'Sesc': 'Tio Reinaldo, fone: 98527-1910'},
            'residencial santos dumont' :{'Elite' : 'Tia Márcia, fone: 98497-1203','Sesi' : 'Tia Márcia, fone: 98497-1203', 
                            'Blue Scholl' : 'Tia Márcia, fone: 98497-1203', 'Adventista' : 'Tia Márcia, fone: 98497-1203',
                            'Cemi' : 'Tia Márcia, fone: 98497-1203', 'Cg': 'Tia Márcia, fone: 98497-1203 e Tio Zé Maria, Fone: 99100-6568', 'Sesc': 'Tia Márcia, fone: 98497-1203'},
            'ponte alta norte': {'Cef1': 'Tio Davis, fone: 92222-1111 e Filho Davis, fone: 93333-2222'}, 
            'novo gama':{'Cef1': 'Tio Jacaré, fone: 97777-3333',},
            'valparaiso':{'Cef1': 'Tio Jurandi, fone: 94444-3333',},
            'céu azul':{'Cef1': 'Tio Jamelão, fone: 96666-5555',},
            'lago azul':{'Cef1': 'Tio Tomate, fone: 96666-1111',},
                                           
            # Adicione mais direções e escolas conforme necessário
        }
    def solicitar_transporte(self, direcao, escola):
        direcao = direcao.lower()
        escola = escola.title()

        if direcao in self.setores_direcoes and escola in self.setores_direcoes[direcao]:
            motorista = self.setores_direcoes[direcao][escola]
            print(f"Transporte solicitado do(a) {direcao.upper()} em direção à {escola}.")
            print(f"O motorista que conduz do(a) {direcao.upper()} para {escola} é {motorista}.")
            # Adicione aqui a lógica adicional, como envio de notificação ao motorista, etc.
        else:
            print("Desculpe, a combinação de direção e escola informada não está disponível, verifique se os dados informados estão dentro do solicitado.")

# Exemplo de uso
if __name__ == "__main__":
    transporte = TransporteEscolar()

    direcao_usuario = input("Digite a cidade e o setor onde reside o aluno: ")
    escola_usuario = input("Digite a escola para onde você deseja o transporte: ")

    transporte.solicitar_transporte(direcao_usuario, escola_usuario)
input('Aperte enter para sair')
