from search_algo.breadth_first_search import breadth_first_search
from search_algo.depth_first_search_iterative import dfs_iterative
from search_algo.depth_first_search_recursive import dfs_recursive
from search_algo.A_star import A_star_search

import argparse
from eight_puzzle import EightPuzzle

str2algo = {
    'bfs': breadth_first_search,
    'dfs_it': dfs_iterative,
    'dfs_rec': dfs_recursive,
    'a_star': A_star_search,
}

def visualise_state(state):
    ## Visualise the state of the 8-puzzle

    for i in range(3):
        for j in range(3):
            print(state[i * 3 + j], end=' ')
        print()
    print()

def visualise_solution(problem, solution):
    
    state = problem.initial_state
    print('\n##############################################')
    print('Initial state:')
    visualise_state(state)
    print('Solution:', solution)
    print('\n----------------------------------------------')

    for i, action in enumerate(solution):
        state = problem.transition_fn(state, action)
        print(f'\nAction {i+1}: {action}')
        visualise_state(state)


def main():
    arg_parser = argparse.ArgumentParser(description='Solve the 8-puzzle using various search algorithms.')
    arg_parser.add_argument('--initial_state', type=int, nargs=9, default=[1, 2, 3, 4, 0, 5, 6, 7, 8],
                            help='The initial state of the 8-puzzle.')
    arg_parser.add_argument('--algo', type=str, default='bfs', help='The search algorithm to use.')
    args = arg_parser.parse_args()

    algo = str2algo[args.algo]

    # Convert the list of integers to a tuple
    initial_state = tuple(args.initial_state)
    print(f"\nInput Initial state:{initial_state}\n")

    # Create the EightPuzzle instance with the provided initial state
    problem = EightPuzzle(initial_state)

    solution = algo(problem)
    visualise_solution(problem, solution)


if __name__ == '__main__':
    main()