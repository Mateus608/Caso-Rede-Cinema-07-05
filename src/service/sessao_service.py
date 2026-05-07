from repository.sessao_repository import SessaoRepository

class SessaoService:

    def __init__(self):
        self.repository = SessaoRepository()

    def cadastrar_sessao(self, sessao):

        if not sessao.horario_inicio:
            raise Exception(
                "Horário inicial inválido"
            )

        if not sessao.horario_fim:
            raise Exception(
                "Horário final inválido"
            )

        self.repository.salvar(sessao)
