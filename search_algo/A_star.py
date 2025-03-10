from search_algo.node import Node
from .utils import get_action_sequence
import heapq

class AStarNode(Node):
    def __init__(self, state, parent=None, action=None, cost=0, eval=0):
        super().__init__(state, parent, action, cost)
        self.eval = eval

    # Override the less-than operator
    def __lt__(self, nxt):
        return self.eval < nxt.eval

def A_star_search(problem): # graph version
    
    frontier_nodes = [AStarNode(state=problem.initial_state)]
    heapq.heapify(frontier_nodes) # Priority queue for giving the lowest evaluated node first.
    explored_states = set()

    while frontier_nodes:
        node = heapq.heappop(frontier_nodes) # Get the node with lowest evaluation value.
        #print(node.eval)     
        explored_states.add(node.state)	
        
        if problem.goal_checker(node.state): 
            print('Explored states:', len(explored_states))
            return get_action_sequence(node) 

        for action in problem.allowed_act_fn(node.state):
            path_cost = node.cost + problem.cost_fn(node.state, action) 
            child_node = AStarNode(state=problem.transition_fn(node.state, action),
                              parent=node,action=action,
                              cost=path_cost,
                              eval=path_cost + problem.heuristic_fn(node.state))#f(n) = g(n) + h(n)  
            if (child_node.state in explored_states) or (child_node in frontier_nodes):
                continue	

            heapq.heappush(frontier_nodes, child_node)

    print('Explored states:', len(explored_states))
    return None
