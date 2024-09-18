import random

class Market:
    def __init__(self, initial_price, initial_stock):
        """Initialize the market with an initial price and stock."""
        self.price = initial_price
        self.stock = initial_stock
        self.iteration = 0

    def run_simulation(self, agents, iterations):
        """
        Runs the simulation for a given number of iterations.
        
        Args:
            agents (list): List of agents participating in the market.
            iterations (int): Number of iterations to simulate.
        """
        for _ in range(iterations):
            self.iteration += 1
            # Shuffle agents to simulate random order of actions
            random.shuffle(agents)
            previous_price = self.price
            
            # Each agent makes a decision in turn
            for agent in agents:
                action = agent.decide_action(self.price, previous_price)
                self.execute_action(agent, action)
                # print(f"Iteration {self.iteration}: Agent {agent.name} performed action: {action}, Price = {self.price:.2f}, Stock = {self.stock}")
                

            # Print the current state of the market at intervals
            if self.iteration % 100 == 0:
                print(f"Iteration {self.iteration}: Price = {self.price:.2f}, Stock = {self.stock}")

    def execute_action(self, agent, action):
        """
        Executes the chosen action (buy, sell, or do nothing) by the agent.
        
        Args:
            agent: The agent performing the action.
            action (str): The action chosen by the agent ("buy", "sell", "hold").
        """
        if action == "buy" and self.stock > 0 and agent.balance >= self.price:
            # Agent buys a graphics card
            agent.balance -= self.price
            agent.cards += 1
            self.price *= 1.005  # Price increases by 0.5%
            self.stock -= 1
        elif action == "sell" and agent.cards > 0:
            # Agent sells a graphics card
            agent.balance += self.price
            agent.cards -= 1
            self.price *= 0.995  # Price decreases by 0.5%
