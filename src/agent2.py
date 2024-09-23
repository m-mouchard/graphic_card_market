import random

class Agents:
    def __init__(self, name):
        """Initialices an agent with a name, starting balance and no cards."""
        self.name = name
        self.balance = 1000.0
        self.cards = 0
    
    def decide_action(self, current_price, previous_price, iteration):
        """Decide action to be overwritten by subclasees"""
        return "hold"
    
class RandomAgent(Agents):
    def decide_action(self, current_price, previous_price, iteration):
        return random.choice(["buy", "sell", "hold"])
    
class TrendAgent(Agents):
    def decide_action(self, current_price, previous_price, iteration):
        if current_price >= previous_price * 1.01:
            return random.choices(["buy","hold"], [0.75,0.25])[0]
        else: 
            return random.choices(["sell","hold"], [0.20,0.80])[0]
            
class AntiTrendAgent(Agents):
    def decide_action(self, current_price, previous_price, iteration):
        if current_price <= previous_price * 0.99:
            return random.choices(["buy","hold"],[0.75,0.25])[0]
        else: 
            return random.choices(["sell","hold"],[0.20,0.80])[0]

# class CustomAgent(Agents):
#     def decide_action(self, current_price, previous_price, iteration):        
#         if current_price > previous_price and self.cards > 0 :
#             return "sell"
#         elif current_price < previous_price and iteration<998:
#             return "buy"
#         return "hold"            
    
class CustomAgent(Agents):
    def decide_action(self, current_price, previous_price, iteration):
        """
        Custom logic to maximize profit: buys when price is low, sells when high.
        Ensures to end with zero cards.
        """
        if self.cards > 0 and current_price > 250:
            return "sell"
        elif self.balance > current_price and current_price < 180:
            return "buy"
        return "hold"