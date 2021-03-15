class GameStats:
    #Track statistics for game
    def __init__(self,ai_game):
        #init stats
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        #initialize stats that can change during game
        self.ships_left = self.settings.ship_limit