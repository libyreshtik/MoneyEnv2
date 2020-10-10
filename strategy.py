from envelope import Envelope


class BaseStrategy:
    def __init__(self, envelopes):
        self.envelopes = envelopes


class Automatic_BaseStrategy(BaseStrategy):
    def __init__(self, envelopes):
        super().__init__(envelopes)
        self.envelopes = envelopes
    
    def play(self):
        num = random.randrange(100)
        envelope = self.envelopes[num]
        print(envelope.display())

    def display(self):
        """
        display what this strategy is doing
        :return description:
        """
        return "Automatic BaseStrategey - take random envelope from the list of envelopes \n " \
               "and print how much money was in the envelope and that's how much you've got."

class N_max_strategy(BaseStrategy):
    def __init__(self, envelopes):
        super().__init__(envelopes)
        self.envelopes = envelopes
        self.N = 3

    def play(self):
        """
        play the game: open the envelopes until we find N envelopes with max money and then stop
        and print the amount of money
        :return none:
        """
        max_money = 0
        count = 0
        index = 0
        while index < 100 and count < self.N:
            if self.envelopes[index].money > max_money and not self.envelopes[index].used:
                max_money = self.envelopes[index].money
                count += 1
                self.envelopes[index].used = True
            index += 1
        print("you got: " + str(max_money) + " dollars")

    def display(self):
        """
        display what this strategy is doing
        :return description:
        """
        return "N max strategy - find N max envelopes, and when it found N maxes it stops \n " \
               "and print how much money was in the last envelope and that's how much you've got."

class More_then_N_percent_group_strategy(BaseStrategy):
    def __init__(self, envelopes, percent):
        super().__init__(envelopes)
        self.envelopes = envelopes
        self.percent = percent
