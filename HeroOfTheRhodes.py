from collections import defaultdict

class Island:
    
    #constuctor
    def __init__(self):
        self.graph = defaultdict(list)
    
    #adds edge
    def addEdge(self, u, v):
        self.graph[u].append(v)


    def findShortestPathDFS(self, start, goal):
        visited = set() #a set of visited nodes
        path = [] 
        all_paths = []

        def dfs(current, path):
            path.append(current)
            visited.add(current)

            if current == goal:
                all_paths.append(list(path))
            else:
                for neighbor in self.graph[current]:
                    if neighbor not in visited:
                        dfs(neighbor, path)

            path.pop()
            visited.remove(current)

        dfs(start, path)

        if not all_paths:
            return None
        
        # Find the shortest path (fewest nodes)
        shortest = min(all_paths, key=len)
        return shortest


if __name__ == "__main__":
    g = Island()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    g.addEdge(4, 5)
    g.addEdge(2, 4)

    shortest_path = g.findShortestPathDFS(0, 5)
    
    if shortest_path:
        print("Shortest path from 0 to 5 using DFS:", shortest_path)
    else:
        print("No path found from 0 to 5.")
