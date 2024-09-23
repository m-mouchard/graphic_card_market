from market2 import Market
from agent2 import RandomAgent, TrendAgent, AntiTrendAgent, CustomAgent

def create_agents():

    agents = []

    for i in range(51):
        agents.append(RandomAgent(name=f"Random Agent {i+1}"))
    
    for i in range(24):
        agents.append(TrendAgent(name = f"Tren Agent {i+1}"))

    for i in range(24):
        agents.append(AntiTrendAgent(name=f"Anti Trend Agent {i+1}"))

    agents.append(CustomAgent(name="Custom Agent"))

    return agents

def main():
    
    market = Market(initial_price=200, initial_stock=100000)

    agents = create_agents()

    market.run_simulation(agents,1000)

if __name__ == "__main__":
    main()