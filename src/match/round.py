from awpy import Demo

class Round():
    def __init__(self, round: tuple):
        self.round_num =  round[0]
        self.start_tick = round[1]
        self.freeze_time_end_tick = round[2]
        self.end_tick = round[3]
        self.round_winner = round[5]
        self.winner_reason = round[6] # The reason the round_winner won
        self.bomb_plant = round[7] # None if the bomb wasn't planted or the tick of when bomb was planted
        self.bombsite = round[8] # bombsite where it was planted

    def __repr__(self):
        return f"""
        ROUND NUM: {self.round_num}
        START TICK: {self.start_tick}
        FREEZE END: {self.freeze_time_end_tick}
        END ROUND: {self.end_tick}
        ROUND WINNER: {self.round_winner}
        WINNER REASON: {self.winner_reason}
        BOMB PLANT: {self.bomb_plant}
        BOMBSITE: {self.bombsite}
        """



