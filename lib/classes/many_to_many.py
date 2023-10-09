class Game:
    def __init__(self, title):
        if isinstance(title, str) and len(title) > 0:
            self._title = title
        else: raise ValueError("Title must be a non-empty string")

        self.result_list = []
        self.players_list = []
    
    @property
    def title(self):
        return self._title

    def results(self):
        return self.result_list

    def players(self):
        unique_list = set(self.players_list)
        player_list = list(unique_list)
        return player_list

    def average_score(self, player):
        total_scores = 0
        count = 0
        for result in self.result_list:
            if result.player == player:
                count += 1
                total_scores = total_scores + result.score
        return total_scores / count

class Player:
    def __init__(self, username):
        if isinstance(username, str) and len(username) >= 2 and len(username) <= 16:
            self._username = username
        else: raise ValueError("Username must be a string between 2 and 16")   

        self.result_list = []
        self.games_list = []

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and len(username) >= 2 and len(username) <= 16:
            self._username = username
        else: raise ValueError("Username must be a string between 2 and 16")   

    def results(self):
        return self.result_list

    def games_played(self):
        unique_list = set(self.games_list)
        games_list = list(unique_list)
        return games_list

    def played_game(self, game):
        return game in self.games_list

    def num_times_played(self, game):
        if self.played_game(game):
            return self.games_list.count(game)
        else:
            return 0

class Result:
    all = []
    
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        if not type(score) is int:
            raise ValueError("Score must be an integer between 1 and 5000")
        if score < 1 or score > 5000:
            raise ValueError("Score must be between 1 and 5000")
        self._score = score
        game.result_list.append(self)
        game.players_list.append(self.player)
        player.result_list.append(self)
        player.games_list.append(self.game)
        Result.all.append(self)
    
    @property
    def score(self):
        return self._score
