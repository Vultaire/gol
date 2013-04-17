from grid import Grid

def test_get_nonexistant_cell():
    grid = Grid()
    assert not ((1,1) in grid)

def test_set_and_get_cell():
    grid = Grid()
    grid[(0,0)] = True
    assert grid[(0,0)]

def test_set_clear_and_get_cell():
    grid = Grid()
    grid[(0,0)] = True
    del grid[(0,0)]
    assert not grid[(0,0)]

def test_large_negative_indices():
    grid = Grid()
    x, y = -0x7FFFFFFF, -0x3FFFFFFF
    grid[(x,y)] = True
    assert grid[(x,y)]


class TestPopulatedGrid(object):

    def setUp(self):
        self.grid = self._create_grid_from_lists([
                [0,0,0,1,0],
                [0,0,1,0,1],
                [0,0,0,0,0],
                ])

    def _create_grid_from_lists(self, lists):
        grid = Grid()
        for y, row in enumerate(lists):
            for x, cell in enumerate(row):
                if cell:
                    grid[x,y] = True
        return grid

    def test_get_num_of_neighbors(self):
        test_y, test_x = 1, 3   # 2nd row, 4th col
        expected_num = 3
        real_num = self.grid.get_num_of_neighbors(test_x, test_y)
        assert expected_num == real_num

    def test_get_candidate_cells(self):
        assert (
            self.grid.get_candidate_cells() ==
            set([
                       (2,-1),(3,-1),(4,-1),
                (1,0), (2,0), (3,0), (4,0), (5,0),
                (1,1), (2,1), (3,1), (4,1), (5,1),
                (1,2), (2,2), (3,2), (4,2), (5,2),
            ]))

    def test_iterate(self):
        next_grid = self._create_grid_from_lists([
                [0,0,0,1,0],
                [0,0,0,1,0],
                [0,0,0,0,0],
                ])

        new_grid = self.grid.iterate()
        assert new_grid == next_grid

    def test_grid_render(self):
        assert self.grid.render((0,0), (5,3)) == """\
_ _ _ X _
_ _ X _ X
_ _ _ _ _"""


def test_create_grid_via_constructor():
    grid = Grid(
        [
            [0,1,0],
            [0,1,0],
            [1,1,0],
        ])

    # Test instantiated data
    assert not grid[(0,0)]
    assert grid[(1,0)]
    assert not grid[(2,0)]
    assert not grid[(0,1)]
    assert grid[(1,1)]
    assert not grid[(2,1)]
    assert grid[(0,2)]
    assert grid[(1,2)]
    assert not grid[(2,2)]

    # Test point outside of supplied data
    assert not grid[(999,-999)]
