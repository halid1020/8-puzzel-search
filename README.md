# Search Algorithms

Author: Halid Abdulrahim Kadi

This repository provides Python implementation of search algorithms for Module CS5011 Artificial Intelligence Practice at the School of Computer Science. University of St Andrews.

### I. Installation

You do not a need special package installation, but you do need to have `Python` installed in your machine.

### II. Running

This repository supports Breadth First Search (`bfs`),  A* search (`a_start`) as well as the iterative and recursive version of Depth First Search (`dfs_it` and `dfs_rec`). We do not provide the implementation of other algorithms, as we would like to examine your ability in the regarding practical.

To run `bfs` with an custom set initial  state for 8 puzzel, please simply type the following at the root directory of this repository:

```
python run.py --algo bfs --initial_state 1 2 3 4 0 5 6 7 8

# The initial state of the above example look like this:
#########
# 1 2 3 #
# 4 0 5 #
# 6 7 8 #
#########
```
