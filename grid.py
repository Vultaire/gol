from rules import alive_next_turn


class Grid(object):

    def __init__(self, data=None):
        self._set = set()
        if data:
            for y, row in enumerate(data):
                for x, cell in enumerate(row):
                    if cell:
                        self[(x,y)] = True
    def __contains__(self, key):
        return key in self._set
    def __setitem__(self, key, value):
        if value:
            self._set.add(key)
        else:
            self._set.discard(key)
    def __getitem__(self, key):
        # Could also be __contains__, but tests have not driven
        # development of __contains__ yet.  Not sure that this is a
        # good thing.
        return key in self._set
    def __delitem__(self, key):
        self._set.discard(key)
    def __eq__(self, other):
        return self._set == other._set
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
            alive = alive_next_turn(neighbors, self[(x, y)])
            if alive:
                new_grid[(x, y)] = True
        return new_grid
    def get_candidate_cells(self):
        candidates = set()
        for x,y in self._set:
            for x2 in xrange(-1, 2):
                for y2 in xrange(-1, 2):
                    #print (x,y), ":", (x+x2, y+y2)
                    candidates.add((x+x2, y+y2))
        return candidates
    def __repr__(self):
        return repr(self._set)
    def render(self, start_point, end_point):
        rows = []
        for y in xrange(start_point[1], end_point[1]):
            cells = []
            for x in xrange(start_point[0], end_point[0]):
                cells.append("X" if (x, y) in self else "_")
            rows.append(" ".join(cells))
        return "\n".join(rows)
