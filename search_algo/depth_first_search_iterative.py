from search_algo.node import Node
from .utils import get_action_sequence

def dfs_iterative(problem): # graph version
    
    frontier_nodes = [] # A normal array can be used as a stack.
    frontier_nodes.append(Node(state=problem.initial_state))
    explored_states = set() # Hash Table.

    while frontier_nodes:
        node = frontier_nodes.pop() # Get a node from the stack, i.e., at the end of the array.   
        explored_states.add(node.state)

        if problem.goal_checker(node.state):
            print('Explored states:', len(explored_states))
            return get_action_sequence(node) # Back traverse the nodes through theirs parents.

        for action in reversed(problem.allowed_act_fn(node.state)):
            next_state = problem.transition_fn(node.state, action)
            cost = node.cost + problem.cost_fn(node.state, action) # path cost: g(n)
            child_node = Node(state=next_state,parent=node,action=action,cost=cost)
		  
            # Make sure the content of states is compared.	
            if (child_node.state in explored_states) or (child_node in frontier_nodes):
                continue

            frontier_nodes.append(child_node)
    
    print('Explored states:', len(explored_states))
   
    return None # No solution.
