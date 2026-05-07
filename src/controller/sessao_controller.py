from model.sessao import Sessao
from service.sessao_service import SessaoService

class SessaoController:

    def __init__(self):
        self.service = SessaoService()

    def cadastrar_sessao(
        self,
        horario_inicio,
        horario_fim
    ):

        sessao = Sessao(
            horario_inicio,
            horario_fim
        )

        self.service.cadastrar_sessao(sessao)

        print("\nSessão cadastrada com sucesso!")
