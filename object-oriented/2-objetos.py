class Game:
    total_games = 0  # Contar número total de jogos

    def __init__(self, name="", year_launch=0, multiplayer=False, note=0):
        self.name = name
        self.year_launch = year_launch
        self.multiplayer = multiplayer
        self.note = note
        self.__total_evaluation = 0
        self.__evaluators = 0
        Game.total_games += 1

    def __str__(self):
        return f"Game: {self.name}"

    def technical_sheet(self):
        """
        verifica ficha técnica
        """
        print(
            f"Nome do jogos {self.name}\n"
            f"Ano de lançamento: {self.year_launch}.\n"
            f"Multiplayer:{self.multiplayer}.\nNota: {self.note}"
        )

    def evaluate(self, note):
        self.__total_evaluation += note
        self.__evaluators += 1

    def average(self):
        print(
            f"Média do filme: {self.name}: {self.__total_evaluation / self.__evaluators}"
        )


# Primeiro Jogo

game1 = Game(name="Brigandine", multiplayer=False, year_launch=1998, note=10)
# game1.name = "Brigandine"
# game1.multiplayer = False
# game1.yearLaunch = 1998
# game1.note = 10
game1.technical_sheet()

game1.evaluate(9.0)
game1.evaluate(7.5)
game1.average()

print(f"Total de jogos: {Game.total_games}")
