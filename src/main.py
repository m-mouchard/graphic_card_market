from market import Market
from agent import RandomAgent, TrendAgent, AntiTrendAgent, CustomAgent

def create_agents():
    """Creates a list of agents with predefined behaviors for the simulation."""
    agents = []
    # Create 51 random agents
    for i in range(51):
        agents.append(RandomAgent(name=f"Random Agent {i+1}"))
    
    # Create 24 trend-following agents
    for i in range(24):
        agents.append(TrendAgent(name=f"Trend Agent {i+1}"))
    
    # Create 24 anti-trend agents
    for i in range(24):
        agents.append(AntiTrendAgent(name=f"Anti-Trend Agent {i+1}"))
    
    # Create 1 custom agent with personalized logic
    agents.append(CustomAgent(name="Custom Agent"))

    return agents

def main():
    """Main function to run the market simulation."""
    # Initialize the market with a starting price and stock
    market = Market(initial_price=200.0, initial_stock=100000)

    # Create agents for the market
    agents = create_agents()

    # Run the simulation for 1000 iterations
    market.run_simulation(agents, iterations=1000)

if __name__ == "__main__":
    main()
