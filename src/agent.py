import random

class Agent:
    def __init__(self, name):
        """Initializes an agent with a name, starting balance, and no cards."""
        self.name = name
        self.balance = 1000.0
        self.cards = 0

    def decide_action(self, current_price, previous_price):
        """Decides the action to take; to be overridden by subclasses."""
        return "hold"

class RandomAgent(Agent):
    def decide_action(self, current_price, previous_price):
        """Randomly decides to buy, sell, or do nothing."""
        return random.choice(["buy", "sell", "hold"])

class TrendAgent(Agent):
    def decide_action(self, current_price, previous_price):
        """
        Follows a trend: if the price has increased by 1% or more,
        it prefers to buy; otherwise, it mostly holds.
        """
        if current_price >= previous_price * 1.01:
            return random.choices(["buy", "hold"], [0.75, 0.25])[0]
        else:
            return random.choices(["sell", "hold"], [0.2, 0.8])[0]

class AntiTrendAgent(Agent):
    def decide_action(self, current_price, previous_price):
        """
        Acts against the trend: if the price has decreased by 1% or more,
        it prefers to buy; otherwise, it mostly holds.
        """
        if current_price <= previous_price * 0.99:
            return random.choices(["buy", "hold"], [0.75, 0.25])[0]
        else:
            return random.choices(["sell", "hold"], [0.2, 0.8])[0]

class CustomAgent(Agent):
    def decide_action(self, current_price, previous_price):
        """
        Custom logic to maximize profit: buys when price is low, sells when high.
        Ensures to end with zero cards.
        """
        if self.cards > 0 and current_price > 250:
            return "sell"
        elif self.balance > current_price and current_price < 180:
            return "buy"
        return "hold"
