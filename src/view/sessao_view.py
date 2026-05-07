from controller.sessao_controller import SessaoController

class SessaoView:

    def __init__(self):
        self.controller = SessaoController()

    def menu(self):

        print("===== CADASTRO DE SESSÃO =====")

        horario_inicio = input(
            "Digite o horário de início: "
        )

        horario_fim = input(
            "Digite o horário de término: "
        )

        self.controller.cadastrar_sessao(
            horario_inicio,
            horario_fim
        )
