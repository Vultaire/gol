from rules import alive_next_turn

def test_underpop():
    assert not alive_next_turn(1, True)
def test_statusquo_2_neighbors_and_alive_stays_alive():
    assert alive_next_turn(2, True)
def test_statusquo_2_neighbors_and_dead_stays_dead():
    assert not alive_next_turn(2, False)
def test_statusquo_3_neighbors_and_alive_stays_alive():
    assert alive_next_turn(3, True)
def test_birth():
    assert alive_next_turn(3, False)
def test_overpop():
    assert not alive_next_turn(4, True)
