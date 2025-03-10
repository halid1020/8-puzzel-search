def get_action_sequence(node):
    """
    Get the sequence of actions taken to reach a node.
    """
    actions = []
    while node.parent is not None:
        actions.append(node.action)
        node = node.parent
    actions.reverse()
    return actions