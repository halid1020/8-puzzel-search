from search_algo.node import Node
from .utils import get_action_sequence

def dfs(problem, node, explored_states): # graph version
    if problem.goal_checker(node.state):
        print('Explored states:', len(explored_states))
        return get_action_sequence(node)
    
    explored_states.add(node.state)

    for action in problem.allowed_act_fn(node.state):
        next_state = problem.transition_fn(node.state, action)
        cost = node.cost + problem.cost_fn(node.state, action)
        child_node = Node(state=next_state, parent=node, action=action, cost=cost)

        if (child_node.state in explored_states):
            continue

        result = dfs(problem, child_node, explored_states)
        if result:
            return result
    
    return None



def dfs_recursive(problem): # graph version
    explored_states = set() # Hash Table
    #frontier_nodes = [] # A normal array can be used as a stack

    return dfs(problem, Node(state=problem.initial_state), explored_states)