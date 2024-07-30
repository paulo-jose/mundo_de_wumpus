import numpy as np

class WumpusWorld:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.knowledge_matrix = np.full((grid_size, grid_size), 'unknown')
        self.probability_matrix = np.zeros((grid_size, grid_size))
        self.auxiliary_matrix = np.zeros((grid_size, grid_size))
        self.agent_position = (0, 0)
        
        # Initialize the agent's starting position knowledge
        self.knowledge_matrix[self.agent_position] = 'safe'

    def move_agent(self, new_position):
        self.agent_position = new_position
        self.update_perception()
        self.update_probabilities()

    def update_perception(self):
        x, y = self.agent_position
        # Example perception update, can be expanded with real observations
        self.knowledge_matrix[x, y] = 'safe'  # or 'wumpus', 'pit', 'gold'
        self.update_adjacent_perceptions(x, y)

    def update_adjacent_perceptions(self, x, y):
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.grid_size and 0 <= ny < self.grid_size:
                if self.knowledge_matrix[nx, ny] == 'unknown':
                    self.auxiliary_matrix[nx, ny] += 1  # Example increment, can be more sophisticated
                    self.probability_matrix[nx, ny] = self.calculate_probability(nx, ny)

    def calculate_probability(self, x, y):
        # Example probability calculation based on auxiliary matrix and Bayesian update
        prior_prob = self.probability_matrix[x, y]
        likelihood = self.calculate_likelihood(x, y)
        evidence = self.calculate_evidence(x, y)
        return (likelihood * prior_prob) / evidence

    def calculate_likelihood(self, x, y):
        # Calculate likelihood based on neighboring perceptions
        likelihood = 1
        if x > 0:
            if 'stench' in self.knowledge_matrix[x-1, y]:
                likelihood *= 0.8  # Adjust based on actual model
        if x < self.grid_size-1:
            if 'stench' in self.knowledge_matrix[x+1, y]:
                likelihood *= 0.8
        if y > 0:
            if 'stench' in self.knowledge_matrix[x, y-1]:
                likelihood *= 0.8
        if y < self.grid_size-1:
            if 'stench' in self.knowledge_matrix[x, y+1]:
                likelihood *= 0.8
        return likelihood

    def calculate_evidence(self, x, y):
        # Calculate evidence as the sum of likelihoods across all hypotheses
        evidence = 0.5  # Example, should be adjusted based on actual evidence calculation
        return evidence

    def update_probabilities(self):
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                if self.knowledge_matrix[x, y] == 'unknown':
                    self.probability_matrix[x, y] = self.calculate_probability(x, y)

    def display_matrices(self):
        print("Knowledge Matrix:")
        print(self.knowledge_matrix)
        print("Probability Matrix:")
        print(self.probability_matrix)
        print("Auxiliary Matrix:")
        print(self.auxiliary_matrix)

# Example usage
wumpus_world = WumpusWorld(grid_size=4)
wumpus_world.display_matrices()

# Move the agent and update matrices
wumpus_world.move_agent((1, 2))
wumpus_world.display_matrices()

wumpus_world.move_agent((2, 2))
wumpus_world.display_matrices()

wumpus_world.move_agent((3, 3))
wumpus_world.display_matrices()
