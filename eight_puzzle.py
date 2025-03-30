from search_problem import SearchProblem

class EightPuzzle(SearchProblem):
    """
    Represent a search problem for the 8-puzzle.
    States are represented as tuples of 9 integers.
    """
    def __init__(self, initial_state):
        self.initial_state = initial_state  # The starting state of the problem

    def transition_fn(self, state, action):
        """ The transition function that takes a state and an action and returns a new state."""
        state_list = list(state)
        blank_index = state_list.index(0)
        new_index = blank_index
        if action == 'up':
            new_index = blank_index - 3
        elif action == 'down':
            new_index = blank_index + 3
        elif action == 'left':
            new_index = blank_index - 1
        elif action == 'right':
            new_index = blank_index + 1
        # Swap the blank tile with the adjacent tile
        state_list[blank_index], state_list[new_index] = state_list[new_index], state_list[blank_index]
        return tuple(state_list)

    def goal_checker(self, state):
        """ Checks if a given state satisfies the goal condition."""
        return state == (0, 1, 2, 3, 4, 5, 6, 7, 8)

    def allowed_act_fn(self, state):
        """ Returns a list of allowed actions for a given state. """
        blank_index = state.index(0)
        allowed_actions = []
        # Check possible moves
        if blank_index >= 3:
            allowed_actions.append('up')
        if blank_index <= 5:
            allowed_actions.append('down')
        if blank_index % 3 != 0:
            allowed_actions.append('left')
        if (blank_index + 1) % 3 != 0:
            allowed_actions.append('right')
        return allowed_actions

    def cost_fn(self, state, action):
        """ Computes the cost of applying an action to a given state."""
        return 1.0



    ###################################################################
    ###################################################################

    def heuristic_fn(self, state):
        return self.heuristic_fn_1(state)
    
    def heuristic_fn_2(self, state):
        """ Computes the heuristic value (Manhattan distance) of a given state."""
        goal_positions = {
            0: (0, 0), 1: (0, 1), 2: (0, 2),
            3: (1, 0), 4: (1, 1), 5: (1, 2),
            6: (2, 0), 7: (2, 1), 8: (2, 2)
        }
        total_distance = 0.0
        for index in range(9):
            value = state[index]
            if value == 0:
                continue
            goal_row, goal_col = goal_positions[value]
            current_row = index // 3
            current_col = index % 3
            distance = abs(current_row - goal_row) + abs(current_col - goal_col)
            total_distance += distance
        return total_distance
    
    def heuristic_fn_1(self, state):
        """ Computes the heuristic value (number of misplaced tiles) of a given state."""
        total_misplaced = 0
        for index in range(9):
            value = state[index]
            if value != 0 and value != index:
                total_misplaced += 1
        return total_misplaced