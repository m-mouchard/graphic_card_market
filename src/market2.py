import random

class Market:
    def __init__(self, initial_price, initial_stock):
        self.price = initial_price
        self.stock = initial_stock
        self.iteration = 0

    def run_simulation(self, agents, iterations):

        for j in range(iterations):
            self.iteration +=1

            random.shuffle(agents)
            previous_price = self.price

            for agent in agents:
                action = agent.decide_action(self.price, previous_price, j)
                self.execute_action(agent,action)

            if self.iteration %100 == 0:
                print(f"iteration {self.iteration}: Price = {self.price:.2f}, Stock = {self.stock}")    
            

    def execute_action(self, agent, action):
        if action=="buy" and self.stock > 0 and agent.balance >= self.price:
            agent.cards += 1
            agent.balance -= self.price
            self.price *= 1.005
            self.stock -= 1
        elif action =="sell" and agent.cards >= 1:
            agent.cards -= 1
            agent.balance += self.price
            self.price *= 0.995
            self.stock += 1