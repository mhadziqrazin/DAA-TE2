# Python program for solution of 
# hamiltonian path problem using backtracking

class Graph(): 
    def __init__(self, vertices): 
        self.graph = [[0 for column in range(vertices)]
                            for row in range(vertices)] 
        self.V = vertices 

    def isSafe(self, v, pos, path): 
        # Check if current vertex and last vertex 
        # in path are adjacent 
        if self.graph[ path[pos-1] ][v] == 0: 
            return False

        # Check if current vertex not already in path 
        for vertex in path: 
            if vertex == v: 
                return False

        return True

    # A recursive utility function to solve 
    # hamiltonian path problem 
    def hamPathUtil(self, path, pos): 

        # base case: if all vertices are 
        # included in the path 
        if pos == self.V: 
            return True

        # Try different vertices as a next candidate 
        # in Hamiltonian path.
        for v in range(0,self.V):
            if self.isSafe(v, pos, path): 

                path[pos] = v # add vertex to path

                if self.hamPathUtil(path, pos+1): 
                    return True

                # Remove current vertex if it doesn't 
                # lead to a solution 
                path[pos] = -1

        return False

    def hamPath(self): 

        for i in range(0, self.V):
            # try every vertex as starting point
            path = [-1] * self.V 
            path[0] = i

            if self.hamPathUtil(path,1): 
                # self.printSolution(path) 
                return True

        # print ("Solution does not exist\n")
        return False

    # def printSolution(self, path): 
    #     print ("Solution Exists: Following",
    #             "is one Hamiltonian path")
    #     for vertex in path: 
    #         print (vertex, end = " ")
    #     print()

g = Graph(3)
g.graph = [[0,1,1],[1,0,0],[1,0,0]]
g.hamPath()

# Driver Code 

# ''' Let us create the following graph 
#     (0)--(1)--(2) 
#     |    / \    | 
#     |   /   \   | 
#     |  /     \  | 
#     (3)-------(4) '''
# g1 = Graph(5) 
# g1.graph = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1], 
#             [0, 1, 0, 0, 1,],[1, 1, 0, 0, 1], 
#             [0, 1, 1, 1, 0], ] 

# # Print the solution 
# g1.hamPath(); 

# ''' Let us create the following graph 
#     (0)--(1)--(2) 
#     |    / \    | 
#     |   /   \   | 
#     |  /     \  | 
#     (3)       (4) '''
# g2 = Graph(5) 
# g2.graph = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1], 
#         [0, 1, 0, 0, 1,], [1, 1, 0, 0, 0], 
#         [0, 1, 1, 0, 0], ] 

# # Print the solution 
# g2.hamPath(); 

# This code is contributed by Divyanshu Mehta 