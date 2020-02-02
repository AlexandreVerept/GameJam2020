from lib.scenes import SceneCollection


# Might be useless
class GameCollection(SceneCollection):
    def __init__(self):
        self.activeId = 0

    def get_id(self, game_id):
        if game_id >= self.size():
            return None

        return self.scenes[id]

    def set_active_id(self, game_id):
        game = self.get_id(game_id)

        if game:
            self.activeId = game

    def get_active_id(self):
        if not self.activeId:
            self.set_active_id(0)
            return self.get_active_id()

        return self.activeId