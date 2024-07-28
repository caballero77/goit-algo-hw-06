import folium
from graph import G, capitals
import networkx as nx


def visualize_capitals(graph, capitals):
    m = folium.Map(location=[54.5260, 15.2551], zoom_start=4)

    for capital, coords in capitals.items():
        folium.Marker(
            location=[coords[0], coords[1]],
            popup=capital,
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(m)

    for edge in graph.edges(data=True):
        capital1, capital2, data = edge
        coord1 = capitals[capital1]
        coord2 = capitals[capital2]
        folium.PolyLine(
            locations=[coord1, coord2],
            color='gray',
            weight=1,
            opacity=0.5
        ).add_to(m)

    m.save('europe_capitals.html')


def analyze_graph(graph):
    print("Graph Analytics")
    print("================")

    num_nodes = graph.number_of_nodes()
    num_edges = graph.number_of_edges()
    print(f"Number of nodes: {num_nodes}")
    print(f"Number of edges: {num_edges}")

    print("\nList of capitals:")
    for capital in graph.nodes():
        print(capital)

    print("\nDegree of each capital:")
    for capital, degree in graph.degree():
        print(f"{capital}: {degree}")

    average_degree = sum(dict(graph.degree()).values()) / num_nodes
    print(f"\nAverage degree: {average_degree:.2f}")

    density = nx.density(graph)
    print(f"Graph density: {density:.4f}")


visualize_capitals(G, capitals)

analyze_graph(G)
