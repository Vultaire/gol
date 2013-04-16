def alive_next_turn(num_neighbors, is_alive_now):
    if num_neighbors == 3:
        return True
    if num_neighbors == 2:
        return is_alive_now
    return False
