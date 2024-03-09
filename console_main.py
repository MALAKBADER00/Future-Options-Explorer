from algorithms import * 

def display_intro():
    """Displays the introduction message for the program."""
    
    print("Welcome to the Future Options Explorer!")
    print("This program helps you find the optimal path from graduation (SQU) to retirement (Retire).")
    print("Choose an algorithm to explore your future options:")

def display_menu():
    """Displays the menu of available algorithms."""
    
    print("\n" + "-" * 40)
    print("1. Depth-First Search (DFS)")
    print("2. Breadth-First Search (BFS)")
    print("3. Uninformed Cost Search")
    print("4. A* Search")
    print("5. Hill Climbing")
    print("0. Exit")
     
def generate_description(optimal_path: list) -> str:
    """
    Generates a description of the optimal path.

    Parameters:
    - optimal_path: The optimal path from start to end.

    Returns:
    - Description of the journey along the optimal path.
    """
    descriptions = {
        "S": "Starting your journey in Sultan Qaboos University , then",
        "A": "you'll find yourself in Industry, more years later",
        "B": "you'll advance to Grad School, then",
        "C": "dedication leads you to becoming a Professor, after that",
        "D": "you'll reach Government service. Then,",
        "E": "more years of hard work, you'll embrace entrepreneurship.",
        "R": "Finally, Retirement awaits you, with years of relaxation and joy ahead... Enjoy the journey :)"
    }

    description = ""

    journey = []
    for i in range(0, len(optimal_path)):
        node = optimal_path[i]
        if i >= 0:
            journey.append(descriptions[node])
    description += " ".join(journey)

    return description 

def get_user_choice():
    """
    Prompts the user to enter a choice from the menu.

    Returns:
    - The user's choice.
    """
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 0 <= choice <= 5:
                return choice
            else:
                print("Invalid choice. Please enter a number between 0 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")      


def main():
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    S = "S"
    R = "R"
    graph = {
        A: {B: 2, R: 30},
        B: {A: 1, C: 12, D: 3, E: 3},
        C: {D: 6, E: 2},
        D: {E: 5, R: 21},
        E: {R: 40},
        S: {A: 5, B: 8, D: 4, E: 1},
        R: {}
    }
    heuristics = {
        A: 40,
        B: 30,
        C: 30,
        D: 35,
        E: 2,
        S: 25,
        R: 0
    }
    display_intro()
    
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == 0:
            print("GoodBye...")
            break
        
        algorithm_functions = [
            (DFS, graph, S, R),
            (BFS, graph, S, R),
            (Uninformed_cost_search, graph, S, R),
            (A_star_search, graph, S, R, heuristics),
            (hill_climbing, graph, S, R, heuristics)
            ]
        
        algorithm_names = ["Depth-First Search (DFS)", "Breadth-First Search (BFS)",
                           "Uninformed Cost Search", "A* Search", "Hill Climbing"]
        
        print(f"\nYou chose: {algorithm_names[choice - 1]}\n")
        
        try:
            func , *arg = algorithm_functions[choice -1]
            path , cost , frontier_states = func(*arg)
            print("Your Journey Path:",path)
            print("Your Journey duration:",cost,"Years\n")
            print("Explore Your Journey Stations:\n"+ generate_description(path)+"\n")
            for state in frontier_states:
                print(state)

        except Exception as e:  
            print(f"An error occured: {str(e)}\n")
main() 