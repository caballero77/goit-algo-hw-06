import networkx as nx
from geopy.distance import distance

capitals = {
    "Amsterdam": (52.3676, 4.9041),
    "Andorra la Vella": (42.5078, 1.5211),
    "Athens": (37.9838, 23.7275),
    "Belgrade": (44.7866, 20.4489),
    "Berlin": (52.5200, 13.4050),
    "Bern": (46.9481, 7.4474),
    "Bratislava": (48.1486, 17.1077),
    "Brussels": (50.8503, 4.3517),
    "Bucharest": (44.4268, 26.1025),
    "Budapest": (47.4979, 19.0402),
    "Chisinau": (47.0105, 28.8638),
    "Copenhagen": (55.6761, 12.5683),
    "Dublin": (53.3498, -6.2603),
    "Helsinki": (60.1695, 24.9354),
    "Kyiv": (50.4501, 30.5234),
    "Lisbon": (38.7223, -9.1393),
    "Ljubljana": (46.0569, 14.5058),
    "London": (51.5074, -0.1278),
    "Luxembourg": (49.6117, 6.1319),
    "Madrid": (40.4168, -3.7038),
    "Monaco": (43.7384, 7.4246),
    "Oslo": (59.9139, 10.7522),
    "Paris": (48.8566, 2.3522),
    "Podgorica": (42.4410, 19.2636),
    "Prague": (50.0755, 14.4378),
    "Pristina": (42.6629, 21.1655),
    "Reykjavik": (64.1355, -21.8954),
    "Riga": (56.9496, 24.1052),
    "Rome": (41.9028, 12.4964),
    "Sarajevo": (43.8563, 18.4131),
    "Skopje": (41.9973, 21.4280),
    "Sofia": (42.6977, 23.3219),
    "Stockholm": (59.3293, 18.0686),
    "Tallinn": (59.4370, 24.7535),
    "Tirana": (41.3275, 19.8187),
    "Vaduz": (47.1410, 9.5209),
    "Valletta": (35.8989, 14.5146),
    "Vienna": (48.2082, 16.3738),
    "Vilnius": (54.6872, 25.2797),
    "Warsaw": (52.2297, 21.0122),
    "Zagreb": (45.8150, 15.9819)
}

neighbors = {
    "Amsterdam": ["Brussels", "Berlin"],
    "Andorra la Vella": ["Madrid", "Paris"],
    "Athens": ["Skopje", "Sofia", "Valletta"],
    "Belgrade": ["Budapest", "Sofia", "Podgorica", "Skopje", "Sarajevo", "Zagreb"],
    "Berlin": ["Amsterdam", "Prague", "Warsaw", "Copenhagen"],
    "Bern": ["Paris", "Luxembourg", "Vienna"],
    "Bratislava": ["Vienna", "Budapest", "Prague", "Kyiv"],
    "Brussels": ["Amsterdam", "Luxembourg", "Paris"],
    "Bucharest": ["Sofia", "Budapest", "Belgrade"],
    "Budapest": ["Vienna", "Bratislava", "Bucharest", "Zagreb", "Belgrade", "Kyiv"],
    "Chisinau": ["Kyiv", "Bucharest"],
    "Copenhagen": ["Berlin", "Oslo", "Stockholm"],
    "Dublin": ["London"],
    "Helsinki": ["Tallinn"],
    "Kyiv": ["Warsaw", "Chisinau", "Budapest", "Bratislava"],
    "Lisbon": ["Madrid"],
    "Ljubljana": ["Zagreb", "Vienna"],
    "London": ["Dublin", "Paris", "Brussels"],
    "Luxembourg": ["Brussels", "Paris", "Bern"],
    "Madrid": ["Lisbon", "Andorra la Vella"],
    "Monaco": ["Paris"],
    "Oslo": ["Copenhagen", "Stockholm"],
    "Paris": ["Brussels", "Luxembourg", "Monaco", "Andorra la Vella", "London"],
    "Podgorica": ["Belgrade", "Sarajevo", "Tirana"],
    "Prague": ["Berlin", "Vienna", "Bratislava"],
    "Pristina": ["Skopje"],
    "Reykjavik": ["Oslo", "Dublin"],
    "Riga": ["Tallinn", "Vilnius"],
    "Rome": ["Ljubljana", "Valletta"],
    "Sarajevo": ["Belgrade", "Podgorica", "Zagreb"],
    "Skopje": ["Athens", "Belgrade", "Tirana", "Sofia", "Pristina"],
    "Sofia": ["Athens", "Belgrade", "Bucharest", "Skopje"],
    "Stockholm": ["Oslo", "Copenhagen", "Helsinki"],
    "Tallinn": ["Helsinki", "Riga"],
    "Tirana": ["Skopje", "Podgorica"],
    "Vaduz": ["Vienna"],
    "Valletta": ["Rome", "Athens"],
    "Vienna": ["Ljubljana", "Bratislava", "Budapest", "Prague", "Bern", "Vaduz"],
    "Vilnius": ["Riga", "Warsaw"],
    "Warsaw": ["Vilnius", "Berlin", "Prague", "Kyiv"],
    "Zagreb": ["Ljubljana", "Sarajevo", "Budapest", "Belgrade"]
}

G = nx.Graph()

for capital, coords in capitals.items():
    G.add_node(capital, pos=coords)

for capital1, neighbors_list in neighbors.items():
    for capital2 in neighbors_list:
        if capital1 in capitals and capital2 in capitals:
            dist = distance(capitals[capital1], capitals[capital2]).km
            G.add_edge(capital1, capital2, weight=dist)