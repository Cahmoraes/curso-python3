class Game:
    total_games = 0  # Contar número total de jogos

    def __init__(
        self,
        name: str = "",
        year_launch: int = 0,
        multiplayer=False,
        note: float = 0,
    ):
        self.name = name
        self.year_launch = year_launch
        self.multiplayer = multiplayer
        self.note = note
        self.__total_evaluation = 0
        self.__evaluators = 0
        Game.total_games += 1

    def __str__(self) -> str:
        return f"Game: {self.name}"

    def technical_sheet(self) -> None:
        """
        verifica ficha técnica
        """
        print(
            f"Nome do jogos {self.name}\n"
            f"Ano de lançamento: {self.year_launch}.\n"
            f"Multiplayer:{self.multiplayer}.\nNota: {self.note}"
        )

    def evaluate(self, note: float) -> None:
        self.__total_evaluation += note
        self.__evaluators += 1

    def average(self) -> None:
        print(
            f"Média do filme: {self.name}: {self.__total_evaluation / self.__evaluators}"
        )


class GameStudio:
    def __init__(self, name=""):
        self.name = name
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def evaluate_studio_quality(self):
        total_notes = sum(game.note for game in self.games)
        num_games = len(self.games)
        if num_games == 0:
            print(f"O estúdio {self.name} ainda não lançou jogo")
            return
        average_note = total_notes / num_games
        print(f"Avaliação média dos jogos do estúdio: {self.name}: {average_note:.2f}")


game1 = Game("The Legend of Zelda", 2017, False, 9.5)

studio = GameStudio("Awesome Games")
studio.add_game(game1)
studio.evaluate_studio_quality()

for game in studio.games:
    game.technical_sheet()
