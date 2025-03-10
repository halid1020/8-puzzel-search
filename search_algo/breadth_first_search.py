from search_algo.node import Node
from collections import deque
from .utils import get_action_sequence

def breadth_first_search(problem): # graph version
    
    frontier_nodes = deque() # FIFO queue data structure
    frontier_nodes.append(Node(state=problem.initial_state))
    explored_states = set() # Hash Table.

    while frontier_nodes:
        node = frontier_nodes.popleft() # Get a node from the queue       
        explored_states.add(node.state)	

        for action in problem.allowed_act_fn(node.state):
            next_state = problem.transition_fn(node.state, action)
            cost = node.cost + problem.cost_fn(node.state, action) # path cost: g(n)
            child_node = Node(state=next_state,parent=node,action=action,cost=cost)
		  
            # Make sure the content of states is compared.	
            if (child_node.state in explored_states) or (child_node in frontier_nodes):
                continue

            if problem.goal_checker(child_node.state):
                print('Explored states:', len(explored_states))
                return get_action_sequence(child_node) 

            frontier_nodes.append(child_node)
    
    print('Explored states:', len(explored_states))
   
    return None # No solution.
