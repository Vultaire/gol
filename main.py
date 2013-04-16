import time

from grid import Grid

R_PENTOMINO_DATA = [
    #  xx
    # xx
    #  x
    # We'll offset by 10 so we can see what's going on (assuming 25x25 grid)
    (11,10), (12,10),
    (10,11), (11,11),
    (11,12)
    ]

GLIDER_DATA = [
    #  x
    #   x
    # xxx
    # Again, offsetting by 10
             (11,10),
                      (12,11),
    (10,12), (11,12), (12,12),
    ]

def create_grid(data):
    grid = Grid()
    for x, y in data:
        grid[x,y] = True
    return grid

def run_grid(grid, start_point, end_point, iterations):
    print "Initial state:"
    print grid.render(start_point, end_point)
    for i in xrange(iterations):
        time.sleep(1)
        print
        print "Iteration {0}:".format(i+1)
        grid = grid.iterate()
        print grid.render(start_point, end_point)
    

def main():
    grid = create_grid(R_PENTOMINO_DATA)
    #grid = create_grid(GLIDER_DATA)
    start_point = (0, 0)
    end_point = (25, 25)  # (excluded from set)
    run_grid(grid, start_point, end_point, 25)


if __name__ == "__main__":
    main()
