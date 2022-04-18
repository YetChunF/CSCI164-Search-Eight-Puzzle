# CSCI164-Search-Eight-Puzzle

## Documentation

### Running different algorithms

The main command line tool should be used as shown below:

```
python3 Main.py <algorithm> <state list>
```

The algorithm can simple be any of the following values: `bfs, dfs, iddfs, astar, idastar`. The state list must be separated by commas and each tile must be one of the following characters: `"012345678ABCDEF"`. Here is an example:

```
python3 Main.py astar 1,6,0,2,7,3,4,8,5
```

The python command may vary depending on your OS. On Windows it may be `py`.

### Using the puzzle animation function

Requirements: MUST HAVE PYGAME INSTALLED. Feel free to open up a virtual environment and use the
requirements.txt file I've provided. If you're feeling dangerous, you can also just run `pip install -r requirements.txt` to simply install the correct pygame version globally. This is not recommended.

Start by simply importing the animation library.
```python
import animate
```

The run_animations function takes one parameter: a list of solutions. Each solution must be a list of puzzle states. Notice how it is a LIST of LISTS! Do not try running the script with only a one-dimensional list of puzzle states.

Here is an example script. Feel free to copy/paste the code and try it out!

```python
import animate

solutions = [['462301587', '402361587', '042361587', '342061587', '342601587', '342610587', '340612587', '304612587', '314602587', '314682507', '314682057', '314082657', '014382657', '104382657', '140382657', '142380657', '142308657', '142358607', '142358670', '142350678', '142305678', '102345678', '012345678']]
animate.run_animations(solutions)
```

Here is a practical example that uses the iterative deepening A* function in the astar library.

```python
import animate
import astar

solutions = []
s, fbound = astar.ida_star("462301587", "012345678")
solutions.append(s)
s, fbound = astar.ida_star("160273485", "012345678")
solutions.append(s)
animate.run_animations(solutions)
```

