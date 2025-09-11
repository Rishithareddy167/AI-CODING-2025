from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in self.adj_list.get(node, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
        return result

    def dfs_recursive(self, start):
        visited = set()
        result = []
        def dfs(node):
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in self.adj_list.get(node, []):
                    dfs(neighbor)
        dfs(start)
        return result

    def dfs_iterative(self, start):
        visited = set()
        stack = [start]
        result = []
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in reversed(self.adj_list.get(node, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return result


if __name__ == "__main__":
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 6)

    print("BFS:", g.bfs(1))
    print("DFS Recursive:", g.dfs_recursive(1))
    print("DFS Iterative:", g.dfs_iterative(1))