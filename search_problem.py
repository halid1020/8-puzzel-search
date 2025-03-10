class SearchProblem():
    """
    Represent a search problem.
    """
    def __init__(self, initial_state):
        self.initial_state = initial_state  # The starting state of the problem

    def transition_fn(self, state, action):
        """ The transition function that takes a state and an action and returns a new state."""
        pass

    def goal_checker(self, state) -> bool:
        """ Checks if a given state satisfies the goal condition."""
        pass

    def allowed_act_fn(self, state):
        """ Returns a list of allowed actions for a given state. """
        pass

    def cost_fn(self, state, action) -> float:
        """ Computes the cost of applying an action to a given state."""

    def heuristic_fn(self, state) -> float:
        """ Computes the heuristic value of a given state."""
        pass