# fairsharer-testing

Runs num_iterations:
In each iteration the highest value in values gives a fraction (share) to both the left and right neighbor. 
The leftmost field is considered the neightbor of the rightmost field.

Examples:
fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0] 
fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]
Args values:
        1D array of values (list or numpy array)
    num_iteration:
        Integer to set the number of iterations

✨_Just a small example how to integrate a test function_✨
