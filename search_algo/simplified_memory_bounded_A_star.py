from search_algo.node import Node
from .utils import get_action_sequence
import math

class SMBA_Node(Node):
    def __init__(self, state, parent=None, action=None, cost=0, 
                 eval_=0, depth=0, is_leaf=False):
        super().__init__(state, parent, action, cost)
        self.eval = eval_
        self.depth = depth
        self.is_leaf = is_leaf
        self.forgotten = []

def ancestors(node):
    ancestors = []
    while node.parent is not None:
        ancestors.append(node.parent)
        node = node.parent
    return ancestors

def shrink_frontier(frontier_nodes, MAX_MEM):
    
    while len(frontier_nodes) > MAX_MEM:
        
        frontier_nodes.sort(key=lambda node: (not node.is_leaf, node.eval))

        # Remove the worst leaf node (assumed to be the last after sorting)
        worst_node = frontier_nodes.pop(-1)

        # Update the parent node if it exists
        if worst_node.parent is not None:
            
            worst_node.parent.forgotten.append(worst_node)

            least_f = min([n.eval for n in worst_node.parent.forgotten])
            worst_node.parent.eval = least_f

            # Determine if the parent is still a leaf
            worst_node.parent.is_leaf = any(
                n for n in frontier_nodes if worst_node.parent in ancestors(n)
            )

            if worst_node.parent.is_leaf:
                frontier_nodes.append(worst_node.parent)

def process_expand(node, problem, frontier_nodes, MAX_MEM=100):
    
    # Expand the current node
    success_list = node.forgotten.copy()  # Start with previously forgotten children
    if not success_list:  # If no forgotten children exist, generate successors
        for action in problem.allowed_act_fn(node.state):
            path_cost = node.cost + problem.cost_fn(node.state, action)
            #print('path cost', path_cost)
            eval_value = path_cost + problem.heuristic_fn(node.state)
            #print('cacl eval', eval_value)
            #assert eval_value < 0, "Heuristic should be non-negative"
            child_node = SMBA_Node(
                state=problem.transition_fn(node.state, action),
                parent=node, action=action,
                cost=path_cost, eval_=eval_value, depth=node.depth + 1
            )
            if child_node not in frontier_nodes:
                success_list.append(child_node)

    ret_list = []
    
    for child_node in success_list:
        if child_node in node.forgotten:
            node.forgotten.remove(child_node)
        elif (not problem.goal_checker(child_node.state)) and child_node.depth == MAX_MEM:
            child_node.eval = math.inf
        child_node.is_leaf = True
        child_node.parent.is_leaf = False
        ret_list.append(child_node)
    return ret_list

def SMA_star_search(problem, MAX_MEM=30):
    
    frontier_nodes = [SMBA_Node(state=problem.initial_state)]
    cnt = 0

    while frontier_nodes:  # Continue while there are nodes in the frontier
        
        frontier_nodes.sort(key=lambda node: (-node.eval, node.depth))
        node = frontier_nodes.pop(-1) # Select the newest node with the lowest evaluation value
        #print(node.eval)

        if problem.goal_checker(node.state):
            print('Explored states:', cnt)
            return get_action_sequence(node)  # Return the sequence of actions to reach the goal

        if node.eval == math.inf:
            return None
        
        cnt = cnt + 1

        success_list = process_expand(node, problem, frontier_nodes, MAX_MEM)
        frontier_nodes.extend(success_list) # Add successors to the frontier
        shrink_frontier(frontier_nodes, MAX_MEM)

    return None
