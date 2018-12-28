from enum import IntEnum


class RPSData:
    def __init__(self, user_id: int, channel, num_rounds: int):
        assert num_rounds > 0
        assert num_rounds % 2 == 1
        self.opponent = user_id
        self.channel = channel
        self.num_rounds = num_rounds
        self.goal_score = (num_rounds//2) + 1
        self.bot_score = 0
        self.opponent_score = 0
        self.winner = "None"
        self.input_status = False
        self.early_status = False
        self.early_shot = False
        self.user_input = None

    def opponent_won(self):
        if self.winner is "None":
            self.opponent_score += 1
            if self.is_game_over():
                self.winner = "You"

    def bot_won(self):
        if self.winner is "None":
            self.bot_score += 1
            if self.is_game_over():
                self.winner = "I"

    def is_game_over(self):
        if self.opponent_score >= self.goal_score or self.bot_score >= self.goal_score:
            return True
        return False

    def get_winner(self):
        return self.winner

    def get_opponent(self):
        return self.opponent

    def get_channel(self):
        return self.channel

    def accept_input(self):
        self.input_status = True

    def refuse_input(self):
        self.input_status = False

    def get_input_status(self):
        return self.input_status

    def set_early(self):
        self.early_status = True

    def set_not_early(self):
        self.early_status = False

    def get_early_status(self):
        return self.early_status

    def reset_early_shot(self):
        self.early_shot = False

    def early_input(self):
        self.early_shot = True

    def is_early_shooter(self):
        return self.early_shot

    def reset_user_input(self):
        self.user_input = None

    # Should be RPSChoices
    def set_user_input(self, user_input):
        self.user_input = user_input

    def get_user_input(self):
        return self.user_input

    def get_game_data(self):
        return {"opponent id": self.opponent, "channel": self.channel, "max rounds": self.num_rounds,
                "bot score": self.bot_score, "opponent score": self.opponent_score, "winner": self.winner,
                "input status": self.input_status, "early status": self.early_status, "shot early": self.early_shot}


class RPSChoices(IntEnum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2
    GUN = 99


class RPSResults(IntEnum):
    LOSE = -1
    DRAW = 0
    WIN = 1
