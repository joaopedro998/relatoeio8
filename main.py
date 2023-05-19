from database import Database
from jogo import game
class Main:
    def __init__(self):
        self.db = Database("bolt://3.93.36.176:7687", "neo4j", "gear-goods-hunk")
        self.j1 = game(self.db)

    def menu(self):
        while True:
            print("----- MENU -----")
            print("1. Criar jogador")
            print("2. Atualizar jogador")
            print("3. Excluir jogador")
            print("4. Criar partida")
            print("5. Obter lista de jogadores")
            print("6. Obter informações sobre uma partida")
            print("7. Obter histórico de partidas de um jogador")
            print("8. Sair")
            opcao = input("Digite a opção desejada: ")

            if opcao == "1":
                self.criar_jogador()
            elif opcao == "2":
                self.atualizar_jogador()
            elif opcao == "3":
                self.excluir_jogador()
            elif opcao == "4":
                self.criar_partida()
            elif opcao == "5":
                self.obter_lista_jogadores()
            elif opcao == "6":
                self.obter_informacoes_partida()
            elif opcao == "7":
                self.obter_historico_jogador()
            elif opcao == "8":
                self.sair()
                break
            else:
                print("Opção inválida. Por favor, tente novamente.")

    def criar_jogador(self):
        jogador_id = input("Digite o ID do jogador: ")
        nome = input("Digite o nome do jogador: ")
        self.j1.criar_jogador(jogador_id, nome)
        print("Jogador criado com sucesso!")

    def atualizar_jogador(self):
        jogador_id = input("Digite o ID do jogador: ")
        nome = input("Digite o novo nome do jogador: ")
        self.j1.atualizar_jogador(jogador_id, nome)
        print("Jogador atualizado com sucesso!")

    def excluir_jogador(self):
        jogador_id = input("Digite o ID do jogador: ")
        self.j1.excluir_jogador(jogador_id)
        print("Jogador excluído com sucesso!")

    def criar_partida(self):
        partida_id = input("Digite o ID da partida: ")
        jogador_ids = input("Digite os IDs dos jogadores (separados por vírgula): ").split(",")
        resultado = input("Digite o resultado da partida: ")
        self.j1.criar_partida(partida_id, jogador_ids, resultado)
        print("Partida criada com sucesso!")

    def obter_lista_jogadores(self):
        jogadores = self.j1.obter_jogadores()
        print("Lista de jogadores:")
        for jogador in jogadores:
            print(jogador["p"]["nome"])

    def obter_informacoes_partida(self):
        partida_id = input("Digite o ID da partida: ")
        partida = self.j1.obter_partida(partida_id)
        if partida:
            print("Informações sobre a partida:")
            print("ID:", partida[0]["m"]["id"])
            print("Resultado:", partida[0]["m"]["resultado"])
            print("Participantes:")
            for jogador in partida[0]["jogadores"]:
                print(jogador["nome"])
        else:
            print("Partida não encontrada.")

    def obter_historico_jogador(self):
        jogador_id = input("Digite o ID do jogador: ")
        historico = self.j1.obter_historico_jogador(jogador_id)
        if historico:
            print("Histórico de partidas do jogador:")
            for partida in historico:
                print("ID:", partida["m"]["id"])
                print("Resultado:", partida["m"]["resultado"])
                print("---------------------")
        else:
            print("Jogador não encontrado ou sem histórico de partidas.")

    def sair(self):
        self.db.close()


# Execução do programa
if __name__ == "__main__":
    main = Main()
    main.menu()