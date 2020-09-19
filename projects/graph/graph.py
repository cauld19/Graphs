"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
        

    def add_edge(self, v1, v2):
        
        if v1 not in self.vertices:
            return None
        else:
            self.vertices[v1].add(v2)
        

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]


    def bft(self, starting_vertex):
        q = Queue()
        
        q.enqueue(starting_vertex)
        visited = set()
        
        while q.size() > 0:
            current = q.dequeue()
        
            if current not in visited:
                print(current)
                visited.add(current)
                
                edges = self.get_neighbors(current)
                
                for edge in edges:
                    q.enqueue(edge)
                    
                    
    def dft(self, starting_vertex):
        s = Stack()
        
        s.push(starting_vertex)
        visited = set()
        
        while s.size() > 0:
            current = s.pop()
        
            if current not in visited:
                print(current)
                visited.add(current)
                
                edges = self.get_neighbors(current)
                
                for edge in edges:
                    s.push(edge)
            

    def dft_recursive(self, starting_vertex, visited = None):
        

        if visited is None:
            visited = set()
        
        visited.add(starting_vertex)
        
        print(starting_vertex)
        
        edges = self.vertices[starting_vertex]
        
        for edge in edges:
            if edge not in visited:
                self.dft_recursive(edge, visited)
            
        
            
            
        
            

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        
        path = []
        parent = {} ## keep track of vertex/edge relationships
        parent[starting_vertex] = None # set first parent to None
        visited = set()
        q.enqueue(starting_vertex)
        
        while q.size() > 0:
            current = q.dequeue()
            
        
            if current not in visited:
                visited.add(current)

                
                edges = self.get_neighbors(current)
                
                for edge in edges:
                    if destination_vertex in parent:
                        break
                    else:
                        parent[edge] = current
                    q.enqueue(edge)
                    
        while destination_vertex is not None: ## calculate shortest path from des to starting vertex
            path.insert(0, destination_vertex) ## add destination to path  
            destination_vertex = parent[destination_vertex] ## change destination to its parent
                         
        return path

    def dfs(self, starting_vertex, destination_vertex):
        s = Stack()
        parent = {}
        parent[starting_vertex] = None
        path = []
        
        visited = set()
        
        s.push(starting_vertex)
        
        while s.size() > 0:
            current = s.pop()
            print(current)
            
            if current not in visited:
                visited.add(current)
                
                edges = self.get_neighbors(current)
                
                for edge in edges:
                    if destination_vertex in parent:
                        break
                    else:
                        parent[edge] = current
                    s.push(edge)
                    
        while destination_vertex is not None: ## calculate path from des to starting vertex
            path.insert(0,destination_vertex) ## add destination to path  
            destination_vertex = parent[destination_vertex] ## change destination to its parent
            
        return path

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None, parent = None, path = None):
        if path == None:
            path = []
        
        if parent == None:
            parent = {}
            parent[starting_vertex] = None

        if visited == None:
            visited = set([starting_vertex])
            
        if starting_vertex == destination_vertex:
               
            while destination_vertex is not None: ## calculate path from des to starting vertex
                path.insert(0,destination_vertex) ## add destination to path  
                destination_vertex = parent[destination_vertex] ## change destination to its parent
                   

        for edge in self.get_neighbors(starting_vertex):
            if edge not in visited:
                if destination_vertex in parent:
                    break
                else:
                    parent[edge] = starting_vertex
                visited.add(edge)
                self.dfs_recursive(edge, destination_vertex, visited, parent, path)
                
        return path 
        

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)
    # print(graph.get_neighbors(2))

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)
    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
