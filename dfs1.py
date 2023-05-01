graph = {
    'A': ['B','C','D'],
    'B': ['E','F'],
    'E': ['K','L'],
    'F': ['L','M'],
    'C': ['G','H'],
    'G': ['N'],
    'H': ['O','P'],
    'D': ['I','J'],
    'P': ['U'],
    'I': ['P','Q'],
    'J': ['R'],
    'K': ['S'],
    'L': ['T'],
    'T': ['F'],
    'S': [],
    'T': [],
    'M': [],
    'N': [],
    'O': [],
    'U': [],
    'Q': [],
    'R': []
}
target = input("Enter target node :")
visited = set() # Set to keep track of visited nodes.
path=[]
def dfs(graph,node,target,visited):
    if node not in visited:
        visited.add(node)
        path.append(node)
        if node == target:
            return node==target
        for ele in graph[node]:
            if dfs(graph,ele,target,visited):
                return True




result=dfs(graph,'A',target,visited)
if result:
    print(path)
    exit()
 
