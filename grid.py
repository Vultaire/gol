from rules import alive_next_turn


class Grid(object):

    def __init__(self, bool_grid=None, coords=None):
        self._set = set()
        if bool_grid:
            for y, row in enumerate(bool_grid):
                for x, cell in enumerate(row):
                    if cell:
                        self[(x,y)] = True
        if coords:
            for x, y in coords:
                self[(x,y)] = True

    def __contains__(self, key):
        return key in self._set

    __getitem__ = __contains__

    def __setitem__(self, key, value):
        if value:
            self._set.add(key)
        else:
            self._set.discard(key)

    def __delitem__(self, key):
        self._set.discard(key)

    def __eq__(self, other):
        return self._set == other._set

    def __repr__(self):
        return repr(self._set)

    def get_num_of_neighbors(self, x, y):
        cells_to_test = [
            (x-1, y-1), (x, y-1), (x+1, y-1),
            (x-1, y),             (x+1, y),
            (x-1, y+1), (x, y+1), (x+1, y+1),
            ]
        count = 0
        for x2, y2 in cells_to_test:
            if (x2, y2) in self:
                count += 1
        return count

    def iterate(self):
        new_grid = Grid()
        for x, y in self.get_candidate_cells():
            neighbors = self.get_num_of_neighbors(x, y)
            alive_now = self[(x, y)]
            alive_next = alive_next_turn(neighbors, alive_now)
            if alive_next:
                new_grid[(x, y)] = True
        return new_grid

    def get_candidate_cells(self):
        candidates = set()
        for x, y in self._set:
            for x2 in xrange(-1, 2):
                for y2 in xrange(-1, 2):
                    candidates.add((x+x2, y+y2))
        return candidates

    def render(self, start_point, end_point):
        rows = []
        for y in xrange(start_point[1], end_point[1]):
            cells = []
            for x in xrange(start_point[0], end_point[0]):
                cells.append("X" if (x, y) in self else "_")
            rows.append(" ".join(cells))
        return "\n".join(rows)
