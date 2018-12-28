class RPSData:
    def __init__(self, user_id: int, num_rounds: int):
        assert num_rounds > 0
        assert num_rounds % 2 == 1
        self.opponent = user_id
        self.num_rounds = num_rounds
        self.goal_score = (num_rounds//2) + 1
        self.bot_score = 0
        self.opponent_score = 0
        self.winner = "None"

    def opponent_won(self):
        if self.winner is "None":
            self.opponent_score += 1
            if self.is_game_over():
                self.winner = "Opponent"

    def bot_won(self):
        if self.winner is "None":
            self.bot_score += 1
            if self.is_game_over():
                self.winner = "Bot"

    def is_game_over(self):
        if self.opponent_score >= self.goal_score or self.bot_score >= self.goal_score:
            return True
        return False

    def get_game_data(self):
        return {"opponent id": self.opponent, "max rounds": self.num_rounds, "bot score": self.bot_score,
                "opponent score": self.opponent_score, "winner": self.winner}
