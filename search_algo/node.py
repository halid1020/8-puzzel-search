class Node:
    """
    Represent a node in the state-space of a search problem.
    """

    def __init__(self, state, parent=None, action=None, cost=0):

        self.state = state          # The current state
        self.parent = parent        # Reference to the parent node
        self.action = action        # Action taken to reach this node
        self.cost = cost            # Path cost to reach this node
       
    
    # Override the less-than operator
    def __lt__(self, nxt):
            return self.cost < nxt.cost
    
    # Override the equal operator
    def __eq__(self, nxt):
        return self.state == nxt.state
