Please answer the following questions using the git [markdown syntax](https://guides.github.com/features/mastering-markdown/).  You should view this file on your repo on GitHub after pushing it to make sure it looks the way you wanted it to.  You can also use a browser extension (like [this one](https://chrome.google.com/webstore/detail/markdown-preview-plus/febilkbfcbhebfnokafefeacimjdckgl) for Chrome) to view your local file.

### (1) For a square NxN flipit problem, what is a **simple** upper bound on the size of the search space (i.e., number of possible states)?  Explain your answer.**

Since each cell in the NxN grid can have two values (0 or 1), a simple upper bound is 2**(N*N)

### (2) What is a better upper bound for the number of possible states taking rotations and reflections into account? Explain your answer.**

This one is tricky.  In general, we might take into account rotations of the board as well as reflections around various axes (e.g., vertical, horizontal and diagonal).  However, we can't just so something simple like dived the naive upper bound by 16, since some states (e.g., all 1s) to not have unique rotations. See [here](https://math.stackexchange.com/questions/570003/how-many-unique-patterns-exist-for-a-n-times-n-grid) for a general solution.  For a 5x5 gird, it turns out that there are just 6814 unique patterns.

### (3) For a given NxN (for N>1) flipit problem, if a solution is possible, are more than one solutions always possible. Explain your answer.

yes.  Given a solution, we can always derive another by selecting a cell on the that solution not once, but three times in a row.

### (4) Is every flipit problem on a 2x2 grid solvable?  Explain how you arrived at your answer.

Yes.  We can prove this by showing a solution for every possible starting state.  This can be done by hand or using our python solution.

### (5) Is every flipit action reversible.  That is if performing action A in state S1 yields state S2, will performing action A in state S2 yield S1?

Yes.  We could prove this by considering all possible context around a cell to be selected and showing that selecting it twice in a row always yields the initial state.

### (6) Describe the heuristic you used in your FlipIt_optimal problem in English and explain why it is admissible, i.e., never over-estimates the distance of a state to the nearest goal state.

A simple optimal heuristic is the number of 1s in the state divided by five rounded up.  Our goal is to eliminate all 1s on the grid.  The largest number of 1s that can be changed to a 0 by one move is 5. If a state has N 1s, then the smallest number of moves that could eliminate them all would be obtained if each move turned five 1s to 0s.

### (6) Describe the heuristic you used in your FlipIt_aggressive problem in English and explain why it is not admissible, i.e., it sometimes over-estimates the distance of a state to the nearest goal state.

A simple aggressive heuristic is the number of 1s on the board.  Given the 2x2 flipit state 0001, this heuristic returns one, but the shortest solution requires three moves (e.g., 2, 1, 3)
