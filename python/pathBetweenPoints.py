# Given a list of Point objects (where a Point object has a name, and a list of names it is connected to),
# a starting Point object, and an ending Point object, return a possible path between the two Points.
# If there are multiple paths, return the shortest one. If there is no path, return “no path”.

# Example:
# listOfPoints = [
#   { name: "A", connections: ["B", "C"] },
#   { name: "B", connections: ["A", "E"] },
#   { name: "C", connections: ["A", "D"] },
#   { name: "D", connections: ["C"] },
#   { name: "E", connections: ["B", "F"] },
#   { name: "F", connections: ["E"] },
# ]

# $ pathBetweenPoints(listOfPoints, "A", "F")
# $ A -> B -> E -> F

# $ pathBetweenPoints(listOfPoints, "D", "B")
# $ D -> C -> A -> B

# $ pathBetweenPoints(listOfPoints, "A", "D")
# $ A -> C -> D


def pathBetweenPoints(listOfPoints, startPoint, endPoint):
    visited = []
    path = []

    def find_shortest_path(current_point):
     #    print(current_point)
        if current_point == endPoint:
            return path
        visited.append(current_point)
        for i in listOfPoints:
            if i['name'] == current_point:
                for j in i['connections']:
                    if j not in visited:
                        path.append(current_point)
                        return find_shortest_path(j)
        return "no path"
    return find_shortest_path(startPoint)


listOfPoints = [
    {"name": "A", "connections": ["B", "C"]},
    {"name": "B", "connections": ["A", "E"]},
    {"name": "C", "connections": ["A", "D"]},
    {"name": "D", "connections": ["C"]},
    {"name": "E", "connections": ["B", "F"]},
    {"name": "F", "connections": ["E"]},
]


print(pathBetweenPoints(listOfPoints, "A", "F"))
print(pathBetweenPoints(listOfPoints, "D", "B"))
print(pathBetweenPoints(listOfPoints, "A", "D"))
