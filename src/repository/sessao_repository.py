from repository.connection_factory import ConnectionFactory

class SessaoRepository:

    def salvar(self, sessao):

        conexao = ConnectionFactory.get_connection()

        cursor = conexao.cursor()

        sql = """
        INSERT INTO sessao
        (horario_inicio, horario_fim, publico)
        VALUES (?, ?, ?)
        """

        cursor.execute(sql, (
            sessao.horario_inicio,
            sessao.horario_fim,
            sessao.publico
        ))

        conexao.commit()
        conexao.close()
