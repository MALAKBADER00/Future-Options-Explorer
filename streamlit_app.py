import streamlit as st
import base64
from algorithms import *  


def display_streamlit_path(path):
    """
    Display the path in a Streamlit app with associated images.

    Parameters:
    - path (list): List of positions in the path.
    """
    names = {
        "A": "Industry",
        "B": "Grad School",
        "C": "Professor Job",
        "D": "Government",
        "E": "Entrepreneur",
        "R": "Retirement",
        "S": "SQU"
    }
    base64_img = []
    html_img_elements = []

    for i in path:
        position = names[i]
        i = i.lower()
        
        # Convert the PNG image to base64 format for displaying in HTML
        with open(f"img/{i}.png", "rb") as file:
            image_data = file.read()
        base64_img = base64.b64encode(image_data).decode()

        if position == "SQU":
            style_attribute = 'style="width: 6rem; height: 5rem;"'
        else:
            style_attribute = ''

        # Construct the HTML code for the image element
        html_code = f"""
            <li>
                <div class="content">
                    <img src="data:image/png;base64,{base64_img}" alt="Your Image" {style_attribute}>
                    <p>{position}</p>
                </div>
            </li>
            """
        html_img_elements.append(html_code)
    if len(path) > 3:
        path_len = (len(path) - 1) * 6 + 5
    else:
        path_len = (len(path) - 1) * 6 + 1

    # HTML code for the entire document
    html_code = f"""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>Document</title>
            <link rel="stylesheet" href="try.css" />
            <style>
                .path-bar {{
                    position: absolute;
                    top: 0; /* Updated to display content at the top */
                    left: 0; /* Updated to display content at the left */
                }}
                .path-bar ul {{
                    padding-left: 50px;
                    position: relative;
                    list-style-type: none;
                }}
                .path-bar ul::after {{
                    content: "";
                    position: absolute;
                    background: #31333F;
                    width: 3px;
                    height: {path_len}rem;
                    top: 0;
                    left: 40px;
                    margin-top: 3rem;
                    z-index: -1;
                }}
                .path-bar ul li {{
                    text-decoration: none;
                    margin-bottom: 1rem;
                }}
                .path-bar ul li .content {{
                    display: flex;
                    flex-direction: row;
                    gap: 0, 5rem;
                    text-align: center;
                    align-items: center;
                    align-content: center;
                }}
                .path-bar ul li img {{
                    width: 6rem;
                    height: 6rem;
                }}
                .path-bar ul li p {{
                    text-decoration: none;
                    position: relative;
                    color: #FF4B4B;
                    font-size: 1.5rem;
                    line-height: 1rem;
                    font-weight: 500;
                }}
                .path-bar ul li .content::before {{
                    content: "";
                    position: absolute;
                    background: #31333F;
                    width: 18px;
                    height: 18px;
                    left: 33px;
                    border-radius: 50px;
                }}
            </style>
        </head>
        <body>
            <div class="path-bar">
                <ul>
                    {''.join(html_img_elements)}
                </ul>
            </div>
        </body>
    </html>
    """

    st.components.v1.html(html_code, width=500, height=113*len(path), scrolling=True)
    
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


def main():
    """
    Main function to create the Streamlit app.
    """
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
  
    st.header("🚀 The Future Options Explorer!")
    st.markdown("Embark on a journey from SQU graduation to retirement with our interactive tool! Discover your path through various search algorithms and unlock thrilling opportunities ahead! ✨🔍")
    st.markdown("---")

    st.subheader("🗺️ Explore Roadmap of your journey")
    st.markdown("with associated costs and positions: A (Industry), B (Grad School), C (Professor), D (Government), E (Entrepreneur). Discover your optimal path!")
    st.image("img/graph.png", caption='', width=600)

    st.markdown("---")
    st.subheader("💡 Choose an algorithm to unveil your path:")
    algorithm_choices = ["Depth-First Search (DFS)",
                    "Breadth-First Search (BFS)",
                    "Uninformed Cost Search",
                    "A* Search",
                    "Hill Climbing"]
    chosen_algorithm = st.radio("", algorithm_choices)
    if st.button("Begin Journey🔍"):
        st.write(chosen_algorithm)

        # Call the appropriate algorithm function based on the user's selection
        algorithm_functions = {
            "Depth-First Search (DFS)": (DFS, graph, S, R),
            "Breadth-First Search (BFS)": (BFS, graph, S, R),
            "Uninformed Cost Search": (Uninformed_cost_search, graph, S, R),
            "A* Search": (A_star_search, graph, S, R, heuristics),
            "Hill Climbing": (hill_climbing, graph, S, R, heuristics)
        }

        # Call the selected algorithm function and display the path
        algorithm_function = algorithm_functions[chosen_algorithm]
        func , *arg = algorithm_function
        path , cost , frontier_states = func(*arg)
        display_streamlit_path(path)

        # Display the description of the journey
        description = generate_description(path)
        st.markdown("<h6>🧭 " + description + "</h6>", unsafe_allow_html=True)
        st.markdown(f"<h6>🕒 This journey will take {cost} years to be completed</h6>", unsafe_allow_html=True)

main()  
