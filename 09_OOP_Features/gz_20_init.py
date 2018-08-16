class MusicPlayer:
    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        if self.init_flag is False:
            print("init")
            self.init_flag = True


player1 = MusicPlayer()
print(player1)
player2 = MusicPlayer()
print(player2)
