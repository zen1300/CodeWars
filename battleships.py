def _get_boats(board):
    boats = {}
    for x, row in enumerate(board):
        for y, col in enumerate(row):
            if col != 0:
                try:
                    boats[board[x][y]] += 1
                except KeyError:
                    boats[board[x][y]] = 1
    return boats


def damaged_or_sunk(board, attacks):
    boats = _get_boats(board)
    scores = {'sunk': 0, 'damaged': 0, 'not_touched': 0, 'points': 0}
    rows = len(board)
    results = {i: 0 for i in range(4)}
    for attack in attacks:
        adj_y = rows - attack[1]
        adj_x = attack[0] - 1
        results[board[adj_y][adj_x]] += 1

    for boat in boats:
        if results[boat] == 0:
            scores['not_touched'] += 1
            scores['points'] -= 1
        elif 0 < results[boat] < boats[boat]:
            scores['damaged'] += 1
            scores['points'] += 0.5
        elif results[boat] == boats[boat]:
            scores['sunk'] += 1
            scores['points'] += 1
    return scores


board = [[3, 0, 1],
         [3, 0, 1],
         [0, 2, 1],
         [0, 2, 0]]

attacks = [[2, 1], [2, 2], [3, 2], [3, 3]]
print(damaged_or_sunk(board, attacks))
