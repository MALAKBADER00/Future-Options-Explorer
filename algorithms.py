from typing import List, Tuple, Dict

class Node:
    """
    Represents a node in the search graph.

    Attributes:
    - name: The name of the node.
    - path: The path from the start node to this node.
    - cost: The cost of reaching this node from the start node.
    """
    def __init__(self, name: str, path: List[str], cost: int = None):
        self.name = name
        self.path = path
        self.cost = cost
        
    def __lt__(self, other: 'Node') -> bool:
        """Comparison method for nodes based on their cost."""
        return self.cost < other.cost    
  
    def __str__(self) -> str:
        """String representation of the node."""
        return f"Node: {self.name}, Path: {self.path}, Cost: {self.cost}"


def DFS(graph, start, goal) -> Tuple[List[str], int]:
    """
    Depth-First Search (DFS) algorithm explores as far as possible along each branch before backtracking.

    Parameters:
    - graph: The graph represented as a dictionary.
    - start: The starting node.
    - goal: The goal node.

    Returns:
    - Tuple containing the optimal path, its cost, and frontier states explored.
    """
    frontier_states = []
    visited = set()
    stack = [Node(start, [], 0)]

    while stack:
        current_node = stack.pop()
        iteration = []
        for node in stack:
            if node.path not in iteration:
                iteration.append(node.path)
        if iteration not in frontier_states:       
            frontier_states.append(iteration)

        if current_node.name == goal:
            frontier_states.append(iteration + [current_node.path + [current_node.name]])
            return current_node.path + [current_node.name], current_node.cost, frontier_states
        
        if current_node.name not in visited:
            visited.add(current_node.name)

            for next_node, edge_cost in list(graph[current_node.name].items()):
                new_path = current_node.path + [current_node.name]
                new_cost = current_node.cost + edge_cost
                new_node = Node(next_node, new_path, new_cost)
                stack.append(new_node)

    return [], 0, frontier_states
    
def BFS(graph, start, goal) -> Tuple[List[str], int]:
    """
    Breadth-First Search (BFS) algorithm explores all neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.

    Parameters:
    - graph: The graph represented as a dictionary.
    - start: The starting node.
    - goal: The goal node.

    Returns:
    - Tuple containing the optimal path, its cost, and frontier states explored.
    """
    frontier_states = []
    visited = set()
    queue = [Node(start, [], 0)]
    
    while queue:
        current_node = queue.pop(0)
        iteration = []
        for node in queue:
            if node.path not in iteration:
                iteration.append(node.path)
        if iteration not in frontier_states:       
            frontier_states.append(iteration)

        if current_node.name == goal:
            frontier_states.append(iteration + [current_node.path + [current_node.name]])
            return current_node.path + [current_node.name], current_node.cost, frontier_states

        if current_node.name not in visited:
            visited.add(current_node.name)
            
            for next_node, next_cost in graph[current_node.name].items():
                new_path = current_node.path + [current_node.name]
                new_cost = current_node.cost + next_cost
                new_node = Node(next_node, new_path, new_cost)
                queue.append(new_node)

    return [], 0, frontier_states

def Uninformed_cost_search(graph, start, end) -> Tuple[List[str], int]:
    """
    Uninformed Cost Search algorithm explores nodes in the order of their total path costs from the start node.

    Parameters:
    - graph: The graph represented as a dictionary.
    - start: The starting node.
    - end: The goal node.

    Returns:
    - Tuple containing the optimal path, its cost, and frontier states explored.
    """
    frontier_states = []
    visited = set()
    priority_queue = [Node(start, [], 0)]
    
    while priority_queue:
        priority_queue.sort(key=lambda x: x.cost)
        current_node = priority_queue.pop(0)
        
        iteration = []
        for node in priority_queue:
            if node.path not in iteration:
                iteration.append(node.path)
        if iteration not in frontier_states:       
            frontier_states.append(iteration)
        
        if current_node.name == end:
            frontier_states.append(iteration + [current_node.path + [current_node.name]])
            return current_node.path + [current_node.name], current_node.cost, frontier_states

        if current_node.name not in visited:
            visited.add(current_node.name)

            for neighbor, edge_cost in graph[current_node.name].items():
                new_cost = current_node.cost + edge_cost
                new_path = current_node.path + [current_node.name]
                new_node = Node(neighbor, new_path, new_cost)
                priority_queue.append(new_node)

    return [], 0, frontier_states

def A_star_search(graph, start, end, h_table) -> Tuple[List[str], int]:
    """
    A* Search algorithm finds the optimal path from start to end node using heuristics.

    Parameters:
    - graph: The graph represented as a dictionary.
    - start: The starting node.
    - end: The goal node.
    - h_table: A heuristic table containing estimated costs from each node to the goal node.

    Returns:
    - Tuple containing the optimal path, its cost, and frontier states explored.
    """
    frontier_states = []
    visited = set()
    priority_queue = [Node(start, [start], (0, h_table[start] + 0))] 

    while priority_queue:
        priority_queue.sort(key=lambda x: x.cost[1])  
        current_node = priority_queue.pop(0)
        
    
        iteration = [node.path for node in priority_queue if node.path not in iteration]
        if iteration not in frontier_states:       
            frontier_states.append(iteration)
        
        if current_node.name not in visited:
            visited.add(current_node.name)

            if current_node.name == end:
                return current_node.path, current_node.cost[0], frontier_states

            for next_node, cost in graph[current_node.name].items():
                if next_node not in visited:
                    new_path_cost = cost + current_node.cost[0]
                    new_heuristic = h_table[next_node] + new_path_cost
                    new_path = current_node.path + [next_node] 
                    priority_queue.append(Node(next_node, new_path, (new_path_cost, new_heuristic)))

    return [], 0, frontier_states
  
def hill_climbing(graph, start, goal, heuristic_values) -> Tuple[List[str], int]:
    """
    Hill Climbing algorithm is a local search algorithm that iteratively makes small improvements
    to a current solution until no further improvements can be made.

    Parameters:
    - graph: The graph represented as a dictionary.
    - start: The starting node.
    - goal: The goal node.
    - heuristic_values: Heuristic values for nodes in the graph.

    Returns:
    - Tuple containing the optimal path, its cost, and frontier states explored.
    """
    frontier_states = []
    explored = set()
    stack = [Node(start, [start], (heuristic_values[start], 0))]

    while stack:
        stack.sort(key=lambda x: x.cost)
        current_node = stack.pop()
        
        if current_node.path not in frontier_states:
            frontier_states.append(current_node.path)
        
        if current_node.name == goal:
            return current_node.path, current_node.cost[1], frontier_states

        explored.add(current_node.name)
        
        for neighbor in graph[current_node.name]:
            if neighbor not in explored:
                neighbor_cost = heuristic_values[neighbor] 
                
                if neighbor_cost < current_node.cost[0]:
                    new_path = current_node.path + [neighbor]
                    if new_path not in frontier_states:
                        frontier_states.append(new_path)
                    new_cost = current_node.cost[1] + graph[current_node.name][neighbor]
                    new_node = Node(neighbor, new_path, (neighbor_cost, new_cost))
                    stack.append(new_node)

    return [], 0, frontier_states