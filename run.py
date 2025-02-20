from search_algo.breadth_first_search import breadth_first_search
from eight_puzzle import EightPuzzle

def visualise_state(state):
    ## Visualise the state of the 8-puzzle

    for i in range(3):
        for j in range(3):
            print(state[i * 3 + j], end=' ')
        print()
    print()

def visualise_solution(problem, solution):
    
    state = problem.initial_state
    print('Initial state:')
    visualise_state(state)
    print('Solution:', solution)

    for i, action in enumerate(solution):
        state = problem.transition_fn(state, action)
        print(f'\nAction {i+1}: {action}')
        visualise_state(state)


def main():
    problem = EightPuzzle((1, 2, 3, 4, 0, 5, 6, 7, 8))
    solution = breadth_first_search(problem)
    visualise_solution(problem, solution)


if __name__ == '__main__':
    main()