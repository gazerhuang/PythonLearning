class Game:
    top_score = 0

    def __init__(self, name):
        self.name = name

    @staticmethod
    def show_help():
        print("help message")

    @classmethod
    def show_top_score(cls):
        print("top_score:%d" % cls.top_score)

    def start_game(self):
        print("start")
        self.top_score += 1


Game.show_help()
Game.show_top_score()
game = Game("G")
game.start_game()
