import heapq

# Goal board configuration
GOAL_STATE = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)  # 0 represents the blank tile '_'
)

# Precalculate goal positions for distance calculations
GOAL_POS = {
    GOAL_STATE[r][c]: (r, c)
    for r in range(3)
    for c in range(3)
    if GOAL_STATE[r][c] != 0
}

def manhattan_distance(state):
    """Calculates h(n) Manhattan distance to goal."""
    dist = 0
    for r in range(3):
        for c in range(3):
            val = state[r][c]
            if val != 0:
                gr, gc = GOAL_POS[val]
                dist += abs(r - gr) + abs(c - gc)
    return dist

class Node:
    def __init__(self, state, parent=None, action=None, g=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.g = g
        self.h = manhattan_distance(state)
        self.f = self.g + self.h

    def __lt__(self, other):
        return self.f < other.f

def get_blank_pos(state):
    for r in range(3):
        for c in range(3):
            if state[r][c] == 0:
                return r, c

def get_successors(node):
    successors = []
    r, c = get_blank_pos(node.state)

    # Valid blank tile moves
    moves = [
        ("UP", (r - 1, c)),
        ("DOWN", (r + 1, c)),
        ("LEFT", (r, c - 1)),
        ("RIGHT", (r, c + 1))
    ]

    for action, (nr, nc) in moves:
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_state = [list(row) for row in node.state]
            new_state[r][c], new_state[nr][nc] = new_state[nr][nc], new_state[r][c]
            tuple_state = tuple(tuple(row) for row in new_state)

            child = Node(tuple_state, parent=node, action=action, g=node.g + 1)
            successors.append(child)

    return successors

def solve_8_puzzle(initial_state):
    start_node = Node(initial_state)
    frontier = []
    counter = 0
    heapq.heappush(frontier, (start_node.f, counter, start_node))
    explored = set()

    while frontier:
        _, _, current = heapq.heappop(frontier)

        if current.state == GOAL_STATE:
            path = []
            curr = current
            while curr:
                path.append(curr)
                curr = curr.parent
            path.reverse()
            return path

        if current.state in explored:
            continue
        explored.add(current.state)

        for child in get_successors(current):
            if child.state not in explored:
                counter += 1
                heapq.heappush(frontier, (child.f, counter, child))

    return None

def print_board(state):
    for row in state:
        print(" ".join(str(val) if val != 0 else "_" for val in row))

def main():
    print("Enter initial board state row by row (use numbers 1-8 and 0 or _ for blank):")
    matrix = []
    for i in range(3):
        while True:
            row_str = input(f"Row {i+1}: ").strip().replace('_', '0')
            vals = row_str.split()
            if len(vals) == 3 and all(v.isdigit() for v in vals):
                matrix.append(tuple(int(v) for v in vals))
                break
            print("Invalid input. Enter 3 space-separated numbers (e.g., '1 2 3' or '7 _ 8').")

    initial_state = tuple(matrix)

    print("\nInitial State:")
    print_board(initial_state)
    print("\nSolving...")

    path = solve_8_puzzle(initial_state)

    if path:
        for step_idx, step in enumerate(path):
            if step.action:
                print(f"Move {step_idx}: {step.action}")
                print_board(step.state)
                print()
        print("Goal State Reached")
        print(f"Solution Cost = {path[-1].g}")
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()