def depth_limited_search(node, goal, graph, limit, path):
    if node == goal:
        return path + [node]
    if limit == 0:
        return 'cutoff'
    
    cutoff_occurred = False
    for child in graph.get(node, []):
        if child not in path:
            result = depth_limited_search(child, goal, graph, limit - 1, path + [node])
            if result != 'cutoff' and result != 'failure':
                return result
            if result == 'cutoff':
                cutoff_occurred = True
                
    if cutoff_occurred:
        return 'cutoff'
    else:
        return 'failure'


def iterative_deepening_search(initial, goal, graph, maximum_depth):
    for depth in range(maximum_depth + 1):
        result = depth_limited_search(initial, goal, graph, depth, [])
        if result != 'cutoff' and result != 'failure':
            return result, depth
    return None, None


def main():
    initial = input("Enter Initial State: ").strip()
    goal = input("Enter Goal State: ").strip()
    max_depth = int(input("Enter Maximum Depth: "))
    
    graph = {}
    print("\nEnter Search Tree (e.g. 'A: B, C' or 'B: -'). Press Enter on a blank line when finished:")
    
    while True:
        line = input().strip()
        if not line:
            break
        # Clean formatting like 'A: B, C' or 'B: -' to extract node and children
        cleaned = line.replace(":", " ").replace(",", " ").replace("-", " ")
        parts = cleaned.split()
        if parts:
            node = parts[0]
            children = parts[1:]
            graph[node] = children
            
    path, depth = iterative_deepening_search(initial, goal, graph, max_depth)
    
    if path:
        print(f"\nGoal '{goal}' found!")
        print(f"Solution Path: {' -> '.join(path)}")
        print(f"Found at Depth: {depth}")
    else:
        print(f"\nGoal '{goal}' not found within maximum depth of {max_depth}.")


if __name__ == "__main__":
    main()