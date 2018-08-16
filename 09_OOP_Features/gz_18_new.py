class MusicPlayer:

    def __new__(cls, *args, **kwargs):
        print("new")
        ins = super().__new__(cls)
        return ins

    def __init__(self):
        print("init")


player = MusicPlayer()
print(player)
