# Classe Pai/Mãe (Super classe) - Generalista


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


# Classe derivada - especializada
class SinglePlayerFame(Game):
    def __init__(self, name="", year_launch=0, note=0, story_line=""):
        super().__init__(
            name=name, year_launch=year_launch, note=note, multiplayer=False
        )
        self.story_line = story_line

    def technical_sheet(self):
        super().technical_sheet()
        print(f"Enredo: {self.story_line}\n")


multi_game = SinglePlayerFame(
    name="Fortnite",
    year_launch=2017,
    note=9.5,
    story_line="Emocionante História de sobrevivência",
)

print(multi_game)
