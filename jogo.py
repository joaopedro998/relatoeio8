class game:
    def __init__(self, database):
        self.db = database

    def criar_jogador(self, jogador_id, nome):
        query = "CREATE (:Player {id: $jogador_id, nome: $nome})"
        parameters = {"jogador_id": jogador_id, "nome": nome}
        self.db.execute_query(query, parameters)

    def atualizar_jogador(self, jogador_id, nome):
        query = "MATCH (p:Player {id: $jogador_id}) SET p.nome = $nome"
        parameters = {"jogador_id": jogador_id, "nome": nome}
        self.db.execute_query(query, parameters)

    def excluir_jogador(self, jogador_id):
        query = "MATCH (p:Player {id: $jogador_id}) DETACH DELETE p"
        parameters = {"jogador_id": jogador_id}
        self.db.execute_query(query, parameters)

    def criar_partida(self, partida_id, jogador_ids, resultado):
        query = """
        MATCH (players:Player)
        WHERE players.id IN $jogador_ids
        CREATE (m:Match {id: $partida_id, resultado: $resultado})
        CREATE (m)-[:PARTICIPANTE]->(players)
        """
        parameters = {"partida_id": partida_id, "jogador_ids": jogador_ids, "resultado": resultado}
        self.db.execute_query(query, parameters)

    def obter_jogadores(self):
        query = "MATCH (p:Player) RETURN p"
        return self.db.execute_query(query)

    def obter_partida(self, partida_id):
        query = """
        MATCH (m:Match {id: $partida_id})
        MATCH (m)-[:PARTICIPANTE]->(p:Player)
        RETURN m, collect(p) AS jogadores
        """
        parameters = {"partida_id": partida_id}
        return self.db.execute_query(query, parameters)

    def obter_historico_jogador(self, jogador_id):
        query = """
        MATCH (p:Player {id: $jogador_id})
        MATCH (m:Match)-[:PARTICIPANTE]->(p)
        RETURN m
        """
        parameters = {"jogador_id": jogador_id}
        return self.db.execute_query(query, parameters)
